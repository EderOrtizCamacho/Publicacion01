from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    dni=models.IntegerField()
    distrito=models.CharField(max_length=30)

    