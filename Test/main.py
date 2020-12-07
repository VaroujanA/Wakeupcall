import requests
import time
from playsound import playsound
import webbrowser
import os
import json
from Test.Costum_Hashmap import HashMap
from Test.Linked_List import SingleLinkedList
from Test.directory import give_name_find_path
from Test.Queue import Queue
import folium

def dict_to_hashmap(dict_to_be_transformed):
    hashmap = HashMap()
    code = 0
    for key, value in dict_to_be_transformed.items():
        name = key
        lat = value[0]
        long = value[1]
        code = code + 1
        hashmap.put(str(code), {"name": name,
                                "lat": lat,
                                "long": long,
                                "code": code})
    return hashmap

def show_marker(code):
    info = find_info(code)
    Destination = [info[2], info[3]]
    m = folium.Map(location= Destination, zoom_start=15)
    m.add_child(folium.LatLngPopup())

    folium.Circle(radius=500, location=Destination, color='green').add_to(m)
    folium.Marker(location= Destination, popup='<b>Destination</b>'+'\n'+'<i>'+info[0]).add_to(m)
    m.save('map.html')

def find_info(code):
    raw = hash.get(code)
    name = raw["name"]
    code = float(raw["code"])
    latitude = float(raw["lat"])
    longitude = float(raw["long"])
    return name, code, latitude, longitude

def check_numb_1234(choice):
    if str(choice).isalpha() is True or str(choice) == "":
        print("""
    Please answer with 1, 2, 3, 4
    """)
        return None
    elif int(choice) in (1, 2, 3, 4):
        return choice
    else:
        print("""
    Please answer with 1, 2, 3, 4
    """)
        return None


def check_numb_123(choice):
    if str(choice).isalpha() is True or str(choice) == "":
        print("""
    Please answer with 1, 2, 3
    """)
        return None
    elif int(choice) in (1, 2, 3):
        return choice
    else:
        print("""
    Please answer with 1, 2, 3
    """)
        return None


def check_yes_no(choice):
    if choice == '':
        print("""
    Please answer with yes or no!
    """)
        return None
    fl = choice[0].lower()
    if fl not in ['y', 'n']:
        print("""
    Please answer with yes or no!
    """)
        return None
    else:
        return fl


def question_1():
    while True:
        choice_1 = input("""
        What do you want to do?

        1) WAKE ME UP!
        2) History settings (not available)
        3) music settings   (now available!)

    (type the number that corresponds to your choice)
    """)
        choice = check_numb_123(choice_1)
        if choice is None:
            pass
        else:
            return choice


def question_1_1():
    while True:
        choice_1_1 = (input("""
        Choose your destination

        1) Bus Station
        2) Use history (WIP)
        3) Choose your own destination (WIP)

        4) back
        """))
        choice = check_numb_1234(choice_1_1)
        if choice is None:
            pass
        else:
            return choice


def question_1_3():
    while True:
        choice_1_3 = (input("""
    1) choose music
    2) music history
    3) queue
    4) go back
    """))
        choice = check_numb_1234(choice_1_3)
        if choice is None:
            pass
        else:
            return choice


def question_1_3_1(): # choose player
    while True:
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        for e in dictionary["music"]:
            s.insertLast(e)
        print()
        s.display_items()
        choice = s.display_nth_item_and_return()
        with open("player.json") as data:
            dict = json.load(data)
        dict["music"] = str(choice)
        with open("player.json", "w") as data:
            json.dump(dict, data, indent=2)
        s.remove_all()
        return


def question_1_3_2():
    while True:
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        for e in dictionary["music"]:
            s.insertLast(e)
        print()
        s.display_items()
        s.remove_all()
        choice_1_3_2 = (input("""
    1) import music
    2) remove music 
    3) import music folder
    4) go back
    """))
        choice = check_numb_1234(choice_1_3_2)
        if choice is None:
            pass
        else:
            return choice


def question_1_3_2_1(): # save choice
    folder = choose_folder_and_convert_all_music_to_list_and_json()
    if folder is False:
        question_1_3_2_1()
    else:
        choice = str(display_nth_item_folder(folder))
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        music = SingleLinkedList()
        for e in dictionary["music"]:
            music.insertLast(e)
        music.insertLast(choice)
        with open('music_library.json', "w") as file:
            json.dump(music.to_json(), file, indent=2)
        music.remove_all()
        s.remove_all()


def question_1_3_2_2(): # remove choice
    with open("music_library.json") as data_file:
        dictionary = json.load(data_file)
    for e in dictionary["music"]:
        s.insertLast(e)
    print()
    s.display_items()
    choice = str(s.display_nth_item_and_return())
    s.remove(choice)
    print()
    with open('music_library.json', "w") as file:
        json.dump(s.to_json(), file, indent=2)
    s.remove_all()


def question_1_3_2_3(): # save all
    choose_folder_and_convert_all_music_to_list_and_json()
    with open("music_library.json") as data_file:
        dictionary = json.load(data_file)
    music = SingleLinkedList()
    for e in dictionary["music"]:
        music.insertLast(e)
    cur_node = s.first
    while cur_node is not None:
        music.insertLast(cur_node.data)
        cur_node = cur_node.next
    with open('music_library.json', "w") as file:
        json.dump(music.to_json(), file, indent=2)
    music.remove_all()
    s.remove_all()

def question_1_3_3():
    q.display()
    while True:
        choice_1_3 = (input("""
    1) create queue 
    2) stop Queue
    3) go back
    """))
        choice = check_numb_123(choice_1_3)
        if choice is None:
            pass
        else:
            return choice

