# Generated by Django 5.0.4 on 2024-05-05 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_alter_user_emplid_alter_user_epantherid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='campusphone',
            new_name='phone',
        ),
    ]