from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from imsys.forms import UserForm, SalesOrder, SalesItem
from django.contrib.auth.models import User

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'imsys/dashboard.html', {'username': request.user.first_name})
    else:
        return redirect(request, 'imsys:home')


@login_required
def edit(request):
    if request.method == 'POST':
        typ = request.POST.get('type')
        if typ == 'passwords':
            print('in change password')
            person = authenticate(
                username=request.user.username, password=request.POST.get('password1'))
            if person is not None:
                print(request.POST.get('newpassword'))
                person.set_password(request.POST.get('newpassword'))
                person.save()
            else:
                print("Wrong Password")
        elif typ == 'profiles':
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.username = request.POST.get('username')
            request.user.email = request.POST.get('email')

    else:
        user = request.user
    return render(request, 'imsys/edit.html', {'username': request.user.first_name})


@login_required
def user_logout(request):
    logout(request)
    return redirect('imsys:home')


@login_required
def saledorder(request):
    if request.method == "POST":
        fore = request.POST
        salesorder = SalesOrder(data=fore)
        tempsalesorder = salesorder.save(commit=False)
        tempsalesorder.user = request.user 
        tempsalesorder.save()
        for i in range(int(fore.get('itemno'))):
            salesitem = SalesItem(data=fore)
            tempsalesitem = salesitem.save(commit=False)
            tempsalesitem.sales_order_no = tempsalesorder.sales_order_no
            tempsalesitem.save()
        return render(request, 'imsys/salesorder.html',{'username': request.user.first_name})
    elif request.method == "GET":
        return render(request, 'imsys/salesorder.html', {'username': request.user.first_name})


@login_required
def purchaseorder(request):
    return render(request, 'imsys/purchase order.html', {'username': request.user.first_name})


def user_login(request):
    if request.method == 'POST':
        u1 = request.POST.get('username')
        p1 = request.POST.get('password')
        name = request.POST.get('type')
        person = authenticate(username=u1, password=p1)
        if person is not None:
            login(request, person)
            return redirect('imsys:dashboard')
        else:
            return HttpResponse("Wrong Login id or password")
    else:
        return render(request, "imsys/index.html")


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('imsys:home')
        else:
            print(user_form.errors)
    else:
        return render(request, 'imsys/registration.html')

