# Django 기반 JWT 인증 API 샘플

## 환경

### 파이썬

- 3.6 버전 사용

### 라이브러리

> 자세한 사항은 `requirements.txt` 내용 참고

- Django==2.2.4
- djangorestframework==3.10.2
- djangorestframework-simplejwt==4.3.0

### 환경 설정

- 해당 리포지토리 클론
- 파이썬 가상환경 구동
- 라이브러리 설치 (`pip install -r requirements.txt`)
- 마이그레이션 진행 (`python manage.py migrate`)
- 유저 생성 (`python manage.py createsuperuser`)
- 개발 서버 구동 (`python manage.py runserver`)

## 사용법

### JWT 발급

- 요청
  ```
  curl -X POST \
  http://localhost:8000/auths/token/ \
  -H 'Content-Type: application/json' \
  -d '{"username": "admin", "password": "admin"}'
  ```
- 응답
  ```json
  {
    "refresh": "<리프래시용_JWT>",
    "access": "<인증용_JWT>"
  }
  ```
  - `"access"` : JWT 인증이 필요한 API 요청시 헤더에 추가할 토큰
  - `"refresh"` : `"access"` 토큰이 만료된 경우 (기본 5분) 재발급 API로 새 토큰을 발급받을 때 사용할 토큰, 이 토큰을 사용하면 사용자의 계정 정보를 다시 입력받을 필요 없음

### JWT 재발급

- 요청
  ```
  curl -X POST \
  http://localhost:8000/auths/token/refresh/ \
  -H 'Content-Type: application/json' \
  -d '{"refresh": "<리프래시_토큰>"}'
  ```
- 응답
  ```json
  {
    "access": "<인증용_JWT>"
  }
  ```

### JWT 검사

현재 가지고있는 토큰이 유효한지 검사하는 API. 클라이언트측에서는 JWT를 해석하기 위한 별도 로직을 작성할 필요 없어짐

- 요청
  ```
  curl -X POST \
  http://localhost:8000/auths/token/verify/ \
  -H 'Content-Type: application/json' \
  -d '{"token": "<JWT>"}'
  ```
- 응답
  - 성공 케이스
    ```json
    {}
    ```
  - 실패 케이스
    ```json
    {
      "detail": "Token is invalid or expired",
      "code": "token_not_valid"
    }
    ```

### JWT 사용 테스트

- 요청
  ```
  curl -X GET \
  http://localhost:8000/auths/hello/ \
  -H 'Authorization: Bearer <JWT>'
  ```
- 응답
  - 성공 케이스
    ```json
    {
      "message": "Hello, <username>"
    }
    ```
  - 실패 케이스
    ```json
    {
      "detail": "Given token not valid for any token type",
      "code": "token_not_valid",
      "messages": [
          {
              "token_class": "AccessToken",
              "token_type": "access",
              "message": "Token is invalid or expired"
          }
      ]
    }
    ```
