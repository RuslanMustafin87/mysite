# Generated by Django 4.0.3 on 2022-05-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
