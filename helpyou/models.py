from django.contrib.auth.models import AbstractUser
from django.db import models
import os

#from helpyou.views import CustomUser


# 회원가입
class CustomUser(AbstractUser):


    username = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디') #unique=True,
    password1 = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    password2 = models.CharField(max_length=128, verbose_name='유저 비밀번호 확인')
    fullname = models.CharField(max_length=16, verbose_name='유저 이름') #unique=True,
    address = models.CharField(max_length=128, verbose_name='유저 주소')
    detailed_address = models.CharField(max_length=128, verbose_name='유저 상세 주소')
    year = models.CharField(max_length=4, verbose_name='년도')
    month = models.CharField(max_length=2, verbose_name='월')
    day = models.CharField(max_length=2, verbose_name='일')
    phone_number = models.CharField(max_length=13, verbose_name='전화번호')
    email = models.EmailField(max_length=128, verbose_name='유저 이메일') #unique=True,





    def __str__(self):
        return self.username


    class Meta: #DB 테이블명 지정
        db_table = 'customuser' #테이블명 지정
        verbose_name = '유저' #해당 테이블의 닉네임
        verbose_name_plural = '유저' #verbose_name_plural 등록하지 않으면 복수형으로 표시될때가 있으니 똑같이 적어줌


