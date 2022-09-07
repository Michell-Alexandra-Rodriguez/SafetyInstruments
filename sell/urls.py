from django.urls import path
from . import views

urlpatterns = [
    path("product", views.sell_form, name="sell_url")
]
