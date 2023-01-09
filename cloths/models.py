from django.db import models

# Create your models here.
class Cloth(models.Model):
    colour=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    dop=models.DateField()
    email=models.EmailField()
    quantity=models.IntegerField()
    gender=models.BooleanField()