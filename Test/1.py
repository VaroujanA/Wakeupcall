import requests
import time
from playsound import playsound
import webbrowser
import os
import json
from Test.Costum_Hashmap import HashMap
from Scratch_copy import SingleLinkedList
from directory import give_name_find_path


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

def dict_to_hash(dict_to_be_transformed):
    hashmap = HashMap()
    for key, value in dict_to_be_transformed.items():
        hashmap.put(key, value)
    return hashmap

def check_numb_1234(choice):
    if str(choice).isalpha() is True or str(choice) == "":
        print("""
    Please answer with 1, 2, 3, 4
    """)
        return None
    elif int(choice) in (1, 2, 3,4):
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
    3) go back
    """))
        choice = check_numb_123(choice_1_3)
        if choice is None:
            pass
        else:
            return choice

def question_1_3_1():
    while True:
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        for e in dictionary["music"]:
            s.insertLast(e)
        print()
        s.display_items()
        choice = s.display_nth_item()
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
        choice_1_3_2  = (input("""
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

def question_1_3_2_1():
    s.save_choice()

def question_1_3_2_2():
    s.remove_choice()

def question_1_3_2_3():
    s.save_all()





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


def question_1_1_2():
    while True:
        if os.stat("History.json").st_size == 0:
            print("""
    your history is empty
    """)
            main()
        else:
            print("History:")
            i = 0
            for e in history.hashtable:
                while e is not None:
                    print(str(i+1),")",e.key)
                    break
            choice = input("""
                Please type the wanted destination
                """)
        test = history.get(choice)
        if test is None:
            n = input("""
        cannot identify, press y to try again or press n to go back""")
            if n == "n":
                main()
        else:
            return choice
        if choice == 'n':
            main()

def question_1_1_3():
    choice_1_1_3 = (input("""
        you will be shown a map, click anywhere to see the coordinates"
        would you like to proceed? [y/n]
    """))
    fl = choice_1_1_3[0].lower()
    if choice_1_1_3 == '' or fl not in ['y', 'n']:
        print("""
        Please answer with yes or no!
    """)
    elif fl == 'y':
        webbrowser.open_new_tab('plain_map.html')
        lat = input("""
        please insert the numerical value of the lattitude
    """)
        long = input("""
        please insert the numerical value of the longitude
    """)
        return lat, long


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


def check_if_in_radius(curlatitude, curlongitude, lat, long, radius):
    complete = "c"
    with open("player.json") as data_file:
        dictionary = json.load(data_file)
        print(dictionary)
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

                info = hash.find_info(code)
                lat = info[2]
                long = info[3]
                complete = check_if_in_radius(cur_lat, cur_long, lat, long, radius)
                if complete == "c":
                    break
            break
        if choice == 'n':
            main()


def add_location_to_history(code):
    info = hash.find_info(code)
    lat = info[2]
    long = info[3]

    add_his = input("""
    Would you like to save this destination to your history? [y/n]
    """)
    choice = check_yes_no(add_his)
    if choice is None:
        pass
    if choice == 'y':
        name = input("""
    Please input the name of the destination
    """)

        history.put(name, [lat, long])
        history.print()
        update_history()

    if add_his == 'n':
        end()
        main()

def update_history():
    dict = history.hash_to_dict()
    with open('History.json', 'w') as data:
        json.dump(dict, data, indent=2)

def work(my_des):
    radius = 0.5 / 85.39
    hash.show_marker(my_des)
    open_map_and_proceed(my_des, radius)
    add_location_to_history(my_des)
    end()

def hello():
    print("""
    Hello, Welcome to WakeUp Call! 
    """)


def end():
    print("""
    Finitto! thanks for using WakeUp Call!
    """)


def main():

    choice_1 = question_1()

    if int(choice_1) == 1:
        choice_1_1 = question_1_1()

        if int(choice_1_1) == 1:
            my_des = question_1_1_1()
            work(my_des)

        if int(choice_1_1) == 2:
            question_1_1()
            #choice_1_1_2 = question_1_1_2()
            #my_des = choice_1_1_2
            #work(my_des)

        if int(choice_1_1) == 3:
            question_1_1()
            #choice_1_1_3 = question_1_1_3()
            #lat = float(choice_1_1_3[0])
            #long = float(choice_1_1_3[1])
            #destination = [lat, long]

        if int(choice_1_1) == 4:
            question_1()

    if int(choice_1) == 3:
        choice_1_3 = question_1_3()

        if int(choice_1_3) == 1:
            question_1_3_1()

        if int(choice_1_3) == 2:
            choice_1_3_2 = question_1_3_2()

            if int(choice_1_3_2) == 1:
                question_1_3_2_1()
                choice_1_3_2 = question_1_3_2()

            if int(choice_1_3_2) == 2:
                question_1_3_2_2()
                choice_1_3_2 = question_1_3_2()

            if int(choice_1_3_2) == 3:
                question_1_3_2_3()
                choice_1_3_2 = question_1_3_2()

            if int(choice_1_3_2) == 4:
                question_1_3()

        if int(choice_1_3) == 3:
            question_1()


with open("Stations.json") as data_file:
    dictionary = json.load(data_file)
    hash = dict_to_hashmap(dictionary)

with open("History.json") as data_file:
    dictionary = json.load(data_file)
    history = dict_to_hash(dictionary)

s = SingleLinkedList()
while True:
    hello()
    main()

