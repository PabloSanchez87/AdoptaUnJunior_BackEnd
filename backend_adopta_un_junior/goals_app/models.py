from django.db import models

class Goal(models.Model):
    term = models.CharField(max_length=255)  # Ejemplo: "Corto plazo", "Mediano plazo", "Largo plazo"
    description = models.TextField()

    def __str__(self):
        return f"{self.term}: {self.description}"

class Task(models.Model):
    title = models.CharField(max_length=255)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pendiente'), ('In Progress', 'En progreso'), ('Completed', 'Completado')], default='Pending')

    def __str__(self):
        return self.title
