# Generated by Django 5.0.6 on 2024-06-12 05:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("selfchatgpt", "0005_chathistory_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chathistory",
            name="user",
        ),
    ]