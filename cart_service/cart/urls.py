from django.urls import path
from cart import views

urlpatterns = [
    path('showcart/<str:uname>', views.show_cart, name="carts"),
    path('addcart/',views.add_cart,name="add_cart"),
    path('deletecart/<str:uname>', views.delete, name="delete_carts"),
]
