from django.urls import path
from shoe_model import views

urlpatterns = [
    path('shoes/', views.shoe, name="shoes"),
    path('shoes/<int:pk>', views.shoe_detail,name="shoe-detail"),
]
