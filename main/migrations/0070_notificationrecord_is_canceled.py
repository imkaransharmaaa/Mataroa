# Generated by Django 3.2 on 2021-05-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0069_alter_analyticpage_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationrecord",
            name="is_canceled",
            field=models.BooleanField(default=False),
        ),
    ]
