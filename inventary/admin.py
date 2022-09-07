from django.contrib import admin

from .models import Category, StateProduct, Supplier, Product


class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "cellphone", "identification_type", "identification_number", "address")
    search_fields = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price_by_unity", "quantity", "warranty", "date_arrival", "category", "supplier",
                    "state_product")
    search_fields = ["name"]
    list_filter = ["date_arrival", "state_product", "category"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(StateProduct)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
