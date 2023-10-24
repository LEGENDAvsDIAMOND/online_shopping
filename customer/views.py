from django.shortcuts import render
from rest_framework import viewsets
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import generics

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
