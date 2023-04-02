from django.urls import path
from clothe_model import views

urlpatterns = [
    path('clothes/', views.clothe, name="clothes"),
    path('clothes/<int:pk>', views.clothe_detail,name="clothe-detail"),
]
