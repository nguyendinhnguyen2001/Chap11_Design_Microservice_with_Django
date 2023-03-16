from ship_status import views
from django.urls import path, include

urlpatterns = [
    path('shipment_status/', views.shipment_status),
    path('add_shipment/', views.shipment_reg_update),
]
