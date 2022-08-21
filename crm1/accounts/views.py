from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
# from django.http import HttpResponse
from .models import Customer, Product, Order, Tag
from .forms import OrderCreateForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, admin_only, allowed_users
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        username = form.cleaned_data.get('username')
        messages.success(request, 'Account created for' + username)
        return redirect('/accounts/login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts-dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    # return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html', context=context)


def logoutUser(request):
    logout(request)
    return redirect('accounts-login-user')


@login_required(login_url='accounts-login-user')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = Order.objects.all().count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context=context)


@login_required(login_url='accounts-login-user')
def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='accounts-login-user')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'accounts/products.html', context=context)


@login_required(login_url='accounts-login-user')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
       'customer': customer,
       'orders': orders,
       'order_count': order_count,
       'order_filter': order_filter
    }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='accounts-login-user')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/accounts')

    context = {'form': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='accounts-login-user')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderCreateForm(instance=order)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderCreateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/accounts')

    context = {'form': form}
    # context = {}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='accounts-login-user')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/accounts')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)

