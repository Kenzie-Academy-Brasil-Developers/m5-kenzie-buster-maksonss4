# Generated by Django 4.1.4 on 2022-12-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_birthdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=50),
        ),
    ]
