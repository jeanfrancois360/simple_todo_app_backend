from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodos),
    path('add/', views.addTodo),
    path('<str:pk>/update/', views.updateTodo),
    path('<str:pk>/delete/', views.deleteTodo),
    path('<str:pk>/', views.getTodo),
]

