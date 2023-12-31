# Generated by Django 4.2.6 on 2023-10-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0002_alter_contentmovie_movie_alter_season_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentseries',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='contentseries',
            name='series',
        ),
        migrations.AddField(
            model_name='movie',
            name='creator',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='content_creator.contentcreator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='creator',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='content_creator.contentcreator'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContentMovie',
        ),
        migrations.DeleteModel(
            name='ContentSeries',
        ),
    ]
