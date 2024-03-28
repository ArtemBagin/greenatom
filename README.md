# Тестовое для greenatom

### Инструкция для запуска: 
Создайте .env файл по примеру example.env

Пример запуска:
```
poetry install
cd src/api
poetry run uvicorn app:app --reload
```

### Swagger - http://127.0.0.1:8000/docs