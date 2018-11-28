from rest_framework import serializers
from .models import ConfidentialData, ConfidentialLabels, DoctypeData, DoctypeLabels, LanguageData, LanguageLabels


class ConfidentialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialData
        fields = ("name", "total_docs", "id")

class ConfidentialLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialLabels
        fields = ("name", "id" )

class DoctypeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctypeData
        fields = ("name", "total_docs", "id")

class DoctypeLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctypeLabels
        fields = ("name",  "id")

class LanguageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageData
        fields = ("name","total_docs", "short_name",  "id")

class LanguageLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageLabels
        fields = ("name", "shortName",  "id")