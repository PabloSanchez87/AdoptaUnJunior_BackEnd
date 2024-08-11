from django.contrib import admin

from learning_path_app.models import LearningStep

# Registra el modelo en el admin
admin.site.register(LearningStep)