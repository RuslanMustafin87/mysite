# Generated by Django 4.0.3 on 2022-06-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_user_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('example_perm', 'example_perm'),)},
        ),
    ]