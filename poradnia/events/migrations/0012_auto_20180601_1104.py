# Generated by Django 1.11.13 on 2018-06-01 09:04
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0011_auto_20180416_0138")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="deadline",
            field=models.BooleanField(
                default=False,
                help_text="A significant event, especially highlighted, for example, in the list of cases.",
                verbose_name="Dead-line",
            ),
        )
    ]
