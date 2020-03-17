import requests
import time
import _json

def executeSomething():

    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("City : ", city)

    time.sleep(1)

    return

while True:
    executeSomething()


