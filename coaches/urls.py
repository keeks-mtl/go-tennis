from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_coaches, name='view_coaches'),
    path("<int:coach_id>/", views.view_coach, name="view_coach"),
    path('add/', views.add_coach, name='add_coach'),
    path('edit/<int:coach_id>/', views.edit_coach, name='edit_coach'),
    path('delete/<int:coach_id>/', views.delete_coach, name='delete_coach'),
]
