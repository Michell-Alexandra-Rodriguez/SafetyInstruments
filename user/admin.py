from django.contrib import admin
from .models import IdentificationType, UserAdditionalInformation, Client


class UserAdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ("user", "cellphone",)
    search_fields = ["user", "cellphone"]


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "rol")
    search_fields = ["user_name"]
    list_filter = ["rol"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "identification_number")
    search_fields = ["name", "email", "identification_number"]
    admin.site.site_header = 'Safety Instruments'
    admin.site.index_title = 'Manage your products'


admin.site.register(IdentificationType)
admin.site.register(UserAdditionalInformation, UserAdditionalInformationAdmin)
admin.site.register(Client, ClientAdmin)
