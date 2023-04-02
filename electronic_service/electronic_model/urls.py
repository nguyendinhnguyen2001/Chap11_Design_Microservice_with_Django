from django.urls import path
from electronic_model import views

urlpatterns = [
    path('electronics/', views.electronic, name="electronics"),
    path('electronics/<int:pk>', views.electronic_detail,name="electronic-detail"),
]
