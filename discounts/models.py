from django.db import models
from django.conf import settings
from products.models import Product

class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.percentage}% discount on {self.product.name}"
