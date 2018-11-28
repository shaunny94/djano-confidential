from rest_framework import serializers
from .models import ConfidentialData, ConfidentialLabels, DoctypeData


class ConfidentialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialData
        fields = ("name", "total_docs")

class ConfidentialLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialLabels
        fields = ("name", "confidential_labels")

class DoctypeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctypeData
        fields = ("name", "total_docs")