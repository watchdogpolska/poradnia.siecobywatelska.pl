# Generated by Django 3.2.18 on 2023-04-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0038_auto_20211230_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Case number'),
        ),
    ]
