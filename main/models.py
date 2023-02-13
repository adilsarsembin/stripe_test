from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name
