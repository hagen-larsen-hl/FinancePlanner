from xml.dom.pulldom import START_DOCUMENT
from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from budgets.models import Budget, BudgetItem, BudgetItemCategory
from accounts.models import Account
import datetime


class NewBudgetForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255, required=False)
    start_date = forms.DateField(widget=forms.widgets.SelectDateWidget(), initial=datetime.date.today)
    end_date = forms.DateField(widget=forms.widgets.SelectDateWidget(), initial=datetime.date.today)

    
    class Meta:
        model = Budget
        fields = ['name', 'description', 'start_date', 'end_date']


class NewBudgetItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    account_id = forms.ModelChoiceField(queryset=Account.objects.all())
    category_id = forms.ModelChoiceField(queryset=BudgetItemCategory.objects.all())
    budget_amount = forms.DecimalField(max_digits=20, decimal_places=2)
    actual_amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = BudgetItem
        fields = ['name', 'account_id', 'category_id', 'budget_amount', 'actual_amount']
