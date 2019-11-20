from django.db import models

from django.contrib.auth.models import AbstractUser

class UsersProfile(AbstractUser):
    gender_choice=(
      ('1',"男"),
      ('2',"女"),
    )
    mobile = models.CharField('手机', max_length=11)
    gender = models.CharField("性别",choices=gender_choice,default="1",max_length=1)  #性别这个字段可以不写
    avatar = models.ImageField(verbose_name="头像", upload_to='users/%Y/%m/%d/', max_length=128,
                                              null=True,blank=True)
    age = models.IntegerField("年龄",default=18)
