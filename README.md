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

![image](https://user-images.githubusercontent.com/74058047/216105986-7338c3ed-30d0-471d-83ee-43cffbf208f9.png)<br>

정기용돈 관리 서비스<br>
![image](https://user-images.githubusercontent.com/74058047/216106077-ba9583ac-0b30-44eb-b5af-6436a1e864e7.png)<br>
![image](https://user-images.githubusercontent.com/74058047/216106143-03dd1d33-20b9-489e-97de-564bbcb7875b.png)


- 메인기능 : 미션주기<br>

![image](https://user-images.githubusercontent.com/74058047/216106245-4d9658df-2051-4f7a-88be-46bed45da87a.png)
![image](https://user-images.githubusercontent.com/74058047/216106296-77ecc671-2ce2-4c03-a9db-19c611949539.png)
![image](https://user-images.githubusercontent.com/74058047/216106496-d6f1725e-5519-4796-a8e1-f8dc088bf624.png)


- UI만 구현<br>

![image](https://user-images.githubusercontent.com/74058047/216106562-7f41a0e9-ab65-4904-a266-16e98fbc3236.png)
![image](https://user-images.githubusercontent.com/74058047/216106685-844f21fa-c09a-4572-ad27-49369708f2ae.png)
![image](https://user-images.githubusercontent.com/74058047/216106750-b3944bf6-d626-4e14-99de-1ece7f46d113.png)
![image](https://user-images.githubusercontent.com/74058047/216106802-ff15fc64-f337-47e7-9ce5-143d710f28aa.png)


