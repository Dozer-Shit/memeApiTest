valid_auth_payload: dict = {
    "name": "valid_user"
}

invalid_auth_payload: dict = {
    "name": "invalid_user",
    "invalid field": "invalid field"
}

get_token: dict = {
    "name": "Evgen"
}
valid_token_response = {
    "token": "valid_token",
    "user": "valid_user"
}


def invalid_payload_name() -> list[dict]:
    return [
        {"name": ""},
        {"name": "a" * 1001},
        {"name": "!@#$%^&*()"}
    ]


invalid_payload_name_ids: list = ['empty', 'long', 'special']

create_meme: dict = {
    "text": "Some valid text",
    "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
    "tags": [
        "it",
        "fun",
        ["meme", "PyCharm"]
    ],
    "info": {
        "title": "it meme PyCharm",
        "type": "img"
    }
}

create_meme_with_an_extra_field: dict = {
    "text": "Bad memory PyCharm",
    "extra_field": "some extra field",
    "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
    "tags": [
        "it",
        "fun",
        ["meme", "PyCharm"]
    ],
    "info": {
        "title": "it meme PyCharm",
        "type": "img"
    }
}


def post_fields_binding_validation_payloads() -> list[dict]:
    return [
        {
            "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
            "tags": ["it", "fun", ["meme", "pycharm"]],
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "text": "some text",
            "tags": ['it', 'fun', ['meme', 'pycharm']],
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "text": "some text",
            "url": "https://cs15.pikabu.ru/post_img/2024/07/06/6/1720253976117393084.jpg",
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "text": "some text",
            "url": "https://cs14.pikabu.ru/post_img/2022/05/06/7/1651837878118526807.jpg",
            "tags": ['it', 'fun', ['meme', 'pycharm']],
        }
    ]


post_fields_binding_validation_payloads_ids: list = ['no text', 'no url', 'no tags', 'no info']


def generate_invalid_data_types_payloads_ids(invalid_values: list, check_int: bool = False) -> list[str]:
    ids = []
    for value in invalid_values:
        if check_int and not isinstance(value, int):
            ids.append(f"text_invalid_{type(value).__name__}")
        if not isinstance(value, str):
            ids.append(f"text_invalid_{type(value).__name__}")
        if not isinstance(value, str):
            ids.append(f"url_invalid_{type(value).__name__}")
        if not isinstance(value, list):
            ids.append(f"tags_invalid_{type(value).__name__}")
        if not isinstance(value, dict):
            ids.append(f"info_invalid_{type(value).__name__}")
    return ids


def post_invalid_data_types_payloads() -> list[dict]:
    invalid_values = [123, "123", True, None, [], {}, (1, 2)]
    test_cases = []

    for value in invalid_values:
        if not isinstance(value, str):
            test_cases.append({
                "text": value,
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": ["it", "fun"],
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, str):
            test_cases.append({
                "text": "some text",
                "url": value,
                "tags": ["it", "fun"],
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, list):
            test_cases.append({
                "text": "some text",
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": value,
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, dict):
            test_cases.append({
                "text": "some text",
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": ["it", "fun"],
                "info": value
            })
    return test_cases


def post_invalid_data_types_payloads_ids() -> list[str]:
    invalid_values = [123, "123", True, None, [], {}, (1, 2)]
    return generate_invalid_data_types_payloads_ids(invalid_values)


def valid_update_payload(meme_id) -> dict:
    return {
        "id": meme_id,
        "text": "Valid text PyCharm update",
        "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
        "tags": ["it", "fun", ["meme", "pycharm"]],
        "info": {
            "title": "it meme pycharm update",
            "type": "img update"
        }
    }


def update_params_payloads(meme_id=None) -> list[dict]:
    return [
        {
            "id": meme_id,
            "text": "Valid text PyCharm update",
            "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
            "tags": ["it", "fun", ["meme", "pycharm"]],
            "info": {
                "title": "it meme pycharm update",
                "type": "img update"
            }
        },
        {
            "id": meme_id,
            "text": "VALID TEXT PYCHARM UPDATE",
            "url": "HTTPS://PIKABU.RU/STORY/VOT_TAK_NOVOSTI_9141882PYCHARM",
            "tags": ['IT', 'FUN', ['MEME', 'PYCHARM']],
            "info": {
                "title": "IT MEME PYCHARM UPDATE",
                "type": "IMG UPDATE"
            }
        },
        {
            "id": meme_id,
            "text": "Правильный текст PyCharm",
            "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
            "tags": ['айт', 'смешно', ['мем', 'pycharm']],
            "info": {
                "title": "айт мем pycharm",
                "type": "img"
            }
        }
    ]


payload_update_ids: list = ['lowercase', 'uppercase', 'rus']


def put_fields_binding_validation_payloads(meme_id=None) -> list[dict]:
    return [
        {
            "text": "some text",
            "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
            "tags": ["it", "fun", ["meme", "pycharm"]],
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "id": meme_id,
            "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
            "tags": ["it", "fun", ["meme", "pycharm"]],
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "id": meme_id,
            "text": "some text",
            "tags": ['it', 'fun', ['meme', 'pycharm']],
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "id": meme_id,
            "text": "some text",
            "url": "https://cs15.pikabu.ru/post_img/2024/07/06/6/1720253976117393084.jpg",
            "info": {
                "title": "it meme pycharm post",
                "type": "img post"
            }
        },
        {
            "id": meme_id,
            "text": "some text",
            "url": "https://cs14.pikabu.ru/post_img/2022/05/06/7/1651837878118526807.jpg",
            "tags": ['it', 'fun', ['meme', 'pycharm']],
        }
    ]


put_fields_binding_validation_payloads_ids: list = ['no id', 'no text', 'no url', 'no tags', 'no info']


def put_invalid_data_types_payloads() -> list[dict]:
    invalid_values = [123, "123", True, None, [], {}, (1, 2)]
    test_cases = []

    for value in invalid_values:
        if not isinstance(value, int):
            test_cases.append({
                "id": value,
                "text": "some text",
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": ["it", "fun"],
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, str):
            test_cases.append({
                "id": 123,
                "text": value,
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": ["it", "fun"],
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, str):
            test_cases.append({
                "id": 123,
                "text": "some text",
                "url": value,
                "tags": ["it", "fun"],
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, list):
            test_cases.append({
                "id": 123,
                "text": "some text",
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": value,
                "info": {"title": "it meme pycharm post", "type": "img post"}
            })
        if not isinstance(value, dict):
            test_cases.append({
                "id": 123,
                "text": "some text",
                "url": "https://cs15.pikabu.ru/post_img/2024/06/28/6/1719563098181370592.jpg",
                "tags": ["it", "fun"],
                "info": value
            })
    return test_cases


def put_invalid_data_types_payloads_ids() -> list[str]:
    invalid_values = [123, "123", True, None, [], {}, (1, 2)]
    return generate_invalid_data_types_payloads_ids(invalid_values, check_int=True)
