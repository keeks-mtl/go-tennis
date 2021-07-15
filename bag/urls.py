from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<item_id>/', views.edit_bag, name='edit_bag'),
    path('remove/<item_id>/', views.remove_product, name='remove_product'),
    path('book_lesson/<item_id>/', views.book_lesson, name='book_lesson'),
    path('remove_lesson/<item_id>/', views.remove_lesson,
         name='remove_lesson'),
]
