# Generated by Django 1.11.11 on 2018-04-23 20:42
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("letters", "0010_auto_20180104_0436")]

    operations = [
        migrations.AddField(
            model_name="letter",
            name="html",
            field=models.TextField(blank=True, verbose_name="HTML"),
        )
    ]
