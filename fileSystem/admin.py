from django.contrib import admin

# Register your models here.
from .models import CSVFile

admin.site.site_header = "Администрация Москвы"


admin.site.register(CSVFile)
