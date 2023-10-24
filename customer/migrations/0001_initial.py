# Generated by Django 4.2.6 on 2023-10-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]