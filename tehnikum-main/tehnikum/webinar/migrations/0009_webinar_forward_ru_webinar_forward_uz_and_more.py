# Generated by Django 4.1.4 on 2023-01-16 09:17

from django.db import migrations, models

import tehnikum.webinar.validators


class Migration(migrations.Migration):

    dependencies = [
        ("webinar", "0008_subscription_is_sent"),
    ]

    operations = [
        migrations.AddField(
            model_name="webinar",
            name="forward_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="webinar",
            name="forward_uz",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="webinar",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="pics", validators=[tehnikum.webinar.validators.validate_image]
            ),
        ),
    ]
