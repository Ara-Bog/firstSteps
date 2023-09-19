from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "fileSystem"

# всего 2 страницы, главная и выбранной таблицы
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.tableView, name='table'),
    path('delete/<int:pk>/', views.deleteView, name='delete_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
