# Generated by Django 5.0.6 on 2024-06-26 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_travel_hotel_travel_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='amount_of_start',
            new_name='amount_of_star',
        ),
    ]
