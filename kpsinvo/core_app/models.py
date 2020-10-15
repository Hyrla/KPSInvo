from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images/", blank=True)
    barcode_kps = models.CharField(max_length=30, blank=True)
    barcode_manufacturer = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images/", blank=True)
    barcode_manufacturer = models.CharField(max_length=50, blank=True)
    price = models.FloatField(default=1)  # En euros
    price_cotisant = models.FloatField(default=0.9)  # En euros

    def __str__(self):
        return self.name


class FoodStock(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.food.name


class FoodSale(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    is_cotisant = models.BooleanField(default=False)
