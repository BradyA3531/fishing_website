# Generated by Django 4.1.5 on 2023-05-02 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_alter_order_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user_email',
        ),
    ]