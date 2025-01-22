from django.db import models

# Create your models here.
class Analytics(models.Model):
    Analytics_icon=models.FileField(upload_to="drushti_services/",max_length=250,null=True,default=None)
    Analytics_title=models.CharField(max_length=100)
    Analytics_des=models.TextField()
    Analytics_btn=models.CharField(max_length=50)

def __str__(self):
    return self.service_title

# @property
# def imageURL(self):
#     try:
#         url=self.service_icon.url
#     except:
#         url=''
#     return url



class FAQ(models.Model):
    faq=models.TextField()
    faq_ans=models.TextField()

class ourClient(models.Model):
    image=models.FileField(upload_to='ourClient/', max_length=250 ,null=True,blank=True)

def __str__(self):
    return self.image