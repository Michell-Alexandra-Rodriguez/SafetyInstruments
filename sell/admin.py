from django.contrib import admin

from django.contrib import admin
from .models import PaymentType, Sell


class SellAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "date_sell", "payment_type", "user")
    search_fields = ["product"]
    list_filter = ["date_sell"]


admin.site.register(PaymentType)
admin.site.register(Sell, SellAdmin)
