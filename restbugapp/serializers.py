from .models import *
from rest_framework.serializers import *

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
