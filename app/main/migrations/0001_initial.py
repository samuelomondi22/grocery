# Generated by Django 3.2.8 on 2021-10-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groceries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('walmart_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('boulims_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('albertsons_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
