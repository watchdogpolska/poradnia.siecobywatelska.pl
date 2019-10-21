# Generated by Django 1.11.8 on 2018-04-15 21:13
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("judgements", "0001_initial"),
        ("records", "0007_remove_record_alarm"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="courtcase",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="judgements.CourtCase",
            ),
        )
    ]
