from rest_framework import serializers
from . import models

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        serializer_class = serializers.