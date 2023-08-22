from django.urls import path
from PhoneBook.views import *

urlpatterns = [
    
    path('register/',registerUser.as_view(),name='register'),
    path('spam/',MarkSpam.as_view(),name='spam'),
    path('namesearch/',SearchByName.as_view(),name='name'),
    path('phonesearch/',PhoneNumberDetails.as_view(),name='search-phone'),
    
]