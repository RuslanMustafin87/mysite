# Generated by Django 4.0.3 on 2022-07-08 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_book_options_book_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit', 'Edit book'),)},
        ),
    ]
