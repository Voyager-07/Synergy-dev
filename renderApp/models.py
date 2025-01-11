from django.db import models

# Create your models here.
from django.db import models

# Model definition
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    age = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username