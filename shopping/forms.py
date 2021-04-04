from django import forms
from shopping.models import Cart,Customer

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=('quantity',)

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','locality','city','zipcode','phone_number')
        