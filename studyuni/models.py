from django.db import models

# Create your models here.

class user(models.Model):
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class course(models.Model):
    id=models.IntegerField(primary_key=True)
    cse=models.CharField(max_length=30)
    starttime=models.CharField(max_length=20)
    endtime=models.CharField(max_length=20)

