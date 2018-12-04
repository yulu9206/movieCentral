from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class TempUser(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.IntegerField()
    isActivate = models.BooleanField(default=False)