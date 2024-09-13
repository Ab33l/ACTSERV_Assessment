from rest_framework import serializers
from .models import Customer, CustomerInvestmentAccount, InvestmentAccount, Transaction

# Serializer setup for the Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user_id', 'full_name', 'email_address', 'phone_number']

# Serializer setup for the CustomerInvestmentAccount model
class CustomerInvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInvestmentAccount
        fields = ['customer', 'investment_account', 'permission']

# Serializer setup for the InvestmentAccount model
class InvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentAccount
        fields = ['investment_account_id', 'investment_account_name']

# Serializer setup for the Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'investment_account', 'customer', 'amount', 'date']
