from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Cake', 'Cake'),
        ('Bread', 'Bread'),
        ('Pastry', 'Pastry'),
        ('Cookies', 'Cookies'),
        ('Beverage', 'Beverage'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name