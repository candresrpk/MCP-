from django.urls import path
from .views import home_view, create_transaction_view, transactions_view

app_name = 'mcp'


urlpatterns = [
    path('', home_view, name='home'),
    path('transactions/', transactions_view, name='transactions'),
    path('create/', create_transaction_view, name='create'),

]
