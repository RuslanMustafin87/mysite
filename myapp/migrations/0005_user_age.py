# Generated by Django 4.0.3 on 2022-05-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_user_books_user_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
