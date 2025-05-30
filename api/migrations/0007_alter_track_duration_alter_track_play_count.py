# Generated by Django 4.2.9 on 2025-05-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_playstate_volume_alter_playstate_context_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="duration",
            field=models.PositiveBigIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name="track",
            name="play_count",
            field=models.PositiveBigIntegerField(default=0, editable=False),
        ),
    ]
