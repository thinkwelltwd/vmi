# Generated by Django 2.2.4 on 2019-10-25 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191024_1659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MFACode',
        ),
    ]
