# Generated by Django 3.0.7 on 2020-06-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_auto_20200604_2327"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cname",
            field=models.URLField(blank=True, null=True),
        ),
    ]
