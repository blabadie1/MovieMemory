# Generated by Django 2.0 on 2018-01-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20180102_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_seen',
            field=models.DateTimeField(default="Use format 'D/M/Y 19:30'"),
        ),
    ]