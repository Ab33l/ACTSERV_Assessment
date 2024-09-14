"""
URL configuration for investment_management_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from investment_accounts.views import InvestmentAccountViewSet, CustomerInvestmentAccountViewSet, TransactionViewSet
from investment_accounts.admin_views import AdminViewSet

# Registration of the four viewsets (AdminViewSet, TransactionViewSet, InvestmentAccountViewSet, CustomerInvestmentAccountViewSet) and set up of the routing URLs to be used to access the respective resources
router = DefaultRouter()
router.register(r'admin', AdminViewSet, basename='admin')
router.register(r'transactions', TransactionViewSet)
router.register(r'investment-accounts', InvestmentAccountViewSet)
router.register(r'customer-investment-accounts', CustomerInvestmentAccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('investment/', include(router.urls)),
]