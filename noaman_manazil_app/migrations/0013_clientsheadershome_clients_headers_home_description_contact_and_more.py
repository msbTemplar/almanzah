# Generated by Django 5.2.1 on 2025-06-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noaman_manazil_app', '0012_clientsheadershome'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsheadershome',
            name='clients_headers_home_description_contact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clientsheadershome',
            name='clients_headers_home_title_contact',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
