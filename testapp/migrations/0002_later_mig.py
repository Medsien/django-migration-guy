# Generated by Django 3.0 on 2023-01-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='new_field',
            field=models.IntegerField(default=0),
        ),
    ]
