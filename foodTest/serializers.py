from rest_framework import serializers
from .models import Donation,contact,Blog

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'