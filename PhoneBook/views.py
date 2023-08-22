from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class registerUser(APIView):
    def post(self,request):
        data = request.data
        print(data)
        serializer  = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"Success","data":serializer.data},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        obj_data = User.objects.all()
        getSerializer = UserSerializer(obj_data,many = True)
        if getSerializer:
            return Response({"status":"Success",
                             "data":getSerializer.data},status = status.HTTP_200_OK)
        return Response({"message":"Oops! Not Found"},status = status.HTTP_404_NOT_FOUND)  
    
    
class MarkSpam(APIView):
    def post(self,request):
        serializer = SpamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"Success","data":serializer.data}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        obj_data = Spam.objects.all()
        getSerializer = SpamSerializer(obj_data,many = True)
        if getSerializer:
            return Response({"status":"Success",
                             "data":getSerializer.data},status = status.HTTP_200_OK)
        return Response({"message":"Oops! Not Found"},status = status.HTTP_404_NOT_FOUND) 

class SearchByName(APIView):
    def get(self,request):
        name = request.query_params.get("name")
        users_start_name = User.objects.filter(name__istartswith = name)
        users_contain_name = User.objects.filter(name__icontains=name).exclude(id__in=users_start_name)
        results = list(users_start_name) + list(users_contain_name)
        serializer = UserSerializer(results, many=True)
        return Response({"status":"Success","data":serializer.data}, status=status.HTTP_200_OK)

    
class PhoneNumberDetails(APIView):
    def get(self, request):
        phone_number = request.query_params.get("phone")
        try:
            user = User.objects.get(phone_num=phone_number)
            user_serializer = UserSerializer(user)
            
            try:
                spam_entry = Spam.objects.get(phone_num=phone_number)
                spam_serializer = SpamSerializer(spam_entry)
                return Response({
                    "status":"Success",
                    "user": user_serializer.data,
                    "spam": spam_serializer.data
                }, status=status.HTTP_200_OK)
            except Spam.DoesNotExist:
                return Response({
                    "status":"Success",
                    "user": user_serializer.data,
                    "spam": None
                }, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)   
        
    
        
          
        
    
