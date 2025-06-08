from django.db import models

# Create your models here.

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    collection_address = models.TextField()
    food_category = models.CharField(max_length=10, choices=[('veg', 'Vegetarian'), ('non_veg', 'Non-Vegetarian'), ('both', 'Both')])
    quantity = models.PositiveIntegerField()
    food_preparation_date = models.DateField()
    special_note = models.TextField(blank=True, null=True)
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.donor_name


class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(blank=True,null=True)


    def __str__(self):
        return self.name
    



class DonorProfile(models.Model):
    donor_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    total_donated = models.PositiveIntegerField(default=0)
    reward_level = models.CharField(max_length=20, default="New")  # New, Bronze, Silver, Gold

    def __str__(self):
        return f"{self.donor_name} - {self.reward_level} - {self.total_donated} kg"
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    