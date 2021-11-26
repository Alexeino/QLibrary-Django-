# Generated by Django 3.2.9 on 2021-11-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0003_alter_genre_active_timestamp'),
        ('series', '0003_series_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='genres.genre'),
        ),
    ]
