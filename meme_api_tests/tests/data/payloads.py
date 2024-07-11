create_meme: dict = {
    "text": "Bad memory PyCharm",
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


get_token: dict = {
    "name": "Evgen"
}


def update_payloads(meme_id=None) -> list[dict]:
    return [
        {
            "id": meme_id,
            "text": "Bad memory PyCharm update",
            "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
            "tags": ["it", "fun", ["meme", "pycharm"]],
            "info": {
                "title": "it meme pycharm update",
                "type": "img update"
            }
        },
        {
            "id": meme_id,
            "text": "BAD MEMORY PYCHARM UPDATE",
            "url": "HTTPS://PIKABU.RU/STORY/VOT_TAK_NOVOSTI_9141882PYCHARM",
            "tags": ['IT', 'FUN', ['MEME', 'PYCHARM']],
            "info": {
                "title": "IT MEME PYCHARM UPDATE",
                "type": "IMG UPDATE"
            }
        },
        {
            "id": meme_id,
            "text": "Плохая память PyCharm",
            "url": "https://pikabu.ru/story/vot_tak_novosti_9141882PyCharm",
            "tags": ['айт', 'смешно', ['мем', 'pycharm']],
            "info": {
                "title": "айт мем pycharm",
                "type": "img"
            }
        }
    ]


payload_ids: list = ['lowercase', 'uppercase', 'rus']
