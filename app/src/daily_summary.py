from app.src.calendar_sync import get_upcoming_events
from app.src.kakao_alert import send_kakao_alert
import datetime

def send_daily_summary():
    events = get_upcoming_events()

    if not events:
        message = "오늘은 예정된 일정이 없습니다."
    else:
        today = datetime.date.today()
        today_events = []
        for event in events:
            start_date = event["start"].split("T")[0]
            if start_date == today.isoformat():
                today_events.append(f"- {event['summary']} ({event['start']})")

        if today_events:
            message = "🗓️ 오늘의 일정입니다:\n" + "\n".join(today_events)
        else:
            message = "오늘은 예정된 일정이 없습니다."

    send_kakao_alert(message)
