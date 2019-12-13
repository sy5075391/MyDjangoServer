from django.db import models

# Create your models here.

from django.db import models
import uuid


class Article(models.Model):
    title = models.CharField(u"标题", max_length=256)
    content = models.TextField(u"内容")
    time = models.DateTimeField(u"时间")


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
    name = models.CharField(max_length=10, null=False)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now=True, null=False)


class Animals(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now=True, null=False)


# Create your models here.
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1(), editable=False, null=False)
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=80, null=False)
    time = models.DateTimeField(auto_now=True, null=False)
