from django.shortcuts import render
from django.contrib import messages
from budgets.forms import NewBudgetForm, NewBudgetItemForm
from budgets.models import Budget, BudgetItem
from accounts.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def createBudget(request):
    if request.method == "POST":
        form = NewBudgetForm(request.POST)
        if form.is_valid():
            budget = form.save()
            budget.user_id = request.user
            budget.save()
            messages.success(request, "Budget created successfully.")
            return redirect("users:profile")
        messages.error(request, "There was invalid information in your budget form. Please review and try again.")
    else:
        form = NewBudgetForm()
    return render(request=request, template_name="budgets/budget_form.html", context={"form": form})


def viewBudget(request, pk):
    if request.method == "POST":
        form = NewBudgetItemForm(request.POST)
        if form.is_valid():
            budgetItem = form.save()
            budgetItem.budget_id = get_object_or_404(Budget, pk=pk)
            budgetItem.save()
            messages.success(request, "Budget item created successfully.")
            return redirect("budgets:view", pk=pk)
        messages.error(request, "There was invalid information in your budget item form. Please review and try again.")
    else:
        budget = get_object_or_404(Budget, pk=pk)
        budget_items = BudgetItem.objects.filter(budget_id=pk)
        add_item_form = NewBudgetItemForm()
        add_item_form.fields['account_id'].queryset = Account.objects.filter(user_id=request.user)
        return render(request, "budgets/budget_detail.html", {"budget": budget, "budget_items": budget_items, "add_item_form": add_item_form})


def deleteBudgetItem(request, pk):
    budgetItem = get_object_or_404(BudgetItem, pk=pk)
    if budgetItem:
        budget = budgetItem.budget_id
        budget.expected_amount -= budgetItem.budget_amount
        budget.actual_amount -= budgetItem.actual_amount
        budget.delta -= budgetItem.delta
        budget.save()
        budgetItem.delete()
        messages.success(request, "Budget item deleted successfully.")
        return redirect("budgets:view", pk=budgetItem.budget_id.pk)
