# Generated by Django 4.1.6 on 2023-03-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_akun_email_alter_akun_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='nik',
            field=models.CharField(max_length=16),
        ),
    ]
