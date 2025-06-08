

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Inventory Management Model
class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# Charity Model
class Charity(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

# Food Donation Model
class FoodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_donated = models.IntegerField()
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    donation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.donor.username} -> {self.charity.name}"

# Reward System
class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badges = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.points} points"

# Sustainability Impact Metrics
class SustainabilityMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carbon_reduction = models.FloatField()
    economic_savings = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"

# Top Contributors Display
class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contributions = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - {self.contributions} contributions"
