# Fintech_Project
## 시니어를 위한 금융서비스


## 0. 세팅방법

###### 가상환경 패키지 설치
- clone을 진행할 폴더에서 가상환경 설치 후 활성화
``` c
python3 -m venv venv
cd venv/bin
source ./activate
```

- venv와 동일한 위치에서 클론
```c
git clone "repository code입력"
```

- requirementx.txt 동일 위치에서 패키지 설치
``` c
pip install -r requirements.txt
```

###### .env파일 등록
- manage.py와 동일한 위치
```c
DEBUG=on
SECRET_KEY="장고 secret_key 입력"
DB_PW="admin의 password입력"
invoke_url="naver-clova-invokeurl"
secret_key="naver-clova-secretkey"
```

## 1. 실행방법

###### 서버 실행방법
- manage.py와 동일한 위치에서 진행
``` c
python manage.py runserver
```

###### 데이터베이스 모델 저장 및 적용
- manage.py와 동일한 위치에서 진행
``` c
python manage.py makemigrations
python manage.py migrate
```
