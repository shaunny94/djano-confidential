
from rest_framework import serializers
from .models import ConfidentialData


class ConfidentialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialData
        fields = ("name", "total_docs")