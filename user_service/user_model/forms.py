from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers
from user_model.models import user_registration
class UserForm(serializers.ModelSerializer):
    class Meta:
        user=user_registration
        fields=("fname","lname","email","mobile","password1","password2","address")