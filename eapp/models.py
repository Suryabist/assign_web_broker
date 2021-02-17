from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='media')
    category = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
