from django.db import models
from customer.models import Customer

class ShopCard(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=100)

    def __str__(self):
        return f"ShopCard #{self.id}"