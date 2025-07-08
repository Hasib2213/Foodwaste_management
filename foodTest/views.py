from django.shortcuts import render,redirect,get_object_or_404
import requests
from django.http import JsonResponse
import json
from django.db.models import Sum

# Create your views here.
from rest_framework import generics
from .models import Donation,contact,DonorProfile,Blog
from .serializers import DonationSerializer,ContactSerializer,BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    

class DonationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer



def submission_view(request):
    if request.method == "POST":
        donor_name = request.POST.get("donor_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        collection_address = request.POST.get("collection_address")
        food_category = request.POST.get("food_category")
        quantity = int(request.POST.get("quantity"))
        food_preparation_date = request.POST.get("food_preparation_date")
        special_note = request.POST.get("special_note", "")
        accept_terms = request.POST.get("accept_terms") == "on"

        # Save the new donation
        Donation.objects.create(
            donor_name=donor_name,
            email=email,
            phone_number=phone_number,
            collection_address=collection_address,
            food_category=food_category,
            quantity=quantity,
            food_preparation_date=food_preparation_date,
            special_note=special_note,
            accept_terms=accept_terms
        )

        # Update all donor profiles
        update_donor_profiles()

        return redirect("leaderboard")  # Redirect to updated leaderboard

    return render(request, "donation_form.html")


def donation_view(request):
    response=requests.get("http://127.0.0.1:8000/api/donations/")
    data=response.json()
    return render(request,'donation_list.html',{'food_waste_data': data})



# working for update and delete for food donations
def edit_donation(request, pk):
    donation = get_object_or_404(Donation, id=pk)
    
    if request.method == "POST":
        donation.donor_name = request.POST.get("donor_name")
        donation.email = request.POST.get("email")
        donation.phone_number = request.POST.get("phone_number")
        donation.collection_address = request.POST.get("collection_address")
        donation.food_category = request.POST.get("food_category")
        donation.quantity = int(request.POST.get("quantity", 0))
        donation.food_preparation_date = request.POST.get("food_preparation_date")
        donation.special_note = request.POST.get("special_note", "")
        donation.accept_terms = request.POST.get("accept_terms") == "on"
        donation.save()

        return redirect("Donation")  # Redirect to donation list

    return render(request, "edit_donation.html", {"donation": donation})


# Delete Donation View
def delete_donation(request, pk):
    donation = get_object_or_404(Donation, id=pk)
    
    if request.method == "POST":
        donation.delete()
        return redirect("Donation")  # Redirect after deletion

    return render(request, "confirm_delete.html", {"donation": donation})


        























def assign_reward(total_donated):
    """Assign reward level based on total food donation."""
    if total_donated >= 100:
        return "Gold"
    elif total_donated >= 50:
        return "Silver"
    elif total_donated >= 20:
        return "Bronze"
    return "New"

def update_donor_profiles():
    """Update donor profiles with correct names and total donation amounts."""
    donor_totals = Donation.objects.values("email").annotate(total_donated=Sum("quantity"))

    for donor in donor_totals:
        # Fetch the latest donor name for this email
        latest_donation = Donation.objects.filter(email=donor["email"]).order_by("-id").first()
        donor_name = latest_donation.donor_name if latest_donation else "Unknown"

        # Update or create DonorProfile with correct donor_name
        donor_profile, created = DonorProfile.objects.get_or_create(
            email=donor["email"],
            defaults={"donor_name": donor_name, "total_donated": 0, "reward_level": "New"}
        )

        # Update donor details
        donor_profile.donor_name = donor_name  # Ensure correct name
        donor_profile.total_donated = donor["total_donated"]  # Update total donations
        donor_profile.reward_level = assign_reward(donor_profile.total_donated)  # Assign reward
        donor_profile.save()



def leaderboard_view(request):
    update_donor_profiles()
    top_donors = DonorProfile.objects.order_by("-total_donated")[:10]  # Get top 10 donors
    return render(request, "leaderboard.html", {"top_donors": top_donors})



## contact part   
class contactSub(generics.ListCreateAPIView):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer
    

class Contactupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer



def contact_view(request):
    response=requests.get("http://127.0.0.1:8000/api/contact/")
    data=response.json()
    return render(request,'contactList.html',{'contact_data': data})



def contact_sub(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message= request.POST.get("message", "")
        

        # Save data to the database
        contact.objects.create(
            name=name,
            email=email,
            message=message,
        )

        return redirect("contact")  # Redirect to donation list after submission

    return render(request, "contact.html") 


#blog post

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')[:3]  # Latest 3 blogs
    serializer_class = BlogSerializer


#class for blog details
class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 

def blog_detail_template(request):
    return render(request, 'blog-detail.html')

#for blog list
def blog_list_template(request):
    return render(request, 'blog-list.html')
