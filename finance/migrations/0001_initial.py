# Generated by Django 5.0.4 on 2024-05-04 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=32)),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=24)),
                ('date', models.DateField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=24)),
                ('counterparty_name', models.CharField(max_length=256, null=True)),
                ('counterparty_account', models.CharField(max_length=32, null=True)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.category')),
            ],
        ),
    ]
