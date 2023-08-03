# Generated by Django 3.1.7 on 2021-03-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0056_auto_20210317_2313"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="footer_note",
            field=models.CharField(
                blank=True,
                default="Powered&nbsp;by&nbsp;[mataroa.blog](https://mataroa.blog/).",
                help_text="Supports markdown",
                max_length=500,
                null=True,
            ),
        ),
    ]
