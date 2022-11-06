from django.core.management.base import BaseCommand, no_translations
from budgets.models import BudgetItemCategory
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        current_categories = BudgetItemCategory.objects.all()
        if len(current_categories) == 0:
            categories = ["Home", "Auto", "Food", "Utilities", "Entertainment", "Health", "Transportation", "Other"]
            for category in categories:
                BudgetItemCategory.objects.create(name=category)
            print('Created %s categories' % len(categories))
        else:
            print("Categories already exist")
