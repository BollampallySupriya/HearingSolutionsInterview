# Generated by Django 5.0.7 on 2024-08-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('quantity_in_stock', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
