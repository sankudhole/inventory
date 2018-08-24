from django import forms
from django.contrib.auth.models import User
from imsys.models import SalesOrder,user, Sales_Item

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = user
        fields = ('username','email','password','first_name','last_name')

class SalesOrder(forms.ModelForm):

    class Meta():
        model = SalesOrder
        fields = ('customer_name','sales_order_no','sales_order_date','expected_Shipment',
            'sales_person','delivery_method','discount','attachedfile',
            'customer_note','terms_and_conditions','sub_total','final_total')

class SalesItem(forms.ModelForm):
    class Meta():
        model = Sales_Item
        fields = ('sales_order_no','item_info','account_type','quantity','rate','amount')
