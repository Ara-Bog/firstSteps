from django.shortcuts import render
from django_tables2 import SingleTableView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import CSVFile
from .forms import CSVUploadForm, CSVPageForm
from .filters import CSVFileFilter
from .tables import CSVFileTable

import pandas as pd
import csv

# набор кодировок для открытия файла
ENCODING = ['utf-8', 'ISO-8859-10', 'ANSI',
            'mbcs', 'cp1252', 'cp850', 'UTF-16LE', 'latin1']


class IndexView(SingleTableView):  # Основное представление (главная страница)
    model = CSVFile  # Модель для представления (откуда берутся данные)
    form_class = CSVUploadForm  # Форма для добавления новых файлов
    table_class = CSVFileTable  # Таблица для представления данных
    filter_class = CSVFileFilter  # Фильтрация таблицы
    template_name = "index.html"  # Имя шаблона
    paginate_by = 5  # Количество строк таблицы на страницу

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['filter'] = self.filter
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            # получаем файл пользователя с формы
            csv_file = form.cleaned_data['csv_file']
            obj = CSVFile.objects.create(
                name=csv_file.name, file=csv_file, size=csv_file.size)  # создаем новую запись в БД

            # открываем CSV-файл и подсчитываем строки
            with obj.file.open(mode='r') as csvfile:
                csv_reader = csv.reader(csvfile)
                row_count = sum(1 for _ in csv_reader)

            # сохраняем количество строк в записи
            obj.row_count = row_count
            obj.save()

            return HttpResponseRedirect(reverse("fileSystem:index"))

        files_list = self.model().objects.all()
        table = self.table_class()
        return render(request, self.template_name, {'files_list': files_list, 'form': form, 'open_modal': True, 'table': table})


def tableView(request, pk):  # представление для страницы таблицы
    obj = get_object_or_404(CSVFile, pk=pk)  # получаем текущий объект

    form = CSVPageForm(request.POST or None,
                       request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()

    # попытка чтения файла разными кодировками
    html_table = None, None
    for coding in ENCODING:
        try:
            html_table = pd.read_csv(obj.file, encoding=coding).head(
                50).to_html(justify="center", index_names=False)
            break
        except:
            continue
    else:
        # файл не был прочитан
        html_table = "<h4>Файл не может быть прочитан, измените его кодировку на UTF-8</h4>"

    # выбираем первые 50 объектов и преобразовываем в html
    return render(request, 'table_view.html', {'html_table': html_table, 'form': form})


def deleteView(_, pk):  # удаление файла с базы
    obj = get_object_or_404(CSVFile, pk=pk)
    obj.delete()

    return HttpResponseRedirect(reverse("fileSystem:index"))
