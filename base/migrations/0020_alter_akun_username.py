# Generated by Django 4.1.6 on 2023-05-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_produkhukum_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
