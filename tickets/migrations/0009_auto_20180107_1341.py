# Generated by Django 2.0 on 2018-01-07 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0008_auto_20180102_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='viewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_seen',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='notes',
            field=models.TextField(max_length=215),
        ),
    ]
