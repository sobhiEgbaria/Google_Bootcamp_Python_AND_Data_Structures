# import requests


# # def translate(text):
# #     url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
# #     payload = {"q": {text}, "target": "he", "source": "en"}
# #     headers = {
# #         "content-type": "application/x-www-form-urlencoded",
# #         "Accept-Encoding": "application/gzip",
# #         "X-RapidAPI-Key": "4b4c51d946msh6a0409856f3f3d9p13c2abjsn279379cc61c2",
# #         "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
# #     }

# #     response = requests.post(url, data=payload, headers=headers)
# #     res = response.json()

# #     return res["data"]["translations"][0]["translatedText"]


# def Nearby_Search():
#     url = (
#         f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=suhsi&location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&key="
#         "AIzaSyDMkqVQHgWrFbOOvWZcHK6QnV_yFd_jMZc"
#         ""
#     )
#     res = requests.get(url).json()
#     result_details = {}
#     for i in res["results"]:
#         result_details[i["name"]] = {
#             "name": i["name"],
#             "location": i["geometry"]["location"],
#             "photos": i["photos"][0]["photo_reference"],
#             "place_id": i["place_id"],
#         }

#     print(result_details)


# Nearby_Search()
