from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
        full_name = models.CharField(max_length=100)
        phone = models.CharField(max_length=20)
        address = models.TextField()
        city = models.CharField(max_length=100)
        product_name = models.CharField(max_length=100)
        product_price = models.DecimalField(max_digits=6, decimal_places=2)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.full_name} - {self.product_name}"
