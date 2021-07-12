from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('book_lesson/<item_id>/', views.book_lesson, name='book_lesson'),
    path('remove_lesson/<item_id>/', views.remove_lesson,
         name='remove_lesson'),
]
