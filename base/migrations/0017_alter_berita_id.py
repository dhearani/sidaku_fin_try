# Generated by Django 4.1.6 on 2023-03-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_berita_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
