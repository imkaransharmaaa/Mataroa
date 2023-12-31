# Generated by Django 3.1.7 on 2021-03-17 23:13

from django.db import migrations, models

import main.validators


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0055_user_theme_zialucia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="custom_domain",
            field=models.CharField(
                blank=True,
                help_text="To setup: Add an A record in your domain's DNS with IP 95.217.30.133",
                max_length=150,
                null=True,
                validators=[main.validators.validate_domain_name],
            ),
        ),
    ]
