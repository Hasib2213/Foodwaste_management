from django.contrib import admin
from wastes.models import InventoryItem,Charity,FoodDonation,Reward,SustainabilityMetrics,Contributor

# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Charity)
admin.site.register(FoodDonation)
admin.site.register(Reward)
admin.site.register(SustainabilityMetrics)
admin.site.register(Contributor)
