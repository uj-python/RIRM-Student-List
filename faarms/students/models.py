from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField
from django.db.models.signals import pre_save
from phone_field import PhoneField

import time

# Create your models here.

class Studentsinfo(models.Model):
    Roll_No=models.IntegerField(primary_key=True,unique=True)
    Name=models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    School=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.Roll_No)

class StudentAcademics(models.Model):
    Roll_No=models.OneToOneField("Studentsinfo", on_delete=models.CASCADE)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()

    def __str__(self) -> str:
        return str(self.Roll_No)