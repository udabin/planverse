import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

KAKAO_TOKEN = os.getenv("KAKAO_ACCESS_TOKEN")
KAKAO_API_URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

def send_kakao_alert(message: str):
    headers = {
        "Authorization": f"Bearer {KAKAO_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "template_object": {
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://google.com",
                "mobile_web_url": "https://google.com"
            }
        }
    }

    response = requests.post(
        KAKAO_API_URL,
        headers=headers,
        data={"template_object": json.dumps(payload["template_object"])}
    )

    response.raise_for_status()
    return response.json()


# FastAPI endpoint 에서 호출할 함수
async def send_alert():
    message = "Planverse 일정이 업데이트되었습니다! ✨"
    send_kakao_alert(message)
    return {"message": "카카오 알림톡 전송 완료!"}
