from rest_framework import generics
from .models import ConfidentialLabels, ConfidentialData, DoctypeData
from .serializers import ConfidentialDataSerializer, ConfidentialLabelsSerializer, DoctypeDataSerializer


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