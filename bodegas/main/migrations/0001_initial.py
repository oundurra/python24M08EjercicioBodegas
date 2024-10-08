# Generated by Django 5.0.6 on 2024-08-26 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("username", models.CharField(db_column="username", max_length=16)),
                ("email", models.CharField(db_column="email", max_length=255)),
                ("password", models.CharField(db_column="password", max_length=32)),
                ("name", models.CharField(db_column="first_name", max_length=45)),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TipoBodega",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tipo", models.CharField(max_length=255)),
                ("metros", models.IntegerField()),
                ("quimicos", models.IntegerField()),
                ("organicos", models.IntegerField()),
                ("hermetico", models.IntegerField()),
                ("precio", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Noticia",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=45)),
                ("imagen_url", models.CharField(max_length=255)),
                (
                    "users",
                    models.ManyToManyField(related_name="noticias", to="main.user"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bodega",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("codigo", models.CharField(max_length=10)),
                (
                    "tipo_bodega",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.tipobodega",
                    ),
                ),
            ],
        ),
    ]
