from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class MyAppUser (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)