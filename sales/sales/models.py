from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Item(models.Model):
    name = models.CharField(max_length=10)
    info = models.TextField()


class Order(models.Model):
    date = models.DateTimeField(default=datetime.now())

    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Positions(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Seller(models.Model):
    STATUS_CHOICES = [
        ('s', 'salesman'),
        ('ss', 'senior salesman'),
        ('sv', 'supervisor'),
    ]
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField()
    date_hiring = models.DateField()
    position = models.CharField(max_length=2, choices=STATUS_CHOICES)


class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    data_of_sale = models.DateTimeField(default=datetime.now())

    total = models.IntegerField()
