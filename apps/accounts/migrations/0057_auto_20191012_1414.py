# Generated by Django 2.2.4 on 2019-10-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_organization_number_str_include'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='agree_privacy_policy',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='agree_tos',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='auto_ial_2_for_agents',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='auto_ial_2_for_agents_description',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='default_groups_for_agents',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='members',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='number_str_include',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='point_of_contact',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='registration_code',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='users',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='website',
        ),
    ]