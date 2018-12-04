from django.contrib.auth.models import User
from django.db import models

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


