from rest_framework import serializers
from .models import Electronic_detail


class ElectronicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic_detail  # this is the model that is being serialized
        fields = ('name', 'sku', 'description',
                  'availability', 'price')
