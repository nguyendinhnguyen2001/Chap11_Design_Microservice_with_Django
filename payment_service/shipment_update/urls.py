from shipment_update import views
from django.urls import path, include

urlpatterns = [
    path('shipment_details/', views.shipment_details_update),
]
