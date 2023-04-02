from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart  # this is the model that is being serialized
        fields = ('uname','product_id','quantity')
