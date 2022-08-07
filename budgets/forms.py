from xml.dom.pulldom import START_DOCUMENT
from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .models import Budget
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
