# Generated by Django 3.0.7 on 2020-07-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veva_pcs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
