from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #display es lo que queremos que se vea en la previu
    list_display = ['table', 'product', 'status', 'created_at']
 