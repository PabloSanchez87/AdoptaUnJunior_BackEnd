from django.contrib import admin
from goals_app.models import Goal, Task

# Registra los modelos en el admin
admin.site.register(Goal)
admin.site.register(Task)
