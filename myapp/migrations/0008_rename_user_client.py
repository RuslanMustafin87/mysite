# Generated by Django 4.0.3 on 2022-06-16 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_major_alter_user_age_user_major'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
    ]
