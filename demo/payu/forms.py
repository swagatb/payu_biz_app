from django import forms
from cart.utils import generate_hash

class OrderForm(forms.Form):
    # cart order related fields
    txnid = forms.CharField()
    productinfo = forms.CharField()
    amount = forms.DecimalField(decimal_places=2)

    # buyer details
    firstname = forms.CharField()
    lastname = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.RegexField(regex=r'\d{10}', min_length=10, max_length=10)
    address1 = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    zipcode = forms.RegexField(regex=r'\d{6}', min_length=6, max_length=6, required=False)


class PayUForm(forms.Form):
    # payu specific fields
    key = forms.CharField()

    # cart order related fields
    txnid = forms.CharField()
    productinfo = forms.CharField()
    amount = forms.DecimalField(decimal_places=2)

    # buyer details
    firstname = forms.CharField()
    lastname = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.RegexField(regex=r'\d{10}', min_length=10, max_length=10)
    address1 = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    zipcode = forms.RegexField(regex=r'\d{6}', min_length=6, max_length=6, required=False)
    
    # merchant's side related fields
    furl = forms.URLField()
    surl = forms.URLField()
    curl = forms.URLField(required=False)
    codurl = forms.URLField(required=False)
    touturl = forms.URLField(required=False)
    udf1 = forms.CharField(required=False)
    udf2 = forms.CharField(required=False)
    udf3 = forms.CharField(required=False)
    udf4 = forms.CharField(required=False)
    udf5 = forms.CharField(required=False)
    pg = forms.CharField(required=False)
    drop_category = forms.CharField(required=False)
    custom_note = forms.CharField(required=False)
    note_category = forms.CharField(required=False)


class HashForm(forms.Form):
    hash = forms.CharField(required = False)
