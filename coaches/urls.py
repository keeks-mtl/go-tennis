from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.view_coaches, name='view_coaches'),
    path('add/', views.add_coach, name='add_coach'),
    path('edit/<int:coach_id>', views.edit_coach, name='edit_coach'),
]