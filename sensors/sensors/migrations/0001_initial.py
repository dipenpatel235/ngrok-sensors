# Generated by Django 2.1.4 on 2019-01-07 10:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('sensorid', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
                ('deployed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
