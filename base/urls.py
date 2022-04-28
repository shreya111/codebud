from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('problem/<str:pk>/', views.problem_detail, name="problem_detail"),
    
    
]