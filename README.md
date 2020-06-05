# Проект CatBot

CatBot - это бот для Telegram, который присилывает пользователю котиков.

## Усановка

1. Клонируйте репозиторий с github
2. Создйте виртуальое окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py` 
5. Впишите в setiings.py переменные:
```
API_KEY = "API-ключ бота"
PROXY_URL = "Адрес прокси"
PROXY_USERNAME = "Логин прокси"
PROXY_PASSWORD = "Пароль прокси"
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```
6. Запустите бота командой `python bot.py`
