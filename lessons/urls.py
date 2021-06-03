from django.urls import path
from .import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('book/', views.all_lessons, name='all_lessons'),
]