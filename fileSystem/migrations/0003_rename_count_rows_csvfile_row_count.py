# Generated by Django 4.2.5 on 2023-09-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileSystem', '0002_csvfile_count_rows_csvfile_size_csvfilecolumn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csvfile',
            old_name='count_rows',
            new_name='row_count',
        ),
    ]
