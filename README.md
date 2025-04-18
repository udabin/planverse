# Planverse 🌌

**구글 캘린더 → 노션 일정 자동 동기화** 프로젝트


## 기능

- 구글 캘린더의 일정을 읽어와서
- 노션 데이터베이스에 자동으로 추가
- 일정 내용에 따라 Task 타입 분류 (업무/미팅/기타)
- 매일 자동 스케줄링으로 동기화


## 기술 스택

- Python 3.10+
- FastAPI
- APScheduler
- Notion API
- Google Calendar API


## 설치 방법

```bash
git clone [YOUR_REPO_URL]
cd planverse
pip3 install -r requirements.txt
