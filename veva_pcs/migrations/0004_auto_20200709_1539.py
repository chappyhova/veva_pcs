# Generated by Django 3.0.7 on 2020-07-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veva_pcs', '0003_auto_20200708_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
        migrations.AddField(
            model_name='basket',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
