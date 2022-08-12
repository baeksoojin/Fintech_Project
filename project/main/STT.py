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


client_id = env("client_id")
client_secret =  env("client_secret")
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('audio.ogg', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": env("client_id"),
    "X-NCP-APIGW-API-KEY": env("client_secret"),
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)
