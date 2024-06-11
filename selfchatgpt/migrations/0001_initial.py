# Generated by Django 5.0.6 on 2024-06-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Helpaivleqa",
            fields=[
                (
                    "id",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
                (
                    "class_field",
                    models.TextField(blank=True, db_column="class", null=True),
                ),
                ("qa", models.TextField(blank=True, db_column="QA", null=True)),
            ],
            options={
                "db_table": "helpaivleqa",
                "managed": False,
            },
        ),
    ]
