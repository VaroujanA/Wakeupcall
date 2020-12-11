import folium
import json

def update_Stations_json(): #for updating the actual map with stations, write in Stations.json and run this code
    m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)

    m.add_child(folium.LatLngPopup())

    with open("Stations.json") as data_file:
        markers = json.load(data_file)
    code = 0
    for l in markers.items():
        code = code + 1
        folium.Marker(location=l[1], popup='<b>' + l[0] + '</b>' + "\n" + 'code:' + str(code)).add_to(m)
        print(l)

    m.save('Stations_map.html')