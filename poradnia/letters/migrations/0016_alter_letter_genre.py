# Generated by Django 3.2.18 on 2023-04-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0015_alter_letter_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='genre',
            field=models.CharField(choices=[('mail', 'mail'), ('comment', 'comment'), ('app_message', 'app_message')], default='comment', max_length=20),
        ),
    ]
