from rest_framework import viewsets, permissions
from .models import InvestmentAccount, UserInvestmentAccount, Transaction
from .serializers import InvestmentAccountSerializer, UserInvestmentAccountSerializer, TransactionSerializer

# Handles CRUD operations for InvestmentAccount based on its serializer class InvestmentAccountSerializer
class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()
    serializer_class = InvestmentAccountSerializer

# Handles CRUD operations for CustomerInvestmentAccount based on its serializer class CustomerInvestmentAccountSerializer
class UserInvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = UserInvestmentAccount.objects.all()
    serializer_class = UserInvestmentAccountSerializer

# Handles CRUD operations for Transaction based on its serializer class TransactionSerializer as well as handling additional permission requirements for authenticated users and admin roles
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]
