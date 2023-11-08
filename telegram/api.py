import requests
import json


def age_of_celb(name):
    api_url = f"https://api.api-ninjas.com/v1/celebrity?name={name}"

    response = requests.get(
        api_url, headers={"X-Api-Key": "K7HUfTzDONfdXWfbw5qAYg==iC2g5EcqOJfP9Yg9"}
    )
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return data[0]["age"]


name = input("enter a celebrity name: ")
print(age_of_celb(name))
