from apscheduler.schedulers.background import BackgroundScheduler
from app.src.calendar_sync import get_upcoming_events
from app.src.notion_sync import create_notion_page, get_existing_notion_titles
from app.src.daily_summary import send_daily_summary
from app.src.kakao_alert import send_kakao_alert
import requests
import os

def sync_job():
    print("스케줄러가 자동으로 캘린더를 동기화합니다...")
    try :
        events = get_upcoming_events()
        print(f"불러온 이벤트 개수: {len(events)}개")
        existing_titles = get_existing_notion_titles()

        for event in events:
            summary = event["summary"]
            start = event["start"]
            location = event["location"]
            task_type = event["task_type"]

            if summary in existing_titles:
                print(f"중복 발견, 추가 스킵: {summary}")
                continue

            create_notion_page(summary, start, location, task_type)
            print(f"노션에 추가 완료: {summary}")

        print("캘린더 동기화 및 노션 업데이트 완료!")

        send_kakao_alert("Planverse 일정이 노션에 업데이트 되었습니다!")

    except Exception as e:
        print("스케줄러 오류:", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_job, 'cron', day_of_week='sun', hour=7, minute=0)
    # scheduler.add_job(sync_job, 'interval', minutes=1) # test
    scheduler.add_job(send_daily_summary, 'cron', hour=8, minute=0)
    # scheduler.add_job(send_daily_summary, 'interval', minutes=5) # test
    scheduler.start()
