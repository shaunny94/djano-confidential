
from django.urls import path
from .views import ListConfidentialDataView, ListConfidentialLabelsView


urlpatterns = [
    path('confidentialdata/', ListConfidentialDataView.as_view(), name="confidentialdata"),
    path('confidentiallabels/', ListConfidentialLabelsView.as_view(), name="confidentiallabels")

]