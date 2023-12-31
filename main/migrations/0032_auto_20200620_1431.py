# Generated by Django 3.0.7 on 2020-06-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0031_auto_20200620_1344"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="webring_next_url",
            field=models.URLField(
                blank=True,
                help_text="URL for your webring's next website.",
                null=True,
                verbose_name="Webring next URL",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="webring_prev_url",
            field=models.URLField(
                blank=True,
                help_text="URL for your webring's previous website.",
                null=True,
                verbose_name="Webring previous URL",
            ),
        ),
    ]
