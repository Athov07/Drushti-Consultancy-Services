from django.db import models

# Create your models here.
class userFeedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    satisfied=models.CharField(max_length=50)
    rnumber=models.IntegerField(null=True)
    feed_message=models.TextField()
    def __str__(self):
        return str(self.rnumber)