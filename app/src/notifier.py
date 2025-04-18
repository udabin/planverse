import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("KAKAO_ACCESS_TOKEN")

def send_kakao_message(message_text):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message_text,
            "link": {
                "web_url": "https://google.com",
                "mobile_web_url": "https://google.com"
            },
            "button_title": "바로가기"
        })
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print("카카오톡 알림 성공!")
    else:
        print("카카오톡 알림 실패:", response.text)
