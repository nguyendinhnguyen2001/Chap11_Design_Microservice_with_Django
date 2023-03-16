from payment import views
from django.urls import path, include

urlpatterns = [
    path('initpayment/', views.get_payment),
    path('payment_status/', views.user_transaction_info)
]
