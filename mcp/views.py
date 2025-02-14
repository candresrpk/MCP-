from django.shortcuts import render
from .forms import TransactionForm
from .models import Transaction
# Create your views here.


def home_view(request):

    return render(request, 'mcp/home.html')


def transactions_view(request):

    transactions = Transaction.objects.filter(owner=request.user)

    context = {
        'transactions': transactions
    }

    return render(request, 'mcp/transactions.html', context)


def create_transaction_view(request):

    context = {
        'form': TransactionForm()
    }

    if request.method == 'GET':

        return render(request, 'mcp/create_transaction.html', context)

    else:

        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.owner = request.user
            if transaction.category == 'expense' and transaction.amount > 0:
                transaction.amount = transaction.amount * -1

            transaction.save()

            return render(request, 'mcp/create_transaction.html', context)

        else:
            context['message'] = 'something went wrong'
            context['form'] = form
            return render(request, 'mcp/create_transaction.html', context)
