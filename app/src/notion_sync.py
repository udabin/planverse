# app/src/notion_sync.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
NOTION_API_URL = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_notion_page(summary: str, start: str, location: str, task_type):
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": summary
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                    "start": start
                }
            },
            "Location": {
                "rich_text": [
                    {
                        "text": {
                            "content": location
                        }
                    }
                ]
            },
            "Task Type": {
                "select": {
                    "name" : task_type
                }
            }
        }
    }
    response = requests.post(NOTION_API_URL, headers=headers, json=data)

    response.raise_for_status()
