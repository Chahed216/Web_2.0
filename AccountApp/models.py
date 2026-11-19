from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Speciality(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=true)
    updated_at = models.DateTimeField(auto_now=true)

class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True)
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=true)
    updated_at = models.DateTimeField(auto_now=true)
    specialities =  models.ManyToManyField(
        Speciality,
        related_name="doctors",
    )

class Patient(User):
    national_id = models.CharField(max_length=8,unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=true)
    updated_at = models.DateTimeField(auto_now=true)

    
    
    