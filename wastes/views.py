from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import InventoryItem, FoodDonation, Reward, SustainabilityMetrics, Contributor, Charity
from datetime import datetime, timedelta

# Home Page
def index(request):
    return render(request, 'index.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Get Inventory Items (for alerts)
def get_inventory(request):
    items = InventoryItem.objects.all()
    data = [{'id': item.id, 'name': item.name, 'expiry_date': item.expiry_date.strftime("%Y-%m-%d"), 'quantity': item.quantity} for item in items]
    return JsonResponse(data, safe=False)

# Get Charities
def get_charities(request):
    charities = Charity.objects.all()
    data = [{'id': charity.id, 'name': charity.name, 'location': charity.location} for charity in charities]
    return JsonResponse(data, safe=False)

# Donation Matching System
@login_required
def donate_food(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")
        charity_id = request.POST.get("charity_id")
        quantity = int(request.POST.get("quantity"))

        food_item = InventoryItem.objects.get(id=food_id)
        charity = Charity.objects.get(id=charity_id)

        FoodDonation.objects.create(
            donor=request.user, food_item=food_item, quantity_donated=quantity, charity=charity
        )

        # Update Inventory
        food_item.quantity -= quantity
        food_item.save()

        # Reward Points
        reward, created = Reward.objects.get_or_create(user=request.user)
        reward.points += 10  # Add points for donation
        reward.save()

        # Update Contributor
        contributor, created = Contributor.objects.get_or_create(user=request.user)
        contributor.contributions += 1
        contributor.save()

        return redirect("index")

    inventory = InventoryItem.objects.all()
    charities = Charity.objects.all()
    return render(request, "donate.html", {"inventory": inventory, "charities": charities})

# Get Sustainability Impact Metrics
def get_sustainability_metrics(request):
    metrics = SustainabilityMetrics.objects.all()
    data = [{'user': metric.user.username, 'carbon_reduction': metric.carbon_reduction, 'economic_savings': metric.economic_savings} for metric in metrics]
    return JsonResponse(data, safe=False)

# Display Top Contributors
def top_contributors(request):
    contributors = Contributor.objects.order_by('-contributions')[:5]
    return render(request, "contributors1.html", {"contributors": contributors})