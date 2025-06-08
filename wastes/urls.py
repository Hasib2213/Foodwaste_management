from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
   # path('contact/', views.contact, name='contact'),
    path('api/inventory/', views.get_inventory, name='get_inventory'),
    path('api/charities/', views.get_charities, name='get_charities'),
    path('donate/', views.donate_food, name='donate_food'),
    path('api/metrics/', views.get_sustainability_metrics, name='get_sustainability_metrics'),
    path('contributors/', views.top_contributors, name='top_contributors'),
    
   
]
