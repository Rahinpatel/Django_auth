from django.contrib import admin
from django.urls import path,include
from api import api_views

urlpatterns = [
    path('user/', api_views.user_list())
    path('user/<int:pk>', api_views.userid)
]
