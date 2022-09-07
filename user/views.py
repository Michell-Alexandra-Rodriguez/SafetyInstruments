from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_member(user):
                return redirect('sell_url')
            else:
                return redirect('../../admin/')
        else:
            return render(request, "user/login.html", {'error': 'invalid username or password'})

    return render(request, 'user/login.html')


@login_required
def log_out(request):
    logout(request)
    print("log out was done perfectly")
    return render(request, 'user/login.html')


def is_member(user):
    return user.groups.filter(name='Sells').exists()
