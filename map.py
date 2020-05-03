import folium
import json

#generate map in yerevan
m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)

#get lat/long when click on map
m.add_child(folium.LatLngPopup())

with open("Stations.json") as f:
    Station = json.load(f)

    Destination = Station["France Square 1"]


#radius
folium.Circle(radius=500, location = Destination, color='green').add_to(m)

#marker
with open("Stations.json") as data_file:
    markers = json.load(data_file)

for i in markers.items():
    folium.Marker(location=i[1], popup=i[0]).add_to(m)
    print(i)

#save
m.save('map.html')


