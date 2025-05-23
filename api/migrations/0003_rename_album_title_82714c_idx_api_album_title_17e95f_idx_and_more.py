# Generated by Django 4.2.9 on 2025-04-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_user_email"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="album",
            new_name="api_album_title_17e95f_idx",
            old_name="album_title_82714c_idx",
        ),
        migrations.RenameIndex(
            model_name="album",
            new_name="api_album_release_99d61e_idx",
            old_name="album_release_d3585b_idx",
        ),
        migrations.RenameIndex(
            model_name="playhistory",
            new_name="api_playhis_user_id_271f69_idx",
            old_name="play_histor_user_id_2d535d_idx",
        ),
        migrations.RenameIndex(
            model_name="playhistory",
            new_name="api_playhis_track_i_7793f3_idx",
            old_name="play_histor_track_i_e8cb6a_idx",
        ),
        migrations.RenameIndex(
            model_name="playhistory",
            new_name="api_playhis_played__59eb95_idx",
            old_name="play_histor_played__8d598e_idx",
        ),
        migrations.RenameIndex(
            model_name="playlist",
            new_name="api_playlis_title_0da375_idx",
            old_name="playlist_title_f77965_idx",
        ),
        migrations.RenameIndex(
            model_name="playlist",
            new_name="api_playlis_created_ccbe29_idx",
            old_name="playlist_created_1ee2c9_idx",
        ),
        migrations.RenameIndex(
            model_name="track",
            new_name="api_track_title_1d65fe_idx",
            old_name="track_title_63255f_idx",
        ),
        migrations.RenameIndex(
            model_name="track",
            new_name="api_track_play_co_290988_idx",
            old_name="track_play_co_13ec9b_idx",
        ),
        migrations.RenameIndex(
            model_name="track",
            new_name="api_track_release_56f1f1_idx",
            old_name="track_release_80dde6_idx",
        ),
        migrations.AddIndex(
            model_name="genre",
            index=models.Index(fields=["name"], name="api_genre_name_01c28c_idx"),
        ),
        migrations.AddIndex(
            model_name="library",
            index=models.Index(fields=["user"], name="api_library_user_id_c8709a_idx"),
        ),
        migrations.AlterModelTable(
            name="album",
            table=None,
        ),
        migrations.AlterModelTable(
            name="artist",
            table=None,
        ),
        migrations.AlterModelTable(
            name="genre",
            table=None,
        ),
        migrations.AlterModelTable(
            name="library",
            table=None,
        ),
        migrations.AlterModelTable(
            name="playhistory",
            table=None,
        ),
        migrations.AlterModelTable(
            name="playlist",
            table=None,
        ),
        migrations.AlterModelTable(
            name="track",
            table=None,
        ),
    ]
