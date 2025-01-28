from .models import Customer,Seller,Order
from rest_framework import serializers


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['id','position', 'name', 'lastname', 'phone','email','date_hiring']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','lastname', 'name','phone','email']