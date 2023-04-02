from django.urls import path
from . import views

urlpatterns = [
    path("post_comment/", views.post_comment, name = "post_comment"),
    path('get_comment/<int:product_id>',views.get_comment,name="get_comment"),
]