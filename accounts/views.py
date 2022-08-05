import datetime
from tabnanny import check
from unicodedata import decimal
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewAccountForm, NewInstitutionForm
from django.contrib import messages
from .models import Account, AccountCheckpoint


def createAccount(request):
    if request.method == "POST":
        form = NewAccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            account.user_id = request.user
            account.current_balance = account.starting_balance
            account.save()
            messages.success(request, "Account created successfully.")
            return redirect("users:profile")
        messages.error(request, "There was invalid information in your account form. Please review and try again.")
    else:
        form = NewAccountForm()
    return render(request=request, template_name='accounts/account_form.html', context={"form": form})


def createInstitution(request):
    if request.method == "POST":
        form = NewInstitutionForm(request.POST)
        if form.is_valid():
            institution = form.save()
            institution.save()
            messages.success(request, "Institution created successfully.")
            return redirect("users:profile")
        messages.error(request, "There was invalid information in your institution form. Please review and try again.")
    else:
        form = NewInstitutionForm()
    return render(request=request, template_name='accounts/institution_form.html', context={"form": form})


def updateBalance(request, account_id, balance):
    if request.method == "POST":
        checkpoint = AccountCheckpoint()
        account = get_object_or_404(Account, pk=account_id)
        if balance != account.current_balance:
            checkpoint.account_id = account
            if balance.startswith("$"):
                balance = balance[1:]
            checkpoint.old_balance = float(account.current_balance)
            checkpoint.new_balance = float(balance)
            checkpoint.delta = checkpoint.new_balance - checkpoint.old_balance
            account.current_balance = checkpoint.new_balance
            account.save()
            checkpoint.save()
            messages.success(request, "Balance updated successfully.")
    return redirect("users:profile")


def showAccountHistory(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    checkpoints = AccountCheckpoint.objects.filter(account_id=account_id)
    return render(request=request, template_name='accounts/account_history.html', context={"account": account, "checkpoints": checkpoints})
