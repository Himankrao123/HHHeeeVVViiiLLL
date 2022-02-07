from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from lock import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter', views.enter, name='enter')
]