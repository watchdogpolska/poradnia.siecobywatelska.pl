# Generated by Django 3.2.18 on 2023-03-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0014_merge_20211230_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='html',
            field=models.TextField(blank=True, verbose_name='Mail formatted HTML'),
        ),
    ]
