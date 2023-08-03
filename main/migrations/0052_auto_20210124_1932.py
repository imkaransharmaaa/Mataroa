# Generated by Django 3.1 on 2021-01-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0051_auto_20210111_2111"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="comments_on",
            field=models.BooleanField(
                default=False,
                help_text="Enable/disable comments for your blog",
                verbose_name="Comments",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="notifications_on",
            field=models.BooleanField(
                default=False,
                help_text="Allow/disallow people subscribing for email newsletter for new posts",
                verbose_name="Newsletter",
            ),
        ),
    ]
