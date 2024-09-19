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
            # Check if the user has permission to create a transaction
            account_id = self.request.data.get('investment_account')
            permission = UserInvestmentAccount.objects.filter(
                user=self.request.user,
                investment_account_id=account_id
            ).first()

            if permission and permission.permission == 'crud':
                return [permissions.IsAuthenticated()]
            else:
                return [permissions.IsAdminUser()]
        elif self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        user = self.request.user
        account_id = self.request.data.get('investment_account')
        permission = UserInvestmentAccount.objects.filter(user=user, investment_account_id=account_id).first()

        if permission and permission.permission == 'crud':
            serializer.save(user=user)
        else:
            self.permission_denied(self.request, message="You do not have permission to perform this action.")
