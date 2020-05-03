import requests
import time
from playsound import playsound
import folium
import webbrowser
import os
import json


def question_1():
    while True:
        Choice_1 = input("""
        What do you want to do?

        1) WAKE ME UP!
        2) History settings
        3) music settings

    (type the number that corresponds to your choice)
    """)
        if str(Choice_1).isalpha() == True or str(Choice_1) == "":
            print('Please answer with 1,2 or 3')
        elif int(Choice_1) in (1, 2, 3):
            return Choice_1
        else:
            print('Please answer with 1,2 or 3')


def question_1_1():
    while True:
        Choice_1_1 = (input("""
        Choose your destination
        1) Bus Station
        2) History
        3) Choose your own destination

                """))
        if str(Choice_1_1).isalpha() == True or str(Choice_1_1) == "":
            print('Please answer with 1,2 or 3')
        elif int(Choice_1_1) in (1, 2, 3):
            return Choice_1_1
        else:
            print('Please answer with 1,2 or 3')


def question_1_1_1():
    while True:
        Choice_1_1_1 = (input("""
    you will be shown a map with the available stations, please click the desired station and input the code that corresponds to it"
    would you like to proceed? [y/n]"""))
        Fl = Choice_1_1_1[0].lower()
        if Choice_1_1_1 == '' or not Fl in ['y', 'n']:
            print('Please answer with yes or no!')
        else:
            break

    if Fl == 'y':
        f = open('map.html')
        webbrowser.open_new_tab('map.html')
        input("please type in the code")

    if Fl == 'n':
        main()


def question_1_1_2():
    while True:
        if os.stat("History.json").st_size == 0:
            print("your history is empty")
        else:
            with open("History.json") as data_file:
                Destination = json.load(data_file)
                for item in Destination["coordinates"]:
                    print(item["name"])
                Chosen_history = input("""
    Please type the wanted destination
    """)
        if str(Chosen_history) in item["name"]:
            destination = item[str(Chosen_history)]
            return destination
        else:
            n = input("cannot identify, press y to try again or press n to go back")
            if n == "n":
                main()


def executeSomething():
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    location = data['loc'].split(',')
    Curlatitude = float(location[0])
    Curlongitude = float(location[1])

    print("Current Latitude : ", Curlatitude)
    print("Current Longitude : ", Curlongitude)

    # remove_prints

    time.sleep(1)

    return Curlatitude, Curlongitude


def get_des_info():
    with open("Baghramyan_Avn_AUA.json") as data_file:
        Destination = json.load(data_file)

    return Destination


def des_to_coordinates(des):
    latitude = float(des["lat"])
    longitude = float(des["long"])

    return latitude, longitude


def check_if_in_radius(Curlatitude, Curlongitude, lat, long, radius):
    if ((((Curlatitude - lat) ** 2) + ((Curlongitude - long) ** 2)) <= radius ** 2):
        playsound('land on the horizon.mp3')


def create_map(Destination):
    m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)
    m.add_child(folium.LatLngPopup())
    with open("Stations.json") as f:
        Station = json.load(f)

    folium.Circle(radius=500, location = Destination, color='green').add_to(m)
    with open("Stations.json") as data_file:
        markers = json.load(data_file)
    for i in markers.items():
        folium.Marker(location=i[1], popup=i[0]).add_to(m)
        print(i)
    m.save('map.html')


def main():
    radius = 0.5 / 85.39

    choice_1 = question_1()
    print(choice_1)

    if int(choice_1) == 1:
        choice_1_1 = question_1_1()
        print(choice_1_1)

        if int(choice_1_1) == 1:
            choice_1_1_1 = question_1_1_1()

        if int(choice_1_1) == 2:
            choice_1_1_2 = question_1_1_2()
            my_des = choice_1_1_2

            coordinate = des_to_coordinates(my_des)
            lat = coordinate[0]
            long = coordinate[1]
            Destination = [lat,long]

            create_map(Destination)

            f = open('map.html')
            webbrowser.open_new_tab('map.html')
            while True:
                proceed = input("proceed with project:WakeUp Call? [y/n]")
                Fl = proceed[0].lower()
                if proceed == '' or not Fl in ['y', 'n']:
                    print('Please answer with yes or no!')
                else:
                    break
            if Fl == 'y':
                Curlatitude = 40.192847
                Curlongitude = 44.499548

                check_if_in_radius(Curlatitude, Curlongitude, lat, long, radius)
                print(my_des)

            if Fl == 'n':
                main()






    #my_des = get_des_info()

    #coordinate = des_to_coordinates(my_des)
    #lat = coordinate[0]
    #long = coordinate[1]

    #check_if_in_radius(Curlatitude, Curlongitude, lat, long, radius)


#create_map()

while True:
    main()