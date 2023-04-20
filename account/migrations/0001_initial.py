# Generated by Django 4.1.7 on 2023-04-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('signup_date', models.DateField(auto_created=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('addressline1', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=20)),
                ('sec_answer', models.CharField(max_length=50)),
            ],
        ),
    ]
