# Generated by Django 4.1.6 on 2023-05-24 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_musician_rename_album_name_album_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]