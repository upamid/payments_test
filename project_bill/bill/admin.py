from django.contrib import admin
from .models import Account, Balance, Service, Period, Payment, Bill, Bill_det, Bill_adj


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ['id', "name"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ['id', "name"]


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    fields = ["month"]
    list_display = ['id', "month"]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = ["period_id"]
    list_display = ['id', "period_id"]

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    fields = ["account_id", "period_id"]
    list_display = ['id', "account_id", "period_id"]

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    fields = ["account_id", "bill_id"]
    list_display = ['id', "account_id", "bill_id", "service_id", "value"]

@admin.register(Bill_det)
class Bill_detdAdmin(admin.ModelAdmin):
    fields = ["bill_id", "service_id", "value"]
    list_display = ['id', "bill_id", "service_id", "value"]

@admin.register(Bill_adj)
class Bill_adjdAdmin(admin.ModelAdmin):
    fields = ["account_id", "bill_id", "value"]
    list_display = ['id', "bill_id", "service_id", "value"]