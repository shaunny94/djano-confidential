from django.urls import path
from .views import ListConfidentialDataView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('confidential/', ListConfidentialDataView.as_view(), name="confidential-data")

]