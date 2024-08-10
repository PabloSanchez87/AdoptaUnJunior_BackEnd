from django.shortcuts import render
from .models import Motivation

def motivation_list(request):
    motivations = Motivation.objects.all()
    return render(request, 'motivation_list.html', {'motivations': motivations})
