from django.contrib import admin
from django.urls import path, re_path
from bill import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('bill/', views.bill, name='bill'),
    path('ajax_bill/', views.ajax_bill, name='ajax_bill'),
    path('ajax_services/', views.ajax_services, name='ajax_services'),
    path('ajax_bill_adj/', views.ajax_bill_adj, name='ajax_bill_adj'),
    path('ajax_bill_adj_delete/', views.ajax_bill_adj_delete, name='ajax_bill_adj_delete'),
    path('balance/', views.balance, name='balance'),
]
