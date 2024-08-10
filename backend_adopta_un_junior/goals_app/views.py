from django.shortcuts import render
from .models import Goal, Task

def goals_list(request):
    goals = Goal.objects.all()
    return render(request, 'goals_list.html', {'goals': goals})

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})