from django.http import HttpResponse
from django.template import loader
from .forms import CustomForm, SellerForm, ItemForm, SalesForm
from .models import Customer, Seller, Item, Sales
from django.shortcuts import render
from rest_framework import permissions, viewsets

from .serializers import CustomerSerializer, SellerSerializer


def index(request):
    template = loader.get_template("sales/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context


def Custom_info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        c = Customer.objects.values_list('name')
        r = ((str(n)[1:], str(n)) for n in c)
        e = Customer(name=name, lastname=lastname, email=email, phone=phone)
        e.save()

        return HttpResponse('ok')
    else:

        customform = CustomForm()
        template = loader.get_template("sales/forms.html")
        context = get_context('Главная страница', {'form': customform})
        return HttpResponse(template.render(context, request))


def Seller_info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_hiring = request.POST.get('date_hiring')
        position = request.POST.get('position')
        e = Seller(name=name, lastname=lastname, email=email, phone=phone, date_hiring=date_hiring, position=position)
        e.save()

        return HttpResponse('ok')
    else:

        sellerform = SellerForm()
        template = loader.get_template("sales/forms.html")
        context = get_context('Главная страница', {'form': sellerform})
        return HttpResponse(template.render(context, request))


def Sales_info(request):
    if request.method == "POST":

        date = request.POST.get('data_of_sale')
        total = request.POST.get('total')
        customer_id = request.POST.get('customer')
        customer = Customer.objects.filter(id=customer_id).all()
        seller_id = request.POST.get('seller')
        seller = Seller.objects.filter(id=seller_id).all()
        item_id = request.POST.get('item')
        item = Item.objects.filter(id=item_id).all()
        e = Sales(data_of_sale=date, total=total, customer=customer[0], seller=seller[0], item=item[0])
        e.save()

        return HttpResponse('ok')
    else:

        orderform = SalesForm()
        template = loader.get_template("sales/forms.html")
        context = get_context('Главная страница', {'form': orderform})
        return HttpResponse(template.render(context, request))


def Item_info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        info = request.POST.get('info')

        e = Item(name=name, info=info)
        e.save()

        return HttpResponse('ok')
    else:

        itemform = ItemForm()
        template = loader.get_template("sales/forms.html")
        context = get_context('Главная страница', {'form': itemform})
        return HttpResponse(template.render(context, request))


def Info(request):
    sellers = Seller.objects.all().values()
    customers = Customer.objects.all().values()
    items = Item.objects.all().values()
    template = loader.get_template('sales/info.html')
    context = {
        'sellers': sellers,
        'items': items,
        'customers': customers
    }
    return HttpResponse(template.render(context, request))


def Members(request):
    sellers = Seller.objects.all().values()
    template = loader.get_template('beautiful.html')
    context = {
        'sellers': sellers,
    }
    return HttpResponse(template.render(context, request))


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('lastname')
    serializer_class = CustomerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.filter(id=4).values()
    serializer_class = SellerSerializer
