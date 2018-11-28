# Create your models here.
from django.db import models


class ConfidentialData(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    total_docs = models.IntegerField(default=0)
    def __str__(self):
            return "{} - {}".format(self.name, self.total_docs)

class ConfidentialLabels(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    confidential_labels = models.ForeignKey(ConfidentialData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.name, self.confidential_labels)


class DoctypeData(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    total_docs = models.IntegerField(default=0)
    def __str__(self):
        return "{} - {}".format(self.name, self.total_docs)

class DoctypeLabels(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    doctype_labels = models.ForeignKey(DoctypeData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

class LanguageData(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    total_docs = models.IntegerField(default=0)
    short_name = models.CharField(max_length=200)

class LanguageLabels(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    language_data = models.ForeignKey(LanguageData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    shortName = models.CharField(max_length=200)