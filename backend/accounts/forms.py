from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .models import Institution, Account
import datetime


class NewAccountForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    institution_id = forms.ModelChoiceField(queryset=Institution.objects.all())
    starting_balance = forms.DecimalField(max_digits=20, decimal_places=2)
    
    class Meta:
        model = Account
        fields = ['name', 'institution_id', 'starting_balance']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        institution_id = cleaned_data.get('institution_id')
        balance = cleaned_data.get('starting_balance')
        if Account.objects.filter(name=name, institution_id=institution_id).exists():
            raise ValidationError('Account already exists.')


class NewInstitutionForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = Institution
        fields = ['name']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if Institution.objects.filter(name=name).exists():
            raise ValidationError('Institution already exists.')
