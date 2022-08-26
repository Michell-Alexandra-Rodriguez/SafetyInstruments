from django.contrib import admin
from .models import IdentificationType, Profile, Client


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "identification_type", "identification_number")
    search_fields = ["identification_number", "email"]


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "rol")
    search_fields = ["user_name"]
    list_filter = ["rol"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "people")
    search_fields = ["people"]
    admin.site.site_header = 'Safety Instruments'
    admin.site.index_title = 'Manage your products'


admin.site.register(IdentificationType)
admin.site.register(Profile)
admin.site.register(Client, ClientAdmin)
