from django.db import models
from django.contrib.auth.models import User
# from ..accounts.models import Customer


class PharmacyCustomer(models.Model):
    # name_en = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    uid = models.IntegerField(unique=True, null=False, blank=False)
    mobile = models.CharField(max_length=14, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='user_created_pharmacy_customer', null=True, blank=True, on_delete=models.SET_NULL, default="")
    edited_at = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, related_name='user_edited_pharmacy_customer', null=True, blank=True, on_delete=models.SET_NULL, default="")

    def __str__(self):
        return self.name + '(UID: ' + self.uid + ')'


class Address(models.Model):
    customer_ref = models.ForeignKey(PharmacyCustomer, null=False, blank=False, on_delete=models.CASCADE)
    apartment_number = models.CharField(max_length=20, null=False, blank=False, default='')
    floor_number = models.CharField(max_length=20, null=False, blank=False, default='')
    building_number = models.CharField(max_length=20, null=False, blank=False, default='')
    street_name = models.CharField(max_length=200, null=False, blank=False)
    # street = models.ForeignKey(Street, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False, default='مرسى مطروح')
    country = models.CharField(max_length=50, null=False, blank=False, default='مصر')

    def __str__(self):
        return 'Address for ' + self.customer_ref.name + ' @ ' + self.street_name


class Receipt(models.Model):
    customer_ref = models.ForeignKey(PharmacyCustomer, null=False, blank=False, on_delete=models.CASCADE)
    external_receipt_reference = models.CharField(max_length=100, null=False, blank=False, default='')
    external_issue_date = models.DateTimeField()

    def __str__(self):
        return 'Receipt for ' + self.customer_ref.name + ' @ ' + self.external_issue_date

# class Street(models.Model):
#     arabic_name = models.CharField(max_length=200, null=False, blank=False)
#     english_name = models.CharField(max_length=200, null=False, blank=False)

