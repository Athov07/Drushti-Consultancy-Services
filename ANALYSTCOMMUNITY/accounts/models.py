from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username=None
    phone_number=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=50)
    user_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_profile_image=models.ImageField(upload_to="profile")
    user_email=models.EmailField(max_length=100)
    user_post=models.CharField(max_length=100)
    user_designation=models.CharField(max_length=100)
    user_bio=models.CharField(max_length=100)
    

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()













    