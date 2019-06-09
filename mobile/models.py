from django.db import models


# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=50, primary_key=True)  # 用户标识，QQ接口提供
    access_token = models.CharField(max_length=50, null=True)  # QQ接口访问令牌
    expires_time = models.IntegerField(null=True)  # 令牌到期时间
    nickname = models.CharField(max_length=50, null=True)  # 昵称
    figureurl = models.CharField(max_length=100, null=True)  # 头像url


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField(null=True)  # 时间戳(还原开始时间)
    moves = models.IntegerField(null=True)  # 步数
    result = models.IntegerField(null=True)  # 成绩(毫秒数)
