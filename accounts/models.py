from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require


class Institution(models.Model):
    name = models.CharField(max_length=100)

    __str__ = lambda self: self.name


class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    institution_id = models.ForeignKey(Institution, on_delete=models.RESTRICT)
    starting_balance = models.DecimalField(max_digits=20, decimal_places=2)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class AccountCheckpoint(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="checkpoint_ids", null=True)
    old_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    new_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    delta = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    __str__ = lambda self: self.account_id.name + " - " + str(self.balance) + " - " + str(self.create_date)

    class Meta:
        ordering = ['create_date']