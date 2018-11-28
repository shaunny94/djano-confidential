from rest_framework import generics
from .models import ConfidentialLabels, ConfidentialData, DoctypeData, DoctypeLabels, LanguageData, LanguageLabels
from .serializers import ConfidentialDataSerializer, ConfidentialLabelsSerializer, DoctypeDataSerializer, DoctypeLabelsSerializer, LanguageDataSerializer, LanguageLabelsSerializer


class ListConfidentialDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ConfidentialData.objects.all()
    serializer_class = ConfidentialDataSerializer


class ListConfidentialLabelsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ConfidentialLabels.objects.all()
    serializer_class = ConfidentialLabelsSerializer

class ListDoctypeDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = DoctypeData.objects.all()
    serializer_class = DoctypeDataSerializer

class ListDoctypeLabelsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = DoctypeLabels.objects.all()
    serializer_class = DoctypeLabelsSerializer


class ListLanguageDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = LanguageData.objects.all()
    serializer_class = LanguageDataSerializer

class ListLanguageLabelsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = LanguageLabels.objects.all()
    serializer_class = LanguageLabelsSerializer