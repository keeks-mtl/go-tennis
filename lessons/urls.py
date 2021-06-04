from django.urls import path
from .import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('book/', views.all_lessons, name='all_lessons'),
    path('add/', views.add_lesson, name='add_lesson'),
    path('edit/<int:lesson_id>', views.edit_lesson, name='edit_lesson'),
    path('delete/<int:lesson_id>', views.delete_lesson, name='delete_lesson'),
]
