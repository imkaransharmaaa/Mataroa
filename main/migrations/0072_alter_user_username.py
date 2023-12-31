# Generated by Django 4.0.3 on 2022-04-11 22:53

from django.db import migrations, models

import main.validators


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0071_user_monero_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="This is your subdomain. Lowercase alphanumeric.",
                max_length=150,
                unique=True,
                validators=[
                    main.validators.AlphanumericHyphenValidator(),
                    main.validators.HyphenOnlyValidator(),
                ],
            ),
        ),
    ]
