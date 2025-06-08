Установка
Клонируйте репозиторий:

bash
git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
cd ваш-репозиторий
Установите зависимости:

bash
pip install -r requirements.txt
Структура проекта
text
.
├── src/
│   ├── __init__.py
│   ├── masks.py        # Функции маскирования карт и счетов
│   ├── processing.py   # Фильтрация и сортировка операций
│   └── widget.py       # Форматирование данных
├── tests/
│   ├── __init__.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── .gitignore
├── requirements.txt
└── README.md
Основные функции
masks.py
get_mask_card_number(card_number): Маскирует номер карты (формат: XXXX XX** **** XXXX)

get_mask_account(account): Маскирует номер счета (формат: **XXXX)

widget.py
mask_account_card(input_str): Автоматически определяет тип данных (карта/счет) и применяет маскировку

get_date(raw_date): Преобразует дату из ISO формата в DD.MM.YYYY

processing.py
filter_by_state(operations, state): Фильтрует операции по статусу (EXECUTED, CANCELED)

sort_by_date(operations, reverse=True): Сортирует операции по дате (по умолчанию - новые сначала)

Тестирование
Запуск тестов
bash
pytest --cov=src --cov-report=html
Просмотр отчета о покрытии
После запуска тестов откройте файл htmlcov/index.html в браузере для просмотра детального