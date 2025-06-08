# waste_reduction/serializers.py
from rest_framework import serializers
from .models import FoodItem, WasteRecord, Donation

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class WasteRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteRecord
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'