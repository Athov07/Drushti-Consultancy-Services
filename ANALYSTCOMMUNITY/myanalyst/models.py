from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()
# Create your models here.

class Analyst(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,blank=True, null=True)


class JobPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    amountLow = models.IntegerField(default=0)
    amountHigh = models.IntegerField(default=0)
    applycount = models.IntegerField(default=0)
    lastDateToApply = models.DateField()

    def __str__(self):
        return str(self.title)
    

STATUS_CHOICE = (
    ('pandding','pandding'),
    ('selected','selected')
)

class CandidateApplications(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    plan = models.OneToOneField(to=JobPost, on_delete=models.CASCADE)
    duration  = models.IntegerField()
    yearOfExt = models.IntegerField()
    dataset = models.FileField(upload_to='media')
    status = models.CharField(choices=STATUS_CHOICE, max_length=200, default='pandding')


class SelectCandidateJob(models.Model):
    id = models.AutoField(primary_key=True)
    plan = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)
    candidate = models.OneToOneField(to=CandidateApplications, on_delete=models.CASCADE)