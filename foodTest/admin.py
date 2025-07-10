from django.contrib import admin

# Register your models here.
from foodTest.models import Donation,contact,DonorProfile,Blog,Inventory

# Register your models here.
admin.site.register(Donation)
admin.site.register(contact)
admin.site.register(DonorProfile)
admin.site.register(Blog)
admin.site.register(Inventory)