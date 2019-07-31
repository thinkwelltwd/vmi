# Generated by Django 2.1.8 on 2019-07-30 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190730_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='subject',
            field=models.CharField(blank=True, db_index=True, default='537315119629362', help_text='Subject ID', max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]