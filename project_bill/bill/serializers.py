from rest_framework import serializers
from .models import (Account, Balance, Bill, Bill_det,
                     Bill_adj, Payment, Period, Service)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'month']


class Bill_detSerializer(serializers.ModelSerializer):
    service_id = ServiceSerializer(read_only=True)

    class Meta:
        model = Bill_det
        fields = ['service_id', 'value']


class PaymentSerializer(serializers.ModelSerializer):
    period_id = PeriodSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'account_id', 'period_id', 'value']


class Bill_adjSerializer(serializers.ModelSerializer):
    service_name = serializers.ReadOnlyField(source='service_id.name')

    class Meta:
        model = Bill_adj
        fields = ['id', 'account_id', 'bill_id',
                  'service_id', 'service_name', 'value']


class BillSerializer(serializers.ModelSerializer):
    account_id = AccountSerializer()
    period_id = PeriodSerializer()
    bill_dets = Bill_detSerializer(many=True)
    bill_adj = Bill_adjSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['id', 'account_id', 'period_id', 'bill_dets', 'bill_adj']


class BalanceSerializer(serializers.ModelSerializer):
    service_id = ServiceSerializer(read_only=True)

    class Meta:
        model = Balance
        fields = ['id', 'service_id', 'value']


class BalanceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = ['id', 'account_id', 'bill_id']

    def create(self, validated_data):
        account_id = validated_data.pop('account_id')
        bill_id = validated_data.pop('bill_id')
        bill_dets = Bill_det.objects.filter(bill_id=bill_id)
        service_debt = {}
        for bill_det in bill_dets:
            service_debt[bill_det.service_id] = bill_det.value
        bill_adjes = Bill_adj.objects.filter(
            account_id=account_id, bill_id=bill_id)
        for bill_adj in bill_adjes:
            if bill_adj.service_id in service_debt.keys():
                service_debt[bill_adj.service_id] += bill_adj.value
            else:
                service_debt[bill_adj.service_id] = bill_adj.value
        service_sum = sum(service_debt.values())
        payments = Payment.objects.filter(
            account_id=account_id, period_id=bill_id.period_id)
        payment_sum = sum(payment.value for payment in payments)
        ratio = {key: val / service_sum for key, val in service_debt.items()}
        srv_paid = {key: round(payment_sum*val, 2)
                    for key, val in ratio.items()}
        return [Balance.objects.create(
                account_id=account_id,
                bill_id=bill_id,
                service_id=key,
                value=val
                )
                for key, val in srv_paid.items()]
