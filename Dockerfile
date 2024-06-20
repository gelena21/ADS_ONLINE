# Используйте конкретную версию Python для лучшей предсказуемости
FROM python:3.10-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файл с зависимостями в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте оставшиеся файлы приложения в контейнер
COPY . .

# Команда по умолчанию для запуска приложения
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
