from django.db import models

# Create your models here.
class Electrica(models.Model):
    marca=models.CharField(max_length=70)
    modelo=models.CharField(max_length=70)
    
class Acustica(models.Model):
    marca=models.CharField(max_length=70)
    modelo=models.CharField(max_length=70)
    
class Amplificadore(models.Model):
    marca=models.CharField(max_length=70)
    modelo=models.CharField(max_length=70)

class Efecto(models.Model):
    marca=models.CharField(max_length=70)
    modelo=models.CharField(max_length=70)