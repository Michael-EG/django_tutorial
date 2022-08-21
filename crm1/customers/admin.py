from django.contrib import admin
from .models import PharmacyCustomer, Address, Receipt
# Register your models here.

admin.site.register(PharmacyCustomer)
admin.site.register(Address)
admin.site.register(Receipt)
