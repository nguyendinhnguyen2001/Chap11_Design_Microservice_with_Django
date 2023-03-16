from django import urls
from django.urls import path

from user_model import views

urlpatterns=[
    path('',views.registration_req,),
    path('showall/',views.show_user,),
]