# Generated by Django 2.1.8 on 2019-07-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190730_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='subject',
            field=models.CharField(blank=True, db_index=True, default='477542194994112', help_text='Subject ID', max_length=64),
        ),
    ]