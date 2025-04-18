from fastapi import FastAPI
from app.src.calendar_sync import get_upcoming_events
from app.src.notion_sync import create_notion_page
from app.scheduler import start_scheduler

app = FastAPI()
start_scheduler()

@app.get("/")
def read_root():
    return {"message": "Welcome to Planverse!"}

@app.get("/sync")
async def sync_calendar():
    events = get_upcoming_events()

    for event in events:
        summary = event["summary"]
        start = event["start"]
        location = event["location"]
        task_type = event["task_type"]
        create_notion_page(summary, start, location, task_type)

    return {"message": "캘린더 동기화 완료!"}
