# Generated by Django 3.0.7 on 2020-07-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veva_pcs', '0004_auto_20200709_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
