from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

# django.contrib.auth import get_user_model
#User = get_user_model()

# Create your models here.

class Params(models.Model) : 
   # user = models.ForeignKey(User, on_delete=models.CASCADE ,  default=1)
    #Reason = models.CharField(max_length=200)
    Gender = models.IntegerField()
    Age = models.IntegerField()
    Education = models.IntegerField()
    JobAndActivity = models.CharField(max_length=200)
    Financial = models.IntegerField()
    Asset = models.IntegerField()
    #Mariage = models.IntegerField()
    Travels = models.IntegerField()
    #SibingsInCA = models.BinaryField()
    #RejectionHistory = models.BinaryField()

    SibingsInCA = models.IntegerField(default=0) #0 or 1 #0 = No #1 = YES
    RelationType =  models.IntegerField(default=0) 

    Marriage = models.IntegerField(default=0) # 0 or 1   #0 = No #1 = YES
    Children = models.IntegerField(default=0)  # 0 or 1    #0 = No #1 = YES
    Submittedwith = models.IntegerField(default=0) # 1:with spouse , 2:with Children , 3:children&spouse , 4:family , 5:siblings


    Reason = models.IntegerField(default=0) # from 1 to 5
    InvitedBy = models.IntegerField(default=0) # from 1 to 5 
    InvitationType = models.IntegerField(default=0) # 0:academic , 1:non-academic


    Financial = models.IntegerField(default=0) # 0 to 2k , 2k to 4k , .... 

    Education = models.IntegerField(default=0) # from 1 to 6
    
    
#class User(AbstractUser) : 
#pass