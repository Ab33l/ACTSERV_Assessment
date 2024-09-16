from django.test import TestCase
from rest_framework.test import APIClient
from .models import Customer, InvestmentAccount, CustomerInvestmentAccount, Transaction

class InvestmentAccountTests(TestCase):
    def account_setup(self):
        self.client = APIClient()
        self.user = Customer.objects.create_user(username='Abel', password='ActServ123')
        self.client.login(username='Bob', password='ActServ321')

    def test_investment_account_creation(self):
        response = self.client.post('/investment/investment-accounts/', {'name': 'KES Money Market Fund'})
        self.assertEqual(response.status_code, 201)

    def test_transaction_initiation(self):
        account = InvestmentAccount.objects.create(name='KES_MMF_TopUp')
        CustomerInvestmentAccount.objects.create(user=self.user, investment_account=account, permission='crud')
        response = self.client.post('/investment/transactions/', {'investment_account': account.id, 'user': self.user.id, 'amount': 12340.10})
        self.assertEqual(response.status_code, 201)

