from django import forms

from fileSystem.models import CSVFile

import os
import humanize


class CSVUploadForm(forms.Form):
    # Только 1 поле, для выбора файла
    csv_file = forms.FileField(label="", required=True)

    def clean_csv_file(self):  # Проверка файла на то, что он csv
        csv_file = self.cleaned_data.get('csv_file')
        if csv_file:
            _, file_extension = os.path.splitext(csv_file.name)
            if file_extension.lower() != '.csv':
                raise forms.ValidationError('Выберите файл с расширением .csv')
        return csv_file


class CSVPageForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ['name']

    def get_id_value(self):
        # Получите значение поля size из объекта instance
        return self.instance.pk

    def get_size_value(self):
        # Получите значение поля size из объекта instance
        return humanize.naturalsize(self.instance.size)

    def get_row_count_value(self):
        # Получите значение поля row_count из объекта instance
        return self.instance.row_count

    def get_uploaded_at_value(self):
        # Получите значение поля uploaded_at из объекта instance
        return self.instance.uploaded_at
