# Generated by Django 4.0.6 on 2023-09-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_market_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ppg',
            field=models.CharField(max_length=50),
        ),
    ]