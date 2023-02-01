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

## 2. 시연영상

https://www.youtube.com/watch?v=9pXF6B2IQ54

## 3. stack

![image](https://user-images.githubusercontent.com/74058047/216101270-ebcbab0e-d588-4614-b873-42e356774a2e.png)<br>


## 4. flow

![image](https://user-images.githubusercontent.com/74058047/216101619-1c945fe9-036a-49d1-81cf-9526b410de1c.png)<br>


## 5. 구현화면

- 메인페이지<br>
![image](https://user-images.githubusercontent.com/74058047/216101838-4e027703-777a-4fea-b393-6d7154372d36.png)<br>

- 메인기능 : 용돈주기<br>
![image](https://user-images.githubusercontent.com/74058047/216102176-b2b0a332-792f-4208-a559-7ec5bab6ee0d.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216102374-271b0a60-be01-4352-b31e-3b56060ab967.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216102465-bf2995ea-f59e-4261-b490-6db92b748672.png)<br>
<br>

음성챗봇 활용 용돈주기<br>

![image](https://user-images.githubusercontent.com/74058047/216102953-1b75f2fb-6279-4d01-912c-7c365e15483b.png)<br>

정기용돈 관리 서비스<br>

![image](https://user-images.githubusercontent.com/74058047/216103094-2d3f8d25-2258-479f-a7a6-d5a1648df39c.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216103251-b73d8bf1-ffc3-499f-ac0c-773456d157be.png)<br>

- 메인기능 : 미션주기<br>

![image](https://user-images.githubusercontent.com/74058047/216103361-67158eb1-afad-4a70-baf8-fa60cde4f8b9.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216103460-5bebbf7b-df95-4d69-9f70-5260ca854e90.png)<br>


- UI만 구현<br>

![image](https://user-images.githubusercontent.com/74058047/216103733-c28dbe9e-84f0-4224-afff-5c71c9ad91ab.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216103682-53682f67-2f1f-454c-82f6-b8ecb9dc9403.png)<br>


