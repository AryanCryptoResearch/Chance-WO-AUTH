from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# django.contrib.auth import get_user_model 
#User = get_user_model()

# Create your models here.

class Params(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE ,  default=1)
    Reason = models.CharField(max_length=200)
    Gender = models.IntegerField()
    Age = models.IntegerField()
    Education = models.IntegerField()
    JobAndActivity = models.CharField(max_length=200)
    Financial = models.IntegerField()
    Asset = models.IntegerField()
    Mariage = models.IntegerField()
    Travels = models.IntegerField()
    SibingsInCA = models.BinaryField()
    RejectionHistory = models.BinaryField()


#class User(AbstractUser) : 
#pass