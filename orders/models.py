from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):

    # Available order status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    # Customer who placed the order
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Selected product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Number of items ordered
    quantity = models.PositiveIntegerField(default=1)

    # Current order status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    # Order creation date and time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"