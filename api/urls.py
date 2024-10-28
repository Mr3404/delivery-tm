from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.auth.views import *



urlpatterns = [
        path("register/", Register.as_view(), name="register"),
        path("login/", TokenObtainPairView.as_view(), name="login"),

    ]
