# Generated by Django 5.0.6 on 2024-06-12 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatgpt", "0006_delete_helpaivleqa"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatgptHelpaivleqa",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("pclass", models.TextField()),
                ("qa", models.TextField()),
            ],
            options={
                "db_table": "chatgpt_helpaivleQA",
                "managed": False,
            },
        ),
    ]
