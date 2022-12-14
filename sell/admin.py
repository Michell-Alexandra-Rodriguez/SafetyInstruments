from django.contrib import admin

from .models import PaymentType, Sell


class SellAdmin(admin.ModelAdmin):
    list_display = ("product", "date_sell", "payment_type", "user")
    search_fields = ["product__name"]
    list_filter = ["date_sell","user","payment_type"]


admin.site.register(PaymentType)
admin.site.register(Sell, SellAdmin)
