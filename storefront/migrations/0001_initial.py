# Generated by Django 4.1.7 on 2023-04-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=75)),
                ('price', models.FloatField()),
                ('product_type', models.CharField(max_length=50)),
                ('on_sale', models.BooleanField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
