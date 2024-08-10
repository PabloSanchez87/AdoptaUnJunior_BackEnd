
from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goals_list, name='goals_list'),
    path('tasks/', views.tasks_list, name='tasks_list'),
]
