from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):

    choices = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]

    owner = models.ForeignKey(
        User, related_name='transactions',
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
