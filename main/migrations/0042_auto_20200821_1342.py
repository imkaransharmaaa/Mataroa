# Generated by Django 3.1 on 2020-08-21 13:42

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0041_auto_20200820_2107"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postnotification",
            name="unsubscribe_key",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
