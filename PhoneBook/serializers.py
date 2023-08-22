from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","phone_num","email","password"]
        
class ContactSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Contact
        fields = ["phone_num"]     
      
class SpamSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Spam
        fields = ["phone_num","spam_score"]
        


