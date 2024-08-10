
from django.contrib import admin
from django.urls import path, include
from home_app.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Ruta para la página de inicio
    path('', include('motivation_app.urls')),
    path('', include('learning_path_app.urls')),
    path('', include('goals_app.urls')),
]
