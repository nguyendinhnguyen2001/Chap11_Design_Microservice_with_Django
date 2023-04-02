from rest_framework import serializers
from .models import Shoe_detail


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe_detail  # this is the model that is being serialized
        fields = ('name', 'brand', 'description',
                  'availability', 'category', 'price')
