from django.shortcuts import render
from rest_framework import generics
from .models import ConfidentialData
from .serializers import ConfidentialDataSerializer
# Create your views here.
from django.http import HttpResponse

class ListConfidentialDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ConfidentialData.objects.all()  
    serializer_class = ConfidentialDataSerializer




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")