from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyAppUser (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)