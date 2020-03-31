from django.db import models

# Create your models here.


class UserInfo(models.Model):
    '''
    用户表
    '''
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)


class Blog(models.Model):
    '''
    博客表
    '''
    title = models.CharField(verbose_name="标题",max_length=32)
    content = models.CharField(verbose_name="内容",max_length=100)
    author = models.ForeignKey(verbose_name="作者",to="UserInfo",on_delete=models.CASCADE)
