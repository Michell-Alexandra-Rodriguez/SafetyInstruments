from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from inventary.models import Product
from user.models import User, Client
from .models import Sell, PaymentType

my_list = [i for i in range(1, 11)]
result = list(map(lambda current_number: current_number ** 2, my_list))
print(result)


@login_required
def sell_form(request):
    if request.method == 'POST':
        try:
            client = Client.objects.get(email=request.POST["current_client"])
            product = Product.objects.get(name=request.POST["current_product"])
            payment_type = PaymentType.objects.get(name=request.POST["current_payment_type"])
            user = User.objects.get(username=request.POST["current_user"])
            quantity = request.POST["quantity"]
        except:
            return HttpResponse(f"Complete the information in order to continue with the purchase")
        else:
            if (not str(quantity).isnumeric()) or int(quantity) > int(product.quantity):
                return HttpResponse(f"Sorry, we do not have all those products")
            new_sell = Sell(client=client, product=product, payment_type=payment_type, user=user, quantity=quantity)
            new_sell.save()
            product.quantity = (int(product.quantity) - int(quantity))
            product.save(update_fields=["quantity"])
            return redirect("../../admin/inventary/product/")

    client_list = Client.objects.all()
    client_name_list = list(map(lambda current_client: current_client.email, client_list))

    product_list = Product.objects.all()
    product_name_list = list(map(lambda current_product: current_product.name, product_list))

    payment_type_list = PaymentType.objects.all()
    payment_type_name_list = list(map(lambda current_payment_type: current_payment_type.name, payment_type_list))

    user_list = User.objects.all()
    user_name_list = list(map(lambda current_user: current_user.username, user_list))
    return render(request, 'sell/form_of_selling.html', {
        "all_clients": client_name_list,
        "all_products": product_name_list,
        "all_payment_types": payment_type_name_list,
        "all_users": user_name_list
    })
