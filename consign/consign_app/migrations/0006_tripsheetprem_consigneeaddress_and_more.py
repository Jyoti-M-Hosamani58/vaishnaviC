# Generated by Django 5.1.4 on 2024-12-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0005_collection_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripsheetprem',
            name='consigneeAddress',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheetprem',
            name='consigneeGST',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheetprem',
            name='consignor',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheetprem',
            name='consignorAddress',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheetprem',
            name='consignorGST',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='consigneeAddress',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='consigneeGST',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='consignor',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='consignorAddress',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='consignorGST',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
