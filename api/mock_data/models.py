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
    id_number = models.ForeignKey(ConfidentialData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.name, self.id_number)


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
    id_number = models.ForeignKey(DoctypeData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.name, self.id_number)

class LanguageData(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    total_docs = models.IntegerField(default=0)
    short_name = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.name, self.total_docs, self.short_name)

class LanguageLabels(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    id_number = models.ForeignKey(LanguageData, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    shortName = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.name, self.id_number, self.short_name)