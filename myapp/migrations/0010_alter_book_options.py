# Generated by Django 4.0.3 on 2022-06-16 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('example_perm', 'example perm'),)},
        ),
    ]
