from django.db import models
from user.models import User

# Create your models here.
class Mission(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #보낸사람 계정에 데이터 저장
    date = models.DateField(null=True)#시작일
    reward = models.IntegerField(null=True) #용돈보상
    text = models.TextField(null=False) #미션내용
    receiver = models.CharField(max_length=100, null=True) #받은사람
    finish = models.BooleanField(default=False) #True일때 완료

class MissionList(models.Model):
    text = models.TextField(null=False)