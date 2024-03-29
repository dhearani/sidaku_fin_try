# Generated by Django 4.1.6 on 2023-05-24 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_album_track_delete_combinedmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tracks',
        ),
        migrations.AlterField(
            model_name='album',
            name='track',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_track', to='base.track'),
        ),
    ]
