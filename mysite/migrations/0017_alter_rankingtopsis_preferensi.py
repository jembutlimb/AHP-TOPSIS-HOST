# Generated by Django 4.1.2 on 2023-11-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0016_rankingtopsis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rankingtopsis",
            name="preferensi",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]