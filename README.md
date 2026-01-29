# Avito Parser Bot

Pet-проект для мониторинга новых объявлений на Avito с уведомлениями в Telegram.

## Описание

Парсер отслеживает объявления о продаже квартир на Avito (по умолчанию — 1-комнатные в Туле с фильтром по цене). При появлении новых объявлений отправляет уведомление в Telegram.

## Возможности

- Парсинг Avito через Selenium (headless-режим)
- Уведомления в Telegram о новых объявлениях
- Сохранение истории объявлений в `data.json`
- Нормализация ссылок (игнорирование параметра `?context=`)
- Запуск по расписанию (каждые 10 минут через .bat)

## Требования

- Python 3.8+
- Google Chrome
- ChromeDriver (совместимый с версией Chrome)

## Установка

1. Клонируйте репозиторий или скопируйте проект:

```bash
cd avito_parser_bot
```

2. Создайте виртуальное окружение:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` (скопируйте `.env.example` и заполните значения):

```
TELEGRAM_BOT=your_bot_token
TELEGRAM_ID=your_chat_id
```

**Как получить:**
- **TELEGRAM_BOT** — токен от [@BotFather](https://t.me/BotFather)
- **TELEGRAM_ID** — ID чата (можно узнать через [@userinfobot](https://t.me/userinfobot))

## Настройка

В `config.py` можно изменить:

- `AVITO_URL` — ссылка на страницу с объявлениями (с нужными фильтрами)
- `CITY`, `CATEGORY` — город и категория (используются при формировании URL)

## Использование

### Первый запуск — инициализация

Сохраните текущие объявления без отправки уведомлений:

```bash
python -c "from main import init_read; init_read()"
```

### Мониторинг новых объявлений

Один запуск:

```bash
python main.py
```

### Непрерывный мониторинг (каждые 10 минут)

Запустите `run_parser_loop.bat` или добавьте в `main.py` цикл:

```python
import time
if __name__ == "__main__":
    while True:
        main()
        time.sleep(600)  # 10 минут
```

> **Важно:** Перед первым запуском `main.py` обязательно выполните `init_read()`, иначе все текущие объявления будут отправлены как «новые».

## Структура проекта

```
avito_parser_bot/
├── .env.example    # Шаблон переменных окружения
├── config.py       # Настройки (URL, город, категория)
├── parser.py       # Парсинг Avito через Selenium
├── main.py         # Основная логика (init_read, main)
├── telegram_bot.py  # Отправка уведомлений в Telegram
├── data.json       # Сохранённые ссылки объявлений
├── .env            # Токены (не коммитить!)
├── run_parser_loop.bat  # Запуск в цикле (Windows)
└── requirements.txt
```

## Примечания

- Avito загружает объявления через JavaScript, поэтому используется Selenium, а не requests + BeautifulSoup
- ChromeDriver должен соответствовать версии установленного Chrome
- Для работы в фоне можно использовать Windows Task Scheduler с `run_parser_loop.bat`
- В `run_parser_loop.bat` при необходимости измените путь к папке проекта
