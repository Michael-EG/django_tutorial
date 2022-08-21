from django.shortcuts import render
from .decorators import admin_only
from .core.print_scripts import printx_load_printers
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts-login-user')
@admin_only
def printx_home(request):
    printers = printx_load_printers()
    # orders = Order.objects.all()
    # customers = Customer.objects.all()
    # total_customers = customers.count()
    # total_orders = Order.objects.all().count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()
    # context = {
    #     'orders': orders,
    #     'customers': customers,
    #     'total_customers': total_customers,
    #     'total_orders': total_orders,
    #     'delivered': delivered,
    #     'pending': pending
    # }
    context = {
        'printers': printers,
        'orders': [],
        'customers': [],
        'total_customers': [],
        'total_orders': [],
        'delivered': [],
        'pending': []
    }
    return render(request, 'printx/main_dashboard.html', context=context)

    # load devices
    # render devices

