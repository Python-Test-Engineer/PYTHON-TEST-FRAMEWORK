# Generated by Django 4.2.7 on 2024-01-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orm", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staff",
            options={"verbose_name_plural": "Staff"},
        ),
        migrations.AlterModelOptions(
            name="staffrestaurant",
            options={"verbose_name_plural": "Staff Restaurant"},
        ),
        migrations.AlterField(
            model_name="staffrestaurant",
            name="salary",
            field=models.FloatField(default=10000.0, null=True),
        ),
    ]
