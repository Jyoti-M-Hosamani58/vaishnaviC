# Generated by Django 5.1.4 on 2025-01-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0006_tripsheetprem_consigneeaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='date',
            field=models.DateField(max_length=250, null=True),
        ),
    ]
