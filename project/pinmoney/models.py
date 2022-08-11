from django.db import models
from user.models import User

# Create your models here.
class Pinmoney(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) #보낸사람 계정에 데이터 저장
    date = models.DateField()
    amount = models.IntegerField()
    text = models.TextField()
    receiver = models.CharField(max_length=100) #받은사람

class Regular(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) #보낸사람 계정에 데이터 저장
    date = models.IntegerField() # 정기용돈 전송일
    unit = models.CharField(max_length=2) # 정기용돈 전송단위
    amount = models.IntegerField()
    type = models.TextField()
    receiver = models.CharField(max_length=100) #받은사람