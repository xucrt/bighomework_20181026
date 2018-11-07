from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(default="nickname",max_length=18)
    def __str__(self):
        return "{}_{}".format(self.nickname,self.username)

class Plate(models.Model):
    title = models.CharField(max_length=16)
    users = models.ManyToManyField(to=User, related_name="plates")
    def __str__(self):
        return "板块：{}".format(self.title)

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    users = models.ForeignKey(to=User,related_name="posts")
    column = models.ForeignKey(to=Plate,related_name="posts")
    createtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "文章：{}".format(self.title,)

class Reply(models.Model):
    user = models.ForeignKey(to=User,related_name="replys")
    post = models.ForeignKey(to=Post,related_name="replys")
    content = models.TextField()
    createtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "回复：{}".format(self.content)