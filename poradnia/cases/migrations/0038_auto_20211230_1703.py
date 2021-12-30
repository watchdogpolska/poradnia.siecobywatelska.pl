# Generated by Django 2.2.25 on 2021-12-30 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0037_auto_20191015_0510"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="case",
            options={
                "ordering": ["last_send"],
                "permissions": (
                    ("can_view", "Can view"),
                    ("can_assign", "Can assign new permissions"),
                    ("can_send_to_client", "Can send text to client"),
                    ("can_manage_permission", "Can assign permission"),
                    ("can_add_record", "Can add record"),
                    ("can_change_own_record", "Can change own records"),
                    ("can_change_all_record", "Can change all records"),
                    ("can_close_case", "Can close case"),
                    ("can_merge_case", "Can merge case"),
                    ("can_select_client", "Can select client"),
                ),
                "verbose_name": "Case",
                "verbose_name_plural": "Cases",
            },
        ),
    ]
