from django.urls import path
from . import views

urlpatterns = [
    path('learning_path/', views.learning_path, name='learning_path'),
]
