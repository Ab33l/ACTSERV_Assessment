from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Transaction
from .serializers import TransactionSerializer

# Admin endpoint that returns all of a user's transactions, along with a nested sum of the user's total balance. Additionally, the endpoint includes a date range filter to retrieve transactions that occurred within a specified date range
class AdminViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='customer-transactions')
    def user_transactions(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        transactions = Transaction.objects.filter(user_id=user_id, date__range=[start_date, end_date])
        total_balance = transactions.aggregate(Sum('amount'))['amount__sum']

        serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': serializer.data, 'total_balance': total_balance})
