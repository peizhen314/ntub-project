# Generated by Django 4.2.11 on 2024-05-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_review_review_result_alter_review_review_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_place",
            field=models.CharField(
                choices=[("taipei", "Taipei"), ("yilan", "Yilan")], max_length=32
            ),
        ),
    ]
