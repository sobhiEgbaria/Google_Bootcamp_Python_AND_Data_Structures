import requests


# def start():
#     text = input("enter the text:\n>")
#     source = input("enter the source language (the text language)\n>")
#     target = input(
#         "enter the target language (the language you wont to translate to:\n>)"
#     )
#     res = [text, source, target]
#     return res


def translate(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = {"q": {text}, "target": "he", "source": "en"}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b4c51d946msh6a0409856f3f3d9p13c2abjsn279379cc61c2",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()

    return res["data"]["translations"][0]["translatedText"]
