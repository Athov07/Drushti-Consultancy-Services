from django.db import models

# Create your models here.
from django.db import models
from myanalyst.models import CandidateApplications, JobPost
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.

class MyApplyList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    plan = models.ForeignKey(to=CandidateApplications, on_delete=models.CASCADE)
    dateYouApply = models.DateField(auto_now_add=True)

class IsSortList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    plan = models.OneToOneField(to=JobPost, on_delete=models.CASCADE)
    dateYouApply = models.DateField(auto_now_add=True)