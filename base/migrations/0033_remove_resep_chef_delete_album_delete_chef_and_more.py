# Generated by Django 4.1.6 on 2023-05-29 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_chef_resep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resep',
            name='chef',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Chef',
        ),
        migrations.DeleteModel(
            name='Musisi',
        ),
        migrations.DeleteModel(
            name='Resep',
        ),
    ]
