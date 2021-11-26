# Generated by Django 3.2.9 on 2021-11-24 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookProxy',
            fields=[
            ],
            options={
                'verbose_name': '',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('books.book',),
        ),
        migrations.RenameField(
            model_name='book',
            old_name='on_board_timestamp',
            new_name='active_timestamp',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='on_board',
            new_name='is_active',
        ),
    ]
