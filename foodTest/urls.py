from django.urls import path
from .views import DonationListCreateView, DonationRetrieveUpdateDestroyView,submission_view,donation_view,Contactupdate,contactSub,contact_sub,contact_view,leaderboard_view,edit_donation,delete_donation,BlogListAPIView,BlogDetailAPIView
from .import views

urlpatterns = [
   path('api/donations/', DonationListCreateView.as_view(), name='donation-list-create'),
   path('api/donations/<int:pk>/', DonationRetrieveUpdateDestroyView.as_view(), name='donation-retrieve-update-destroy'),
   # path('Vsub/',views.submission_view, name="submission"),
    path('Vdon/', views.donation_view, name="Donation"),
    path("Vsub/", submission_view, name="submission"),
    path('Vedit/<int:pk>/', edit_donation, name="edit-donation"),
    path('Vdelete/<int:pk>/', delete_donation, name="delete-donation"),
    
    path("leaderboard/", leaderboard_view, name="leaderboard"),
# contact url

    path('api/contact/',contactSub.as_view(), name='api-contact-view'),
    path('api/contact/<int:pk>/',Contactupdate.as_view(), name='api-contact-update'),
    path('contactsub/', contact_sub, name="contact"),
    path('contactview/', contact_view, name="contactview"),
#blog post
    path('api/blogs/', BlogListAPIView.as_view(), name='blog-list'),
     path('api/blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blog-detail/', views.blog_detail_template, name='blog-detail-page'),

path('blogs/', views.blog_list_template, name='blog-list-page'),

# real time alert
path('alerts/', views.alert_dashboard, name='alert-dashboard'),
# Add Inventory
path('add/', views.add_inventory, name='add-inventory'),
    path('success/', views.inventory_success, name='inventory-success'),

]
