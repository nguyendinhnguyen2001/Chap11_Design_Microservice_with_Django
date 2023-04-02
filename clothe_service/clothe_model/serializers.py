from rest_framework import serializers
from .models import Clothe_detail


class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe_detail  # this is the model that is being serialized
        fields = ('name', 'brand', 'description',
                  'availability', 'category', 'price')
