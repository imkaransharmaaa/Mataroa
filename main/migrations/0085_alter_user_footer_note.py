# Generated by Django 4.1.3 on 2022-12-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0084_alter_user_post_backups_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="footer_note",
            field=models.TextField(
                blank=True,
                default="Powered by [mataroa.blog](https://mataroa.blog/).",
                help_text="Supports markdown",
                null=True,
            ),
        ),
    ]
