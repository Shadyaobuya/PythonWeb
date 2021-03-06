# Generated by Django 3.2.4 on 2021-09-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30, null=True)),
                ('venue', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('link', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
