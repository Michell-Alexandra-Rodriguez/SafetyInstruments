from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inventary.models import Product


@login_required
def index(request):
    products = Product.objects.all()
    return render(request, "feed.html", {
        "all_products": products
    })
