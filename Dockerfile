# Используем базовый образ Python
FROM python:3.10

# Установка переменной окружения для указания, что мы работаем в режиме разработки
ENV DEBUG=True

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование зависимостей проекта (файлы requirements.txt) в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование всех файлов проекта в контейнер
COPY . .

# Определение команды для запуска Django-приложения
CMD ["python", "manage.py", "runserver"]