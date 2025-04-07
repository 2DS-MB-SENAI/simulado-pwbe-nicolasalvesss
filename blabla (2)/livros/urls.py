from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('api/', views.read_api),
]