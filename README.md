# Telegram-бот для выдачи планов тренировок

Этот Telegram-бот, разработанный на основе библиотеки **aiogram** (Python), помогает пользователям получать персонализированные планы тренировок в зависимости от их целей, уровня подготовки и доступного оборудования.

## Особенности

* **Интуитивно понятный интерфейс:** Взаимодействие с ботом осуществляется через команды и inline-клавиатуры, что делает процесс выбора параметров тренировки простым и удобным.
* **Машина состояний (FSM):** Для управления процессом выбора параметров используется машина состояний, обеспечивающая логичную и последовательную навигацию.
* **Гибкая система планов тренировок:** Бот может быть легко расширен для добавления новых планов тренировок и критериев их выбора.
* **Конфигурация через `.env`:** Токен бота хранится в файле `.env`, что обеспечивает безопасность и удобство управления конфигурацией.

## Предварительные требования

* **Python 3.7+**
* Установленные библиотеки:
    ```bash
    pip install aiogram python-dotenv
    ```
* **Токен Telegram-бота:** Получите токен нового бота у [BotFather](https://t.me/BotFather) в Telegram.

## Установка и запуск

1.  **Клонируйте репозиторий (если применимо):**
    ```bash
    git clone <ссылка_на_ваш_репозиторий>
    cd <название_репозитория>
    ```

2.  **Создайте файл `.env`:**
    В корневом каталоге проекта создайте файл с именем `.env` и добавьте туда токен вашего бота:
    ```
    BOT_TOKEN=YOUR_BOT_TOKEN
    ```
    Замените `YOUR_BOT_TOKEN` на фактический токен вашего бота.

3.  **Установите необходимые библиотеки:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Если у вас есть файл `requirements.txt`)*

4.  **Запустите бота:**
    ```bash
    python main.py
    ```

После запуска бот будет готов принимать команды в Telegram. Найдите своего бота по его имени пользователя и отправьте команду `/start`.

## Клавиатуры

Inline-клавиатуры для выбора цели, уровня подготовки и доступного оборудования определены в файле `keyboards/inline.py`. Вы можете добавлять новые варианты выбора, редактируя этот файл.

## Обработчики

Файл `handlers.py` содержит обработчики для различных событий, таких как команда `/start` и нажатия на кнопки inline-клавиатур. Здесь реализована логика взаимодействия с пользователем и переходы между состояниями.

## Зависимости

Основные зависимости проекта перечислены ниже:

* **aiogram:** Асинхронная библиотека для создания Telegram-ботов на Python.
* **python-dotenv:** Библиотека для загрузки переменных окружения из файла `.env`.

Вы можете создать файл `requirements.txt` со следующим содержимым:

aiogram
python-dotenv


и установить зависимости с помощью команды `pip install -r requirements.txt`.
