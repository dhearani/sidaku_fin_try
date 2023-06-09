# Generated by Django 4.1.6 on 2023-03-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_akun_id_alter_paparan_id_alter_produkhukum_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkhukum',
            name='kategori',
            field=models.CharField(choices=[('Undang-Undang', 'Undang-Undang'), ('Perancangan Undang-Undang', 'Perancangan Undang-Undang'), ('Peraturan Pemerintah', 'Peraturan Pemerintah'), ('Peraturan Presiden', 'Peraturan Presiden'), ('Keputusan dan Intruksi Presiden', 'Keputusan dan Intruksi Presiden'), ('Peraturan Menteri', 'Peraturan Menteri'), ('Keputusan Menteri', 'Keputusan Menteri'), ('Keputusan Deputi', 'Keputusan Deputi'), ('Peraturan Terkait', 'Peraturan Terkait'), ('Petunjuk Pelaksanaan', 'Petunjuk Pelaksanaan'), ('Surat Edaran', 'Surat Edaran')], max_length=255),
        ),
    ]