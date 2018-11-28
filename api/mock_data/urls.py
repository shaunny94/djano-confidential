
from django.urls import path
from .views import ListConfidentialDataView, ListConfidentialLabelsView, ListDoctypeDataView, ListDoctypeLabelsView, ListLanguageDataView, ListLanguageLabelsView


urlpatterns = [
    path('confidentialdata/', ListConfidentialDataView.as_view(), name="confidentialdata"),
    path('confidentiallabels/', ListConfidentialLabelsView.as_view(), name="confidentiallabels"),
    path('doctypedata/', ListDoctypeDataView.as_view(), name="doctypedata"),
    path('doctypelabels/', ListDoctypeLabelsView.as_view(), name="doctypelabels"),
    path('languagedata/', ListLanguageDataView.as_view(), name="languagedata"),
    path('languagelabels/', ListLanguageLabelsView.as_view(), name="languagelabels")
]