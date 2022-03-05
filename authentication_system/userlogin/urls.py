from django.contrib import admin
from django.urls import path,include
from userlogin.views import *

urlpatterns = [
    path('', login, name='login'),
    
]
