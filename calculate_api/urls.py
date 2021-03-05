from django.urls import path
from . import views

app_name = 'calculate_api'

urlpatterns = [
    path('calculate', views.Calculator.as_view(), name='calculate_url'),
]