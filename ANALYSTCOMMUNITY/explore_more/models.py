from django.db import models

# Create your models here.

class explore_more(models.Model):
    exp_slid_img=models.FileField(upload_to='explore_more/', max_length=250 ,null=True,blank=True)

