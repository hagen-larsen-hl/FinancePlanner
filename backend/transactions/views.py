from django.shortcuts import render, redirect
from django.contrib import messages
from transactions.forms import NewTransactionForm
from transactions.models import Transaction
from budgets.models import BudgetItem
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def createTransaction(request):
    if request.method == "POST":
        form = NewTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            transaction.user_id = request.user
            transaction.save()
            messages.success(request, "Transaction created successfully.")
            return redirect("users:profile")
        messages.error(request, "There was invalid information in your budget form. Please review and try again.")
    else:
        form = NewTransactionForm()
    return render(request=request, template_name="budgets/budget_form.html", context={"form": form})


def viewTransaction(request, pk):
    return JsonResponse(serializers.serialize('json', [Transaction.objects.get(pk=pk)]), safe=False)
