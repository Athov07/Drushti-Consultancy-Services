from django.db import models


# Create your models here.
class ServicesPlans(models.Model):
    Suggestion_title=models.CharField(max_length=50)
    Plan_title=models.CharField(max_length=50)
    Plan_amount=models.FloatField()
    Plan_highlight1=models.CharField(max_length=50)
    Plan_highlight2=models.CharField(max_length=50)
    Plan_highlight3=models.CharField(max_length=50)
    Plan_highlight4=models.CharField(max_length=50)
    Plan_highlight5=models.CharField(max_length=50)
    Plan_btn=models.CharField(max_length=50)

class PlanDescription(models.Model):    
    Plan_des_title=models.CharField(max_length=50)
    Plan_Condition1=models.TextField()
    Plan_Condition2=models.TextField()
    Plan_Condition3=models.TextField()
    Plan_Condition4=models.TextField()
    Plan_Condition5=models.TextField()




