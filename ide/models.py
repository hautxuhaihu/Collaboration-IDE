from django.db import models
from dashboard.models import Project

class Chat(models.Model):
    username = models.CharField(max_length=20)
    message = models.TextField()
    RefProject = models.ForeignKey(Project, on_delete=models.CASCADE)

