from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    FLAVOUR_CHOICES = [
        ('DRAGON_FRUIT_ICE', 'Dragon Fruit Ice'),
        ('BLUESOUR_RASPBERRY', 'Blue Sour Raspberry'),
        ('STRAWBERRY_KIWI', 'Strawberry Kiwi'),
        ('BLUEBERRY_ON_ICE', 'Blueberry on Ice'),
        ('MIXED_BERRIES', 'Mixed Berries'),
        ('DR_BLUE', 'Dr Blue'),
        ('LOVE_66', 'Love 66'),
        ('PINK_LEMONADE', 'Pink Lemonade'),
        ('BERRY_LEMONADE', 'Berry Lemonade'),
    ]
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    # flavour = models.CharField(max_length=50, choices=FLAVOUR_CHOICES)

    def __str__(self):
        return self.name

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
