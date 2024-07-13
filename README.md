# Проект автотестов для API мемов

## Описание проекта

## Описание проекта

Этот проект представляет собой набор автоматизированных тестов для тестирования API, которое содержит объекты с мемами. Проект разработан для обеспечения качества и надежности API, предоставляющего доступ к базе данных мемов. Автотесты написаны на языке Python с использованием фреймворка `pytest` и библиотеки `requests`.

Для генерации отчетов о тестировании используется `Allure`, который позволяет создавать подробные и наглядные отчеты. 

Для валидации данных используется библиотека `Pydantic`, которая обеспечивает строгую типизацию и проверку данных, что помогает предотвратить ошибки на этапе валидации.

Данный проект был выполнен в рамках домашнего задания из практического курса по автоматизации тестирования Web приложений [okulik.by](http://okulik.by).
<br>
<br>

## Структура проекта

Проект имеет следующую структуру:

```
root
│
├── meme_api_tests
| |
| ├── endpoints/
| | ├── init.py # Инициализация модуля endpoints
| | ├── base_api.py # Базовый класс для работы с API
| | ├── delete_meme.py # Эндпоинт для удаления мема
| | ├── get_all_meme.py # Эндпоинт для получения всех мемов
| | ├── get_check_token.py # Эндпоинт для проверки токена
| | ├── get_single_meme.py # Эндпоинт для получения одного мема
| | ├── post_add_meme.py # Эндпоинт для добавления нового мема
| | ├── post_authorize.py # Эндпоинт для авторизации пользователя
| | ├── put_upd_meme.py # Эндпоинт для обновления мема
| | └── schemas.py # Схемы для валидации данных
| |
| ├── tests/
| | ├── data/
| | | ├── init.py # Инициализация модуля data
| | | └── payloads.py # Тестовые данные и payloads
| | └── test_meme_api.py # Тесты для API мемов
| |
| ├── utils/
| | ├── init.py # Инициализация модуля utils
| | └── client.py # Клиент для работы с API
| |
| ├── init.py # Инициализация основного модуля
| └── conftest.py # Конфигурации для pytest
|
├── requirements.txt # Зависимости проекта
├── .gitignore # Файлы и директории, игнорируемые git
├── pytest.ini # Настройки для pytest
└── README.md # Описание проекта
```
<br>

## Установка

Для установки всех необходимых зависимостей, выполните следующую команду:

`bash
pip install -r requirements.txt`


## Запуск тестов
Для запуска всех тестов выполните следующую команду:

`pytest`

Вы также можете запускать отдельные тесты или группы тестов, указав путь к файлу или директории:

`pytest meme_api_tests/tests/test_meme_api.py`

Отдельный тест:

`pytest meme_api_tests/tests/test_meme_api.py::test_create_meme_object`
<br>
<br>

## Генерация отчетов Allure
Для генерации отчетов Allure выполните следующую команду для запуска тестов с сохранением результатов:

`pytest --alluredir=allure-results`

После завершения тестов, для генерации и открытия отчета выполните:

`allure generate --clean
allure open`
<br>
<br>

# Основные функции API

## Авторизация
POST /authorize
* Описание: Авторизация пользователя.
* Параметры:
  * name (string): Имя пользователя.

Пример запроса:

```
{
  "name": "ExampleUser"
}
```

Пример ответа:

```
{
    "token": "Fru71xjhBwL2oyJ",
    "user": "User"
}
```
<br>

## Проверка токена
GET /authorize/<token>
* Описание: Проверка, жив ли токен.

Пример ответа:

`Token is alive. Username is User`
<br>
<br>

## Получение списка всех мемов
GET /meme
* Описание: Получение списка всех мемов.

Пример ответа:

```
{
    "data": [
        {
            "id": 1,
            "info": {
                "colors": [
                    "green",
                    "black",
                    "white"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            },
            "tags": [
                "fun",
                "meme"
            ],
            "text": "some text",
            "updated_by": "user",
            "url": "www.example.com"
        },
        {
            "id": 2,
            "info": {
                "colors": [
                    "green",
                    "red"
                ],
                "objects": [
                    "text",
                    "picture"
                ]
            },
            "tags": [
                "some tag",
                "another tag"
            ],
            "text": "some meme",
            "updated_by": "TestUser",
            "url": "www.example.com"
        }
    ]
}
```
<br>

## Получение одного мема
GET /meme/<id>
* Описание: Получение информации о меме по его ID.

Пример ответа:

```{
    "id": "9",
    "info": {
        "title": "it meme",
        "type": "img"
    },
    "tags": [
        "it",
        "fun",
        [
            "meme"
        ]
    ],
    "text": "Bad memory",
    "updated_by": "User",
    "url": "https://cs12.pikabu.ru/post_img/big/2022/05/26/7/1653560579164255219.jpg"
}
```
<br>

## Добавление нового мема
POST /meme
* Описание: Добавление нового мема.
* Параметры (все обязательны):
  * text (string): Текст мема.
  * url (string): URL изображения мема.
  * tags (array): Теги мема.
  * info (object): Дополнительная информация о меме.

Пример запроса:

```
{
  "text": "Funny Meme",
  "url": "http://example.com/meme.jpg",
  "tags": ["funny", "meme"],
  "info": {"author": "John Doe", "created_at": "2024-07-13"}
}
```

Пример ответа:

```
{
    "id": 31,
    "info": {
        "title": "it meme",
        "type": "img"
    },
    "tags": [
        "it",
        "fun",
        [
            "meme"
        ]
    ],
    "text": "text",
    "updated_by": "User",
    "url": "https://cs15.pikabu.ru/post_img/2024/07/06/6/1720253976117393084.jpg"
}
```
<br>

## Изменение существующего мема
PUT /meme/<id>
* Описание: Обновление информации о меме по его ID.
* Параметры (все обязательны):
  * id (int): ID мема.
  * text (string): Новый текст мема.
  * url (string): Новый URL изображения мема.
  * tags (array): Новые теги мема.
  * info (object): Обновленная информация о меме.

Пример запроса:

```
{
  "id": 1,
  "text": "Updated Meme",
  "url": "http://example.com/updated_meme.jpg",
  "tags": ["updated", "meme"],
  "info": {"author": "John Doe", "updated_at": "2024-07-14"}
}
```

Пример ответа:

```
{
    "id": "9",
    "info": {
        "title": "it meme",
        "type": "img"
    },
    "tags": [
        "it",
        "fun",
        [
            "meme"
        ]
    ],
    "text": "Some text",
    "updated_by": "User",
    "url": "https://cs12.pikabu.ru/post_img/big/2022/05/26/7/1653560579164255219.jpg"
}
```
<br>

## Удаление мема
DELETE /meme/<id>
* Описание: Удаление мема по его ID.

Пример ответа:

`Meme with id 31 successfully deleted`
<br>
<br>

## Вклад
Если вы хотите внести вклад в развитие проекта, пожалуйста, следуйте этим шагам:

1. Форкните репозиторий.
2. Создайте новую ветку: `git checkout -b feature/YourFeature`.
3. Внесите изменения и закоммитьте их: `git commit -am 'Add some feature'`.
4. Отправьте ветку на GitHub: `git push origin feature/YourFeature`.
5. Создайте Pull Request.

Контакты
Если у вас есть вопросы или предложения, вы можете связаться с нами по электронной почте: windwoverine@gmail.com.
