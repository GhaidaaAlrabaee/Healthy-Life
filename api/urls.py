# myproject/urls.py

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('bmi/', views.bmi_calculator, name='bmi'),
    path('calories/', views.calories_calculator, name='calories'),
    path('food-calculator/', views.food_calculator, name='food_calculator'),
    path('meals/', views.food_meals, name='meals'),
    path('signup/', views.signup_view, name='signup'),
    path('more_info/', views.info_view, name='more_info')
]

