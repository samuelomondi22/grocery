# Generated by Django 3.2.8 on 2021-10-27 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groceries',
            old_name='boulims_price',
            new_name='broulims_price',
        ),
    ]