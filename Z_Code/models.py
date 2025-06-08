# waste_reduction/models.py
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    location = models.CharField(max_length=255)  # Google Location Integration
    status = models.CharField(max_length=50, default='fresh')  # fresh, near_expiry, expired

    def __str__(self):
        return self.name

class WasteRecord(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    wasted_quantity = models.IntegerField()
    reason = models.CharField(max_length=255)  # Reason for waste
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item.name} - {self.wasted_quantity} wasted"

class Donation(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    donated_to = models.CharField(max_length=255)  # Charity or organization name
    donated_quantity = models.IntegerField()
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item.name} donated to {self.donated_to}"