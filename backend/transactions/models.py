from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from budgets.models import BudgetItem

# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=200)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_ids')
    budget_item_id = models.ForeignKey(BudgetItem, on_delete=models.CASCADE, related_name='transaction_ids', null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
