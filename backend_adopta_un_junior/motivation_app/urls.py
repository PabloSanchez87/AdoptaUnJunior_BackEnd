from django.urls import path
from . import views

urlpatterns = [
    path('motivations/', views.motivation_list, name='motivation_list'),
]
