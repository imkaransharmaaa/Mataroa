# Generated by Django 3.0.7 on 2020-06-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0027_auto_20200610_1904"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="is_hidden",
            field=models.BooleanField(
                default=False,
                help_text="If checked, page link will not appear on index footer.",
            ),
        ),
    ]