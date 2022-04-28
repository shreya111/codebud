from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.login_register, name="login_register"),
]