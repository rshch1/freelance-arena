# Generated by Django 2.2.3 on 2019-07-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20190717_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
