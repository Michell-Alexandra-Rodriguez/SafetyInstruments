from django.urls import path
from . import views

urlpatterns = [
    path("products_list/", views.index, name="products_list_url")
]
