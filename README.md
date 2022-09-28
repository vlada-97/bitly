# Битовое сокращение URL-адресов

Проект выполняет две основных функции:
- Сокращает ссылки до формата битлинк
- Подсчитывает количество кликов по битлинку

## Как установить
Python3 уже должен быть установлен. Используйте (или , если есть конфликт с Python2) для установки зависимостей: pip pip3
```
pip install -r requirements.txt
```
## Настройка окружения перед запуском программы
При разработки web-приложения или бота мы часто имеем дело с какой-либо секретной информацией, различными токенами и паролями (API-ключами, секретами веб-форм). Cохранять такие переменные в публичном доступе это очень плохая идея.
```python
# Плохая практика. Не делай так.
API_KEY = 'very_secret_password'
```
Именно поэтому, нам потребуется перенная окружения, в которой мы будем хранить наш токен.
Пример правильной конструкции в коде: 
```python
# Вот так можно.
bitly_token = os.getenv('BITLY_TOKEN')
```
В коде есть такая строка `load_dotenv()`. Данная берет файл .env из текущего каталога и настраивает переменные окружения которые прописаны в данном файле. Код считывает переменную окружения BITLY_TOKEN. Пример заполнения файла:
```python
ENV_VAR=VALUE
```
## Примеры запроса в командной строке
Сокращение ссылки:
```
python main.py https://vk.com/
bit.ly/2qiigvW
```
Переходы по ссылке:
```
python main.py bit.ly/2qiigvW
Переходов по ссылке:0
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/)
