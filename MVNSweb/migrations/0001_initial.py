# Generated by Django 4.1.3 on 2022-11-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Readings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('reading_time', models.TimeField(auto_now_add=True, verbose_name='Time')),
                ('motorist_first_name', models.CharField(max_length=255, verbose_name='Motorist First Name')),
                ('motorist_middle_initial', models.CharField(blank=True, max_length=2, verbose_name='Motorist Middle Initial')),
                ('motorist_last_name', models.CharField(max_length=255, verbose_name='Motorist Last Name')),
                ('db_reading', models.IntegerField(verbose_name='db')),
                ('distance_reading', models.IntegerField(verbose_name='Distance')),
            ],
        ),
    ]
