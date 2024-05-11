from django.db import models

class ProductModel(models.Model):
    Image = models.CharField(max_length=250)
    Name = models.CharField(max_length=100)
    Desc = models.CharField(max_length=250)
    Price = models.FloatField()
    Quantity = models.FloatField()
    class Meta():
        pass
    def __str__(self):
        return str(self.Name)