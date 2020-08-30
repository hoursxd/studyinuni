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

class room(models.Model):
    id=models.IntegerField(primary_key=True)
    cseid=models.IntegerField()
    site1=models.IntegerField()
    site2=models.IntegerField()
    site3=models.IntegerField()
    site4=models.IntegerField()
    site5=models.IntegerField()
    site6=models.IntegerField()
    site7=models.IntegerField()
    site8=models.IntegerField()