from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User, InvestmentAccount, UserInvestmentAccount, Transaction

class InvestmentAccountAPITestCase(APITestCase):

    def account_setup(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Abel', password='ActServ123')
        self.client.force_authenticate(user=self.user)

        self.admin_user = User.objects.create_superuser(username='Bob', password='ActServ321')
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_investment_account_creation(self):
        response = self.client.post('/api/investment-accounts/', {'investment_account_name': 'KES Money Market Fund'})
        self.assertEqual(response.status_code, 201)

    def test_transaction_initiation(self):
        self.account_setup()
        account = InvestmentAccount.objects.create(investment_account_name='KES_MMF_TopUp')
        UserInvestmentAccount.objects.create(user=self.user, investment_account=account, permission='crud')
        response = self.client.post('/api/transactions/', {'investment_account': account.id, 'user': self.user.id, 'amount': 12340.10})
        self.assertEqual(response.status_code, 201)

    def test_view_only_permission(self):
        """Test user with 'view' permission cannot post transactions"""
        self.account_setup()
        account = InvestmentAccount.objects.create(investment_account_name='USD_MMF_TopUp')
        UserInvestmentAccount.objects.create(user=self.user, investment_account=account, permission='view')
        response = self.client.post(reverse('transaction-list'), {'investment_account': account.id, 'amount': 268.06})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)