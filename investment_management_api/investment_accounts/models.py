from django.db import models
from django.contrib.auth.models import AbstractUser

# Creation of the Customer model with importation of built-in authentication
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

# Records investment account details and the investment account owner
class InvestmentAccount(models.Model):
    investment_account_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='UserInvestmentAccount')

# Outlines and manages the relationship and permissions between the customer and their investment account
class UserInvestmentAccount(models.Model):
    VIEW_ONLY = 'view'
    CRUD = 'crud'
    POST_ONLY = 'post'
    PERMISSION_CHOICES = [
        (VIEW_ONLY, 'View Only'),
        (CRUD, 'CRUD'),
        (POST_ONLY, 'Post Only'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

# Records customers transactional details on investment account(s)
class Transaction(models.Model):
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
