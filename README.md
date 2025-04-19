# ✨ Planverse - 개인 일정 자동화 시스템

## 프로젝트 소개

**Planverse**는 구글 캘린더 일정을 자동으로 노션 데이터베이스에 동기화하고,
매일 아침 카카오톡 알림으로 오늘의 일정을 요약해 알려주는 자동화 프로젝트입니다.

> 오전 7시 → 노션 일정 업데이트  
> 오전 8시 → 카카오톡 알림 발송


## 폴더 구조

```
planverse/
├── app/
│   ├── main.py                # FastAPI 서버 구동
│   ├── scheduler.py            # 스케줄러 설정 (노션 업데이트 + 카톡 알림)
│   └── src/
│       ├── calendar_sync.py    # 구글 캘린더 이벤트 가져오기
│       ├── notion_sync.py      # 노션 페이지 생성 및 중복 체크
│       ├── daily_summary.py    # 오늘 일정 요약해서 알림 전송
│       └── kakao_alert.py      # 카카오톡 알림 API
├── .env                        # 키 저장 파일
├── requirements.txt            # 필요 패키지 목록
└── README.md                   # 프로젝트 설명
```


## 사용 기술

- **Python 3.9**
- **FastAPI** : API 서버
- **APScheduler** : 백그라운드 스케줄러
- **Google Calendar API** : 일정 가져오기
- **Notion API** : 일정 데이터 저장
- **Kakao API** : 카카오톡 알림 보내기


## 설치 및 실행 방법

1. 프로젝트 클론

```bash
git clone <레포지터리 URL>
cd planverse
```

2. 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate    # (Mac/Linux)
venv\Scripts\activate.bat   # (Windows)
```

3. 패키지 설치

```bash
pip install -r requirements.txt
```

4. `.env` 파일 설정

```env
GOOGLE_CLIENT_ID=구글 클라이언트 ID
GOOGLE_CLIENT_SECRET=구글 클라이언트 Secret
NOTION_TOKEN=노션 API 토큰
NOTION_DATABASE_ID=노션 데이터베이스 ID
KAKAO_ACCESS_TOKEN=카카오톡 토큰
```

5. 서버 실행

```bash
uvicorn app.main:app --reload
```


##  주의사항

- 구글 API 인증 시 최고 1회 수동 로그인 필요 (token 저장함)
- 카카오톡 메시지 전송을 위해 talk_message scope에 동의해야 함

