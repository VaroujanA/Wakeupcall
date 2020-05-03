import requests
import time

def executeSomething():

    res = requests.get('https://ipinfo.io/')
    data = res.json()

    location = data['loc'].split(',')
    Curlatitude = location[0]
    Curlongitude = location[1]

    print("Current Latitude : ", Curlatitude)
    print("Current Longitude : ", Curlongitude)

    #remove_prints

    time.sleep(1)

while True:
    executeSomething()

    #input if_within_radius_play_music.py
