# Generated by Django 2.2.3 on 2019-07-17 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_moneylog_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneylog',
            old_name='creadit',
            new_name='credit',
        ),
    ]