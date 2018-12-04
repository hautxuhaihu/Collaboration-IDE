from django.db import models
from accounts.models import Contributor
from django.contrib.auth.models import User

class Project(models.Model):
    Title = models.CharField(max_length=50)
    Key = models.CharField(max_length=6)
    FirebaseID = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Created = models.DateField(auto_now=True)
    LastModified = models.DateField(auto_now=True)
    Developers = models.ManyToManyField(Contributor)
    Owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title