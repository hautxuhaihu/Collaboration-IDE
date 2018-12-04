from django.db import models
from dashboard.models import Project

class Chat(models.Model):
    username = models.CharField(max_length=20)
    message = models.TextField()
    RefProject = models.ForeignKey(Project, on_delete=models.CASCADE)

class Source(models.Model):
    RefProject = models.ForeignKey(Project, on_delete=models.CASCADE)

class Directory(models.Model):
    Name = models.CharField(max_length=20)
    Parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    inSource = models.BooleanField()
    SourceFolder = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)

class File(models.Model):
    Name = models.CharField(max_length=20)
    Language = models.CharField(max_length=15)
    FirbaseID = models.CharField(max_length=20)
    Parent = models.ForeignKey(Directory, on_delete=models.CASCADE)
