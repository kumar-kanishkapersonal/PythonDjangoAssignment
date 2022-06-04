from django.urls import path
from . import views

urlpatterns = [
    path('Retrieve_Sales_by_Drug_Classification/', views.Retrieve_Sales_by_Drug_Classification),
    path('Retrieve_Drug_Reviews_for_a_given_Drug/', views.Retrieve_Drug_Reviews_for_a_given_Drug),
]
