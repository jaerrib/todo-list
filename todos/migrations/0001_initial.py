# Generated by Django 5.0 on 2024-01-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("details", models.TextField()),
                ("important", models.BooleanField(default=False)),
                ("urgent", models.BooleanField(default=False)),
                ("due_date", models.DateField()),
            ],
        ),
    ]
