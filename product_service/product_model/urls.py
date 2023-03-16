from product_model import views
from django.urls import path, include

urlpatterns = [
    path('getproduct/', views.get_product_data),
]
