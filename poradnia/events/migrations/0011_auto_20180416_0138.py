# Generated by Django 1.11.8 on 2018-04-15 23:38
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("events", "0010_auto_20180415_1923")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="text",
            field=models.TextField(verbose_name="Subject"),
        )
    ]
