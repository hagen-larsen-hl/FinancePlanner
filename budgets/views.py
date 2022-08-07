from django.shortcuts import render
from django.contrib import messages
from budgets.forms import NewBudgetForm
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
