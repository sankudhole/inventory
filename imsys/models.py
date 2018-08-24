from django.db import models
from django.contrib.auth.models import User

class user(User):
    class Meta:
        proxy = True

class SalesOrder(models.Model):
    user = models.ForeignKey('user',on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    sales_order_no = models.IntegerField(primary_key=True)
    sales_order_date = models.DateField()
    expected_Shipment = models.DateField()
    sales_person = models.CharField(max_length=100)
    delivery_method = models.CharField(max_length=50)
    sub_total = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    final_total = models.DecimalField(max_digits=5, decimal_places=2)
    attachedfile = models.FileField(blank=True)
    customer_note = models.TextField(max_length=500, blank=True)
    terms_and_conditions = models.TextField(max_length=500, blank=True)

class Sales_Item(models.Model):
    sales_order_no = models.ForeignKey('SalesOrder', on_delete=models.CASCADE)
    item_info = models.TextField(max_length=500)
    account_type = models.TextField(max_length=500)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=5,decimal_places=2)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwarg):
        self.amount = self.quantity * self.rate
        return super(Sales_Item,self).save(*args,**kwarg)

class Purchase_Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=200)
    organisation_type = models.CharField(max_length=100)
    purchase_order_no = models.IntegerField(primary_key=True)
    purchase_date = models.DateField()
    delivery_date = models.DateField()
    sub_total = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    final_total = models.DecimalField(max_digits=5, decimal_places=2)
    attachedfile = models.FileField(blank=True)
    customer_note = models.TextField(max_length=500)
    terms_and_conditions = models.TextField(max_length=500)

class Purchase_Item(models.Model):
    purchase_order_no =models.ForeignKey("Purchase_Order", on_delete=models.CASCADE)
    item_info = models.CharField(max_length=500)
    account_type = models.CharField(max_length=500)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount=models.DecimalField(max_digits=5, decimal_places=2)

