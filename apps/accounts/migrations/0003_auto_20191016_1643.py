# Generated by Django 2.2.4 on 2019-10-16 16:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191012_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='Employees or contractors acting on behalf of the Organization.', related_name='org_staff', to=settings.AUTH_USER_MODEL, verbose_name='Organizational Agent'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender_identity',
            field=models.CharField(blank=True, choices=[('', 'Blank'), ('female', 'Female'), ('male', 'Male'), ('custom', 'Custom')], default='', help_text='Gender Identity is not necessarily the same as birth sex.', max_length=64, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to='profile-picture/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('', 'Blank'), ('female', 'Female'), ('male', 'Male'), ('other', 'Gender Neutral')], default='', help_text='Specify birth sex, not gender identity.', max_length=6),
        ),
    ]
