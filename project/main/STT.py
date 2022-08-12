import os
import requests
from pathlib import Path
import environ
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


print("현재경로======> ",os.getcwd(),"\n")
os.chdir("../../../")
print("현재경로======> ",os.getcwd(),"\n")
os.chdir("../Downloads")
print("현재경로======> ",os.getcwd(),"\n")

def get_text(title):

    print("현재경로======> ",os.getcwd(),"\n")
    print(title)
    title = title.replace(':','_')
    print(title)
    lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = open('{0}.ogg'.format(title), 'rb')
    # data = open('{0}.ogg'.format("Fri Aug 12 2022 19_32_51 GMT+0900 (한국 표준시)"), 'rb')
    
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": env("client_id"),
        "X-NCP-APIGW-API-KEY": env("client_secret"),
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url,  data=data, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        print (response.text)
        return response.text
    else:
        print("Error : " + response.text)

# get_text()
