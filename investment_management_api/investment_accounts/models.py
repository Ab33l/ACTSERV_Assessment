from django.db import models
from django.contrib.auth.models import AbstractUser

# Creation of the Customer model with importation of built-in authentication
class Customer(AbstractUser):
    pass

# Outlines and manages the relationship and permissions between the customer and their investment account
class CustomerInvestmentAccount(models.Model):
    VIEW_ONLY = 'view'
    CRUD = 'crud'
    POST_ONLY = 'post'
    PERMISSION_CHOICES = [
        (VIEW_ONLY, 'View Only'),
        (CRUD, 'CRUD'),
        (POST_ONLY, 'Post Only'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

# Records investment account details and the investment account owner
class InvestmentAccount(models.Model):
    investment_account_name = models.CharField(max_length=255)
    customers = models.ManyToManyField(Customer, through='CustomerInvestmentAccount')

# Records customers transactional details on investment account(s)
class Transaction(models.Model):
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
