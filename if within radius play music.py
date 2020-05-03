import json
from playsound import playsound

Curlatitude = 40.1974
Curlongitude = 44.5050
radius = 0.5 / 85.39

def get_des_info():
    with open("Baghramyan_Avn_AUA.json") as data_file:
        Destination = json.load(data_file)

    return Destination

def des_to_coordinates(des):
    latitude = float(des["lat"])
    longitude = float(des["long"])

    return latitude, longitude

def check_if_in_radius(lat, long):
    if ( ( ( (Curlatitude - lat)**2 ) + ( (Curlongitude - long)**2) ) <= radius**2 ):
        playsound('land on the horizon.mp3')

def main():
    my_des = get_des_info()

    coordinate= des_to_coordinates(my_des)
    lat = coordinate[0]
    long = (coordinate[1])

    check_if_in_radius(lat,long)

main()
