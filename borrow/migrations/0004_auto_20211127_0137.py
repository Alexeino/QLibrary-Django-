# Generated by Django 3.2.9 on 2021-11-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0003_alter_borroweditem_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='borroweditem',
            name='book_returend_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borroweditem',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