def question_1_3_3_1():
    with open("music_library.json") as data_file:
        dictionary = json.load(data_file)
    for e in dictionary["music"]:
        q.enqueue(e)

def question_1_3_3_2():
    while q.size != 0:
        q.dequeue()

def question_1_1_1():
    while True:
        choice_1_1_1 = (input("""
    you will be shown a map with the available stations, please click the desired station and input the code that 
    corresponds to it"
    - would you like to proceed? [y/n]"""))
        choice = check_yes_no(choice_1_1_1)
        if choice is None:
            pass
        elif choice == 'y':
            webbrowser.open_new_tab('Stations_map.html')
            code = str(input("""
    please type in the numerical code"""))
            test = hash.get(code)
            if test is None:
                n = input("""
    cannot identify, press y to try again or press n to go back""")
                if n == "n":
                    main()
            else:
                return code
        if choice == 'n':
            main()


def execute_gps():
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    location = data['loc'].split(',')
    curlatitude = float(location[0])
    curlongitude = float(location[1])

    print("Current Latitude : ", curlatitude)
    print("Current Longitude : ", curlongitude)

    time.sleep(1)

    return curlatitude, curlongitude


def check_for_Queue(curlatitude, curlongitude, lat, long, radius):
    if int(q.size) == 0:
        return
    else:
        complete = "c"
        if (((curlatitude - lat) ** 2) + ((curlongitude - long) ** 2)) <= radius ** 2:
            name = q.first().data
            music = give_name_find_path(name)
            playsound(music)
            q.dequeue()
        return complete

def check_if_in_radius(curlatitude, curlongitude, lat, long, radius):
    complete = "c"
    with open("player.json") as data_file:
        dictionary = json.load(data_file)
    if (((curlatitude - lat) ** 2) + ((curlongitude - long) ** 2)) <= radius ** 2:
        if dictionary == {}:
            playsound('land on the horizon.mp3')
        else:
            name = str(dictionary["music"])
            music = give_name_find_path(name)
            playsound(music)
        return complete


def open_map_and_proceed(code, radius):
    webbrowser.open_new_tab('map.html')
    while True:
        proceed = input("""
        proceed with project:WakeUp Call? [y/n]""")
        choice = check_yes_no(proceed)
        if choice is None:
            pass
        if choice == 'y':
            while True:
                # gps_cordinate = execute_gps()
                cur_lat = 40.1925
                cur_long = 44.5002

                info = find_info(code)
                lat = info[2]
                long = info[3]
                complete_1 = check_for_Queue(cur_lat, cur_long, lat, long, radius)
                if complete_1 == "c":
                    break
                else:
                    complete_2 = check_if_in_radius(cur_lat, cur_long, lat, long, radius)
                    if complete_2 == "c":
                        break

            break
        if choice == 'n':
            main()


def work(my_des):
    radius = 0.5 / 85.39
    show_marker(my_des)
    open_map_and_proceed(my_des, radius)
    end()


def end():
    print("""
    Finitto! thanks for using WakeUp Call!
    """)

def choose_folder_and_convert_all_music_to_list_and_json():
    n = input("insert folder name")
    if n == '':
        print("folder does not exists, try again")
        return False
    if os.path.isdir("C:/Users/varou/PycharmProjects/Wakeupcall-master/Test/"+str(n)+"/") is True:
        paths = os.listdir(n)
        music_key = {}
        music_list = []
        for path in paths:
            if path.endswith(".mp3"):
                music_list.append(path)
        music_key["music"] = music_list
        for e in music_key["music"]:
            s.insertLast(e)
        s.display_items()
        return n
    else:
        print("folder does not exists, try again")
        return False

def display_nth_item_folder(folder):
    n = input("which do u want to select?")
    if s.size != 0:
        current_node = s.first
        for i in range(int(n)-1):
            current_node = current_node.next
        playsound("C:/Users/varou/PycharmProjects/Wakeupcall-master/test/"+str(folder)+"/"+str(current_node.data))
        return current_node.data
    else:
        print("its empty")
        return None


def main():

    choice_1 = question_1()

    if int(choice_1) == 1:
        choice_1_1 = question_1_1()

        if int(choice_1_1) == 1:
            my_des = question_1_1_1()
            work(my_des)

        if int(choice_1_1) == 4:
            main()

    if int(choice_1) == 3:
        choice_1_3 = question_1_3()

        if int(choice_1_3) == 1:
            question_1_3_1()

        if int(choice_1_3) == 2:
            choice_1_3_2 = question_1_3_2()

            if int(choice_1_3_2) == 1:
                question_1_3_2_1()

            if int(choice_1_3_2) == 2:
                question_1_3_2_2()

            if int(choice_1_3_2) == 3:
                question_1_3_2_3()

            if int(choice_1_3_2) == 4:
                question_1_3()

        if int(choice_1_3) == 3:
            choice_1_3_3 = question_1_3_3()

            if int(choice_1_3_3) == 1:
                question_1_3_3_1()

            if int(choice_1_3_3) == 2:
                question_1_3_3_2()

            if int(choice_1_3_3) == 3:
                main()

        if int(choice_1_3) == 4:
            question_1()


with open("Stations.json") as data_file:
    dictionary = json.load(data_file)
    hash = dict_to_hashmap(dictionary)

s = SingleLinkedList()
q = Queue()

while True:
    main()