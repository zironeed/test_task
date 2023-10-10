from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from shop.models import Seller, Contact, Product
from shop.serializers import SellerSerializer, ContactSerializer, ProductSerializer, SellerCreateSerializer


class SellerListView(ListAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class SellerCreateView(CreateAPIView):
    serializer_class = SellerCreateSerializer
    queryset = Seller.objects.all()


class SellerRetrieveView(RetrieveAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class SellerUpdateView(UpdateAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class SellerDestroyView(DestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class ContactCreateView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetrieveView(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactUpdateView(UpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
