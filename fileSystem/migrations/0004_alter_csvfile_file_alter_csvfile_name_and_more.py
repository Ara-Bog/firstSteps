# Generated by Django 4.2.5 on 2023-09-17 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fileSystem', '0003_rename_count_rows_csvfile_row_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='file',
            field=models.FileField(upload_to='csv_files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='row_count',
            field=models.IntegerField(default=0, verbose_name='Количество строк'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='size',
            field=models.IntegerField(default=0, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки'),
        ),
        migrations.DeleteModel(
            name='CSVFileColumn',
        ),
    ]