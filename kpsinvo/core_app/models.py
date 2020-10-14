from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images/")
    barcode_kps = models.CharField(max_length=30)
    barcode_manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return self.name