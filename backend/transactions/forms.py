from xml.dom.pulldom import START_DOCUMENT
from django import forms
from django.core.validators import MinValueValidator
from budgets.models import BudgetItem
from accounts.models import Account
from transactions.models import Transaction
import datetime

class NewTransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.SelectDateWidget(), initial=datetime.date.today)
    amount = forms.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = forms.CharField(max_length=255, required=False)
    account_id = forms.ModelChoiceField(queryset=Account.objects.all())
    budget_item_id = forms.ModelChoiceField(queryset=BudgetItem.objects.all(), required=False)
    type = forms.ChoiceField(choices=[('income', 'Income'), ('expense', 'Expense')])

    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'description', 'account_id', 'budget_item_id', 'type']

    def clean(self):
        cleaned_data = super().clean()
