from django import forms
from .models import Customer, Item ,Seller


class CustomForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    phone = forms.RegexField(regex='^\+?7?\d{9,15}$')


class SellerForm(forms.Form):
    name = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    phone = forms.RegexField(regex='^\+?7?\d{9,15}$')
    email = forms.EmailField()
    date_hiring = forms.DateField()
    position = forms.ChoiceField(choices=(('s', "salesman"), ('ss', 'senior salesman'), ('sv', 'supervisor')))


class SalesForm(forms.Form):
    data_of_sale = forms.DateTimeField()

    total = forms.IntegerField()
    c = Customer.objects.all().values()
    customer_choice = ((str(n['id']), str(n['name'])) for n in c)
    customer = forms.ChoiceField(choices=customer_choice)
    i = Item.objects.all().values()
    item_choice = ((str(n['id']), str(n['name'])) for n in i)

    item = forms.ChoiceField(choices=item_choice)
    s = Seller.objects.all().values()
    seller_choice = ((str(n['id']), str(n['name'])) for n in s)

    seller = forms.ChoiceField(choices=seller_choice)



class ItemForm(forms.Form):
    name = forms.CharField(max_length=20)
    info = forms.CharField(max_length=200)
