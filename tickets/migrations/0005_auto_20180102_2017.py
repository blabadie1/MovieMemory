# Generated by Django 2.0 on 2018-01-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20180102_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_seen',
            field=models.CharField(max_length=100),
        ),
    ]
