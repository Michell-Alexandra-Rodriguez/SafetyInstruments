from django.urls import path
from . import views

urlpatterns = [
    path("myindex/", views.index, name="index2")
]
