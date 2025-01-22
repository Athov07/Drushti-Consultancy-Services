from django.db import models

# Create your models here.
class userContact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact_message=models.TextField()

class My_Contact(models.Model):
    cont_title=models.CharField(max_length=20)
    cont_meg=models.CharField(max_length=500)
    my_location=models.CharField(max_length=50)
    location_des=models.CharField(max_length=50)
    my_phone=models.CharField(max_length=50)
    my_phone1=models.CharField(max_length=50)
    my_email=models.CharField(max_length=50)
    my_email1=models.CharField(max_length=50)
    cont_btn=models.CharField(max_length=20)
