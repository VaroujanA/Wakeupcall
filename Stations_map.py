import folium
import json

m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)

m.add_child(folium.LatLngPopup())


with open("Stations.json") as data_file:
    markers = json.load(data_file)

for i in markers.items():
    folium.Marker(location=i[1], popup=i[0]).add_to(m)
    print(i)

m.save('Stations_map.html')