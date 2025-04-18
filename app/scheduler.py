from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os

def sync_job():
    print("⏰ 스케줄러가 자동으로 캘린더를 동기화합니다...")
    try:
        response = requests.get("http://127.0.0.1:8000/sync")
        if response.status_code == 200:
            print("캘린더 동기화 성공:", response.json())
        else:
            print("캘린더 동기화 실패:", response.text)
    except Exception as e:
        print("스케줄러 오류:", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_job, 'cron', hour=7, minute=0)
    # scheduler.add_job(sync_job, 'interval', minutes=1)
    scheduler.start()
