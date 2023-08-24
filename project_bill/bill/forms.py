from django import forms

from .models import Account, Bill, Period, Service


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['account_id', 'period_id']


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name']
