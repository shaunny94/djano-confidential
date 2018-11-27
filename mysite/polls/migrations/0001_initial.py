# Generated by Django 2.0.6 on 2018-11-27 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfidentialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_docs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ConfidentialLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('confidential_labels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.ConfidentialData')),
            ],
        ),
        migrations.CreateModel(
            name='DoctypeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_docs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DoctypeLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('doctype_labels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.DoctypeData')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_docs', models.IntegerField(default=0)),
                ('short_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=200)),
                ('language_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LanguageData')),
            ],
        ),
    ]
