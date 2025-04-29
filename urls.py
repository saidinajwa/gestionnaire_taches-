from django.urls import path
from . import views
from .models import Task

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('ajouter/', views.task_create, name='task_create'),
    path('modifier/<int:pk>/', views.task_update, name='task_update'),
    path('supprimer/<int:pk>/', views.task_delete, name='task_delete'),
]
