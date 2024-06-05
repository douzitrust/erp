from django.contrib import admin
from .models import SalesOrder, SalesOrderLineItem

admin.site.register(SalesOrder)
admin.site.register(SalesOrderLineItem)
