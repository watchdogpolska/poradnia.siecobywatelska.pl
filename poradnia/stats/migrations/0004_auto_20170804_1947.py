
# Generated by Django 1.11.4 on 2017-08-04 17:47
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20170804_0413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='value',
            options={'ordering': ['item_id', 'time'], 'verbose_name': 'Value', 'verbose_name_plural': 'Values'},
        ),
    ]
