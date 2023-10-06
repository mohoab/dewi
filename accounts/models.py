from django.db import models
from django.contrib.auth.models import AbstractUser , User


class Customeuser(AbstractUser):
    mobile = models.CharField(max_length=20 , unique=True)
    userimg=models.ImageField(upload_to='image/user',default='image/default/defaultuser.png')
    email =  models.EmailField(unique=True)

# Create your models here.
