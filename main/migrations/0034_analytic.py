# Generated by Django 3.0.8 on 2020-07-19 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0033_auto_20200626_1947"),
    ]

    operations = [
        migrations.CreateModel(
            name="Analytic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.Post"
                    ),
                ),
            ],
        ),
    ]
