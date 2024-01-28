# Команды
## Создание миграций 
```python
python3 manage.py makemigrations project
python3 manage.py migrate
```

## Авторизация по токену
1. Входим в аккаунт
2. Токен полученный при успешной авторизации сохраняем
3. Запрос с сохраненным токеном отправляем на нужный маршрут
Токен отправляется в заголовке {"Authorization": "Token токен"}