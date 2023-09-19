import django_tables2 as tables
from .models import CSVFile
from django.db.models import F, Func

import humanize


class CSVFileTable(tables.Table):
    name = tables.LinkColumn('fileSystem:table', args=[
                             tables.A('pk')], verbose_name="Название", order_by=('name',))

    # lобавляем колонку с кнопкой удаления
    delete = tables.TemplateColumn(
        template_name='button_delete.html',
        verbose_name='Удалить',
        orderable=False,
    )

    # отдельная сортировка для имени, т.к. они представленны в разном регистре
    def order_name(self, querySet, is_descending):
        querySet = querySet.annotate(
            field_lower=Func(F('name'), function='LOWER')
        ).order_by(('-' if is_descending else '') + 'field_lower')
        return (querySet, True)

    # доп. обработка размера файла для большей читаемости
    def render_size(self, value):
        return humanize.naturalsize(value)

    # доп. обработка даты для большей читаемости
    def render_uploaded_at(self, value):
        _t = humanize.i18n.activate("ru_RU")
        return humanize.naturaltime(value)

    class Meta:
        model = CSVFile
        attrs = {"class": "table table-striped table-bordered"}
        exclude = ('file',)
