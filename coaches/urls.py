from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.view_coaches, name='view_coaches'),
]