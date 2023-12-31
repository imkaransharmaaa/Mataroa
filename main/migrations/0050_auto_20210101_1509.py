# Generated by Django 3.1 on 2021-01-01 15:09

from django.db import migrations, models

import main.validators


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0049_user_redirect_domain"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="redirect_domain",
            field=models.CharField(
                blank=True,
                help_text="Retiring your mataroa blog? We can redirect to your new domain.",
                max_length=150,
                null=True,
                validators=[main.validators.validate_domain_name],
            ),
        ),
    ]
