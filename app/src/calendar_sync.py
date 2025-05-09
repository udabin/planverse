import os
import datetime
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


load_dotenv()
# print("GOOGLE_CREDENTIALS_PATH", os.getenv("GOOGLE_CREDENTIALS_PATH"))

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "client_secret.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")


def get_calendar_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def classify_task(summary):
    summary = summary.lower()
    if any(keyword in summary for keyword in ['회의', '미팅', '컨퍼런스']):
        return "업무(Meeting)"
    elif any(keyword in summary for keyword in ['운동', '헬스', '러닝']):
        return "운동(Workout)"
    elif any(keyword in summary for keyword in ['점심', '저녁', '브런치']):
        return "식사(Meal)"
    elif any(keyword in summary for keyword in ['스터디', '공부', '강의', '1-1']):
        return "학습(Study)"
    elif any(keyword in summary for keyword in ['휴가', '여행']):
        return "휴식(Rest)"
    else:
        return "기타(Etc)"

def get_upcoming_events():
    service = get_calendar_service() 

    now = datetime.datetime.utcnow() #.isoformat() + "Z"
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + datetime.timedelta(days=1)

    # 일주일 동기화 하고 싶으면 아래 코드 사용 (일 ~ 토)    
    # if now.weekday() != 6:
    #     days_to_subtract = now.weekday() + 1
    #     start_of_week = now - datetime.timedelta(days=days_to_subtract)
    # else:
    #     start_of_week = now

    # end_of_week = start_of_week + datetime.timedelta(days=6)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=today_start.isoformat() + "Z",
        timeMax=today_end.isoformat() + "Z",
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    event_list = []
    for event in events:
        summary = event.get("summary", "No Title")
        start = event["start"].get("dateTime", event["start"].get("date"))
        location = event.get("location", "No Location")
        task_type = classify_task(summary)

        event_list.append({
            "summary":summary,
            "start": start,
            "location": location,
            "task_type": task_type
        })
    
    return event_list

