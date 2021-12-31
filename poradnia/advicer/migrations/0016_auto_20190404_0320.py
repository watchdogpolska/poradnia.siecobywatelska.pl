# Generated by Django 1.11.13 on 2019-04-04 01:20
import django.db.models.deletion
from django.db import migrations, models


def fill_area(apps, schema_editor):
    Advice = apps.get_model("advicer", "Advice")
    for row in Advice.objects.all():
        if row.area_old:
            row.area = [row.area_old]
            row.save()


class Migration(migrations.Migration):
    dependencies = [("advicer", "0015_auto_20180104_0436")]

    operations = [
        migrations.RenameField(
            model_name="advice", old_name="area", new_name="area_old"
        ),
        migrations.AddField(
            model_name="advice",
            name="area",
            field=models.ManyToManyField(
                blank=True,
                to="advicer.Area",
                verbose_name="Thematic scopes of requests",
            ),
        ),
        migrations.AlterField(
            model_name="advice",
            name="area_old",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="xxxxxx",
                to="advicer.Area",
                verbose_name="Problem regarding the right to information",
            ),
        ),
        migrations.RunPython(fill_area),
        migrations.RemoveField(model_name="advice", name="area_old"),
    ]
