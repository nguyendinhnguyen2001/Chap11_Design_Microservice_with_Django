from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # this is the model that is being serialized
        fields = ('id','title', 'auther', 'description',
                  'availability', 'publisher', 'publish_Date', 'price')
