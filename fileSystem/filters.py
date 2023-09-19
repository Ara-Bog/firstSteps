import django_filters
from .models import CSVFile


class CSVFileFilter(django_filters.FilterSet):  # Фильтр для таблицы
    # Отдельная фильтрация для даты (фильтрация по времени не доступна в данном решении)
    uploaded_at = django_filters.DateRangeFilter()
    # поле поиска
    name_contains = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Поиск по названию'
    )

    class Meta:
        model = CSVFile
        fields = ['name_contains', 'id', 'size', 'row_count', 'uploaded_at']
