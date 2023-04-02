from django.urls import path
from order import views

urlpatterns = [
    path("order/",views.get_order,name="Orders"),
]
