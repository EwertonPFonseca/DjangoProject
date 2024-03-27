# Generated by Django 5.0.3 on 2024-03-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
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
                ("nome", models.CharField(max_length=200)),
                ("biografia", models.TextField()),
                ("url_foto", models.CharField(max_length=1000)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_modificao", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
