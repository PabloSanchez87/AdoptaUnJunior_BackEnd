from django.db import models

class Motivation(models.Model):
    reason = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.reason
