# Generated by Django 4.0.6 on 2023-08-24 16:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('id_number', models.CharField(max_length=10)),
                ('date_joined', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('rate', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('number_of_orders', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=100)),
                ('no', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
                ('ppg', models.CharField(max_length=30)),
                ('market', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.market')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markets', models.ManyToManyField(to='users.market')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=100)),
                ('basket', models.ManyToManyField(to='users.stock')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]