from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)  # pone fecha y hora de creacion
    datecomplete = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)  # balores booleanos
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # esto mejora la vista desde el Admin
        return f"{self.title} - by - {self.user.username}"
