import json
from playsound import playsound

Curlatitude = 
Curlongitude = 

radius = input_Km / 85.39

with open("Baghramyan_Avn_AUA.json.json") as data_file:
    Destination = json.load(data_file)


latitude= float(Destination["lat"])
longitude = float(Destination["long"])

if ( ( ( (Curlatitude - latitude)**2 ) + ( (Curlongitude - longitude)**2) ) <= radius**2 ):
    playsound('land on the horizon.mp3')
