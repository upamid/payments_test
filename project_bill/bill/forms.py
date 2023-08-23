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

'''
class PeriodForm(forms.ModelForm):
    month = forms.ModelChoiceField(
        queryset=Period.objects.all().order_by('month'),
        label="Period",
        )
    
    class Meta:
        model = Period
        fields = ['month']



        account = forms.ModelChoiceField(
        queryset=Account.objects.all().order_by('name'),
        label="Account",
        )

    month = forms.ModelChoiceField(
        queryset=Period.objects.all().order_by('month'),
        label="Period",
        )
        '''