
from django.contrib import admin
from django.urls import path, include
from home_app.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Ruta para la página de inicio
    path('motivations/', include('motivation_app.urls')),
    path('learning_path/', include('learning_path_app.urls')),
    path('goals/', include('goals_app.urls')),
]
