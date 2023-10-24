from django.db import models
from shopcard.models import ShopCard
from product.models import Product

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopcard = models.ForeignKey(ShopCard, on_delete=models.CASCADE)
    sell_date = models.DateField()

    def __str__(self):
        return f"Item {self.id}"
