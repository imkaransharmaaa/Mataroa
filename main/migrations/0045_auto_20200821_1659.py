# Generated by Django 3.1 on 2020-08-21 16:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0044_postnotificationrecord_post"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="postnotificationrecord",
            unique_together={("post", "post_notification")},
        ),
    ]
