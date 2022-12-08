from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
    titre = models.CharField(max_length=20)
    auteur = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    prix = models.FloatField()

    def __str__(self) -> str:
        return self.name