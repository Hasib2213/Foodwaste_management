# waste_reduction/views.py
from rest_framework import viewsets
from .models import FoodItem, WasteRecord, Donation
from .serializers import FoodItemSerializer, WasteRecordSerializer, DonationSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class WasteRecordViewSet(viewsets.ModelViewSet):
    queryset = WasteRecord.objects.all()
    serializer_class = WasteRecordSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer




    #every code in waste app