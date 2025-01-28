from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

# Create your models here.
