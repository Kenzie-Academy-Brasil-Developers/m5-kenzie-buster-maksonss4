# Generated by Django 4.1.4 on 2022-12-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "General Audiences"),
                    ("PG", "Parental Guidance Suggested"),
                    ("PG-13", "Parents Strongly Cautioned"),
                    ("R", "Restricted"),
                    ("NC-17", "Adults Only"),
                ],
                default="G",
                max_length=20,
            ),
        ),
    ]
