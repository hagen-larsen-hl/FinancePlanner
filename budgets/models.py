from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account


class Budget(models.Model):
    archived = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    delta = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['end_date', 'start_date']

    def save(self, *args, **kwargs):
        self.delta = self.expected_amount - self.actual_amount
        super(Budget, self).save(*args, **kwargs)


class BudgetItemCategory(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BudgetItem(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='budget_item_ids')
    budget_amount = models.DecimalField(max_digits=20, decimal_places=2)
    category_id = models.ForeignKey(BudgetItemCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='budget_item_ids', null=True)
    delta = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)

    description = models.TextField(null=True)
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)

    class Meta:
        ordering = ['account_id', 'category_id', 'budget_amount']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.delta = self.budget_amount - self.actual_amount
        if self.budget_id:
            self.budget_id.actual_amount += self.actual_amount
            self.budget_id.expected_amount += self.budget_amount
            self.budget_id.save()   
        super(BudgetItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.budget_id:
            self.budget_id.actual_amount -= self.actual_amount
            self.budget_id.expected_amount -= self.budget_amount
            self.budget_id.save()
        super(BudgetItem, self).delete(*args, **kwargs)





    