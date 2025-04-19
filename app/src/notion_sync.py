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


def get_existing_notion_titles():
    headers ={
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # titles = []
    # for result in data.get("results", []):
    #     title_property = result["properties"].get("Name", {}).get("title", [])
    #     if title_property:
    #         titles.append(title_property[0]["text"]["content"])

    # return titles

    existing_titles = set()
    for page in data.get("results", []):
        title_property = page["properties"].get("Name", {}).get("title", [])
        if title_property:
            title_text = title_property[0]["text"]["content"]
            existing_titles.add(title_text)

    return existing_titles