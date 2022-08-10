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
    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today)

    
    class Meta:
        model = Budget
        fields = ['name', 'description', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if Budget.objects.filter(name=name, start_date=start_date, end_date=end_date).exists():
            raise ValidationError('Budget already exists.')


class NewBudgetItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    account_id = forms.ModelChoiceField(queryset=Account.objects.all())
    category_id = forms.ModelChoiceField(queryset=BudgetItemCategory.objects.all())
    budget_amount = forms.DecimalField(max_digits=20, decimal_places=2)
    actual_amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = BudgetItem
        fields = ['name', 'account_id', 'category_id', 'budget_amount', 'actual_amount']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        account_id = cleaned_data.get('account_id')
        category_id = cleaned_data.get('category_id')
        budget_amount = cleaned_data.get('budget_amount')
        if BudgetItem.objects.filter(name=name, account_id=account_id, category_id=category_id, budget_amount=budget_amount).exists():
            raise ValidationError('Budget item already exists.')