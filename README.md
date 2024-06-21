# Проект Ads Online

## Обзор

Ads Online — это приложение на Django, которое позволяет пользователям создавать и управлять объявлениями. Приложение поддерживает аутентификацию пользователей с использованием JWT, отзывы к объявлениям и предоставляет фильтруемый и пагинируемый список объявлений.

## Функциональные возможности

- Регистрация и аутентификация пользователей (с использованием JWT)
- Создание, обновление и удаление объявлений
- Добавление отзывов к объявлениям
- Фильтрация и пагинация объявлений
- Документация API с помощью Swagger

## Технологии

- Django
- Django REST Framework
- PostgreSQL
- Docker
- Redis
- djoser (для управления пользователями)
- drf_yasg (для документации API)

## Требования

- Docker
- Docker Compose

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/yourusername/ads_online.git
    cd ads_online
    ```

2. **Создайте виртуальное окружение и активируйте его:**

    ```bash
    python -m venv env
    source env/bin/activate  # Для Windows используйте `env\Scripts\activate`
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Создайте файл `.env` со следующим содержимым:**

    ```env
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=ads_online
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=2182
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    SECRET_KEY=your_secret_key_here
    ```

## Запуск проекта

1. **Соберите и запустите контейнеры Docker:**

    ```bash
    docker-compose down  # Опционально: остановить все работающие контейнеры
    docker-compose up --build
    ```

2. **Выполните миграции:**

    ```bash
    docker-compose exec app python manage.py makemigrations
    docker-compose exec app python manage.py migrate
    ```

3. **Создайте суперпользователя:**

    ```bash
    docker-compose exec app python manage.py createsuperuser
    ```

4. **Доступ к приложению:**

    - API будет доступно по адресу `http://localhost:8000/api/ads_online/`
    - Админ-панель будет доступна по адресу `http://localhost:8000/admin/`
    - Документация Swagger будет доступна по адресу `http://localhost:8000/swagger/`

## Структура проекта

```plaintext
ads_online/
│
├── ads_online/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── permissions.py
│
├── ads_online/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── filters.py
│   └── paginations.py
│
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


API Эндпоинты

Пользователи:

POST /api/users/ - Создать нового пользователя
POST /api/token/ - Получить JWT токен
GET /api/users/ - Список всех пользователей (требуется админ)
GET /api/users/{id}/ - Получить пользователя по ID (требуется админ)
Объявления:

GET /api/ads_online/ads/ - Список всех объявлений
POST /api/ads_online/ads/ - Создать новое объявление
GET /api/ads_online/ads/{id}/ - Получить объявление по ID
PUT /api/ads_online/ads/{id}/ - Обновить объявление по ID
DELETE /api/ads_online/ads/{id}/ - Удалить объявление по ID
Отзывы:

GET /api/ads_online/reviews/ - Список всех отзывов
POST /api/ads_online/reviews/ - Создать новый отзыв
GET /api/ads_online/reviews/{id}/ - Получить отзыв по ID
PUT /api/ads_online/reviews/{id}/ - Обновить отзыв по ID
DELETE /api/ads_online/reviews/{id}/ - Удалить отзыв по ID
Участие в разработке

Форкните репозиторий
Создайте новую ветку (git checkout -b feature-branch)
Закоммитьте свои изменения (git commit -m 'Добавить новую функцию')
Запушьте изменения (git push origin feature-branch)
Создайте новый Pull Request
