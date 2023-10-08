from rest_framework import serializers
from shop.models import Seller, Contact, Product


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'