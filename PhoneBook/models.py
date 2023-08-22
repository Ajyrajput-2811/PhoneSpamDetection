import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=15,unique=True)
    email = models.EmailField(blank=True,max_length=254)
    password = models.CharField(max_length=50)
    
class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    phone_num = models.CharField(max_length=10)
   
class Spam(models.Model):
    phone_num = models.CharField(max_length=15) 
    spam_score = models.IntegerField()   
