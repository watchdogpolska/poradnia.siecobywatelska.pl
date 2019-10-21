# Generated by Django 1.11.8 on 2018-04-15 17:16
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0007_remove_record_alarm"),
        ("events", "0007_reminder"),
    ]

    operations = [
        migrations.RemoveField(model_name="alarm", name="case"),
        migrations.RemoveField(model_name="alarm", name="event"),
        migrations.RemoveField(model_name="reminder", name="triggered"),
        migrations.AddField(
            model_name="reminder",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="created",
            ),
        ),
        migrations.AddField(
            model_name="reminder",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="modified",
            ),
        ),
        migrations.AlterField(
            model_name="reminder",
            name="event",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="events.Event"
            ),
        ),
        migrations.DeleteModel(name="Alarm"),
    ]
