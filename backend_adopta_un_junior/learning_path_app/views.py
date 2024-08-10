from django.shortcuts import render
from .models import LearningStep

def learning_path(request):
    steps = LearningStep.objects.all()
    return render(request, 'learning_path.html', {'steps': steps})