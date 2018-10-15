from django.contrib.auth.models import User
from django.db import models

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isOwner = models.BooleanField(default=False)
