from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from lock import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signedin", views.signedin, name="signedin"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("signedup", views.signedup, name="signednup")
]