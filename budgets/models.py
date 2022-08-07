from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['end_date', 'start_date']


class BudgetItemCategory(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BudgetItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='budget_item_ids')
    budget_item_category_id = models.ForeignKey(BudgetItemCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    budget_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return self.name




    