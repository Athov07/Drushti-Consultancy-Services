from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(default='John Doe (Default)', max_length=100, null=True)
    user_designation=models.CharField(default='This is the default , title change it in profile', max_length=200)
    desc_text='Hey, there is the default text descripthin about you that you can change on after clicking on "Edit" '
    user_bio=models.CharField(default=desc_text, max_length=200, null=True)
    user_profile_image=models.ImageField(default='images/default.jpg',upload_to='images',null=True,blank=True)


    def __str__(self):
        return self.user.phone_number
    

    
