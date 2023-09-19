from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone

import os


class CSVFile(models.Model):  # основная таблица в БД
    name = models.CharField(verbose_name="Название", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to='csv_files/')
    size = models.IntegerField(verbose_name="Размер", default=0)
    row_count = models.IntegerField(verbose_name="Количество строк", default=0)
    uploaded_at = models.DateTimeField(
        verbose_name="Дата загрузки", default=timezone.now)

    def __str__(self):
        return self.name


# дополнительная обработка на удаление файлов, при удалении записи
@receiver(post_delete, sender=CSVFile)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
