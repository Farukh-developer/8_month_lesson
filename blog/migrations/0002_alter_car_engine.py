# Generated by Django 5.0.6 on 2024-06-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=30),
        ),
    ]
