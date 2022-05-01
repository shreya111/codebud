from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('problem/<str:pk>/', views.problem_detail, name="problem_detail"),
    path('problem/<str:py>/submitproblem/', views.submit_Problem, name="submit_Problem"),
    path('topics/', views.topicsPage, name="topics"),  
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
  
]