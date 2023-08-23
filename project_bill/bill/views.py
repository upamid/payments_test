from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import (permissions, status, views,
                            viewsets)

from .models import Account, Balance, Bill, Bill_det,Bill_adj, Payment, Period, Service
from .forms import BillForm, ServiceForm
from .serializers import BalanceCreateSerializer, BalanceSerializer, BillSerializer, Bill_adjSerializer,PaymentSerializer, ServiceSerializer


def index(request):
    form = BillForm()
    return render(request, 'index.html', {'formChoice': form})

def ajax_bill(request):
    biil_obj = Bill.objects.get(account_id=request.POST.get('account_id'),
                                 period_id=request.POST.get('period_id'))
    #obj = list(Bill_det.objects.filter(bill_id=biil_obj.id).values())
    obj = BillSerializer(biil_obj).data
    print(obj)
    return JsonResponse({'data':obj, 'bill_id':biil_obj.id})


def ajax_services(request):
    services = Service.objects.all()
    obj = ServiceSerializer(services, many=True).data

    return JsonResponse({'data':obj})

def ajax_bill_adj(request):
    data = request.POST.copy()  
    print(data)      
    serializer = Bill_adjSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse(serializer.data, status=201)

def ajax_bill_adj_delete(request):
    Bill_adj.objects.filter(id=request.POST.get('id')).delete()
    return JsonResponse({'response':'Удалено'},status=200)

def balance(request):
    data = request.POST.copy()      
    account_id=request.POST.get('account_id'),
    bill_id=request.POST.get('bill_id') 
    Balance.objects.filter(account_id=account_id,
                           bill_id=bill_id
                           ).delete()
    serializer = BalanceCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    balance_obj = Balance.objects.filter(
        account_id=account_id,
        bill_id=bill_id
        )
    balance_data = BalanceSerializer(balance_obj, many=True).data
    biil_obj = Bill.objects.get(id=bill_id)
    bill_data = BillSerializer(biil_obj).data
    #return JsonResponse({'data':balance_data, 'bill':bill_data}, status=201)
    return render(request, 'report.html',{'data':balance_data, 'bill':bill_data})


def bill(request):
    if request.method == 'POST':
        biil_obj = Bill.objects.get(account_id=request.POST.get('account_id'), period_id=request.POST.get('period_id'))
        obj = BillSerializer(biil_obj).data
        payments_obj = Payment.objects.filter(account_id=request.POST.get('account_id'), period_id=request.POST.get('period_id'))
        payments = PaymentSerializer(payments_obj, many=True).data
        print(payments)
        services = Service.objects.all()
        services_data = ServiceSerializer(services, many=True).data
        return render(request, 'bill.html',{'data':obj, 'bill_id':biil_obj.id, 'services':services_data, 'payments':payments})
    #'account':account,'period':period,
    #account = Account.objects.get(id=request.POST.get('account_id'))
    #period = Period.objects.get(id=request.POST.get('period_id'))
