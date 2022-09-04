from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import IdentificationType, UserAdditionalInformation, Client


class UserAdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ("user", "cellphone",)
    search_fields = ["user", "cellphone"]


class UserAdditionalInformationAdminInline(admin.StackedInline):
    model = UserAdditionalInformation
    can_delete = False
    verbose_name_plural = "Aditional Information"


class UserAdmin(BaseUserAdmin):
    inlines = (UserAdditionalInformationAdminInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "identification_number")
    search_fields = ["name", "email", "identification_number"]
    admin.site.site_header = 'Safety Instruments'
    admin.site.index_title = 'Manage your products'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(IdentificationType)
#admin.site.register(UserAdditionalInformation, UserAdditionalInformationAdmin)
admin.site.register(Client, ClientAdmin)
