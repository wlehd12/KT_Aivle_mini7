# Generated by Django 5.0.6 on 2024-06-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatgpt", "0007_chatgpthelpaivleqa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chathistory",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
