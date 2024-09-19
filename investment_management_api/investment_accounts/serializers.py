from rest_framework import serializers
from .models import User, UserInvestmentAccount, InvestmentAccount, Transaction

# Serializer setup for the Customer model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'full_name', 'email_address']

# Serializer setup for the CustomerInvestmentAccount model
class UserInvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInvestmentAccount
        fields = ['user', 'investment_account', 'permission']

# Serializer setup for the InvestmentAccount model
class InvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentAccount
        fields = ['id', 'investment_account_name']

# Serializer setup for the Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'investment_account', 'user', 'amount', 'date']
