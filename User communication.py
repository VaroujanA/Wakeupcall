import webbrowser
import os
import json

print ("Hello, Welcome to WakeUp Call! ")

while True:
    Choice_1 = int(input ("""
    What do you want to do?
    
    1) WAKE ME UP!
    2) History settings
    3) music settings

(type the number that corresponds to your choice)
"""))
    if Choice_1 == '' or not 1:
        print('Please answer with 1,2 or 3')
    else:
        break

if Choice_1 == 1:
    while True:
        Choice_1_1 = (int(input("""
    Choose your destination

    1) Bus Station
    2) History
    3) Choose your own destination

            """)))
        if Choice_1 == '' or not 1 or not 2 or not 3:
            print('Please answer with 1,2 or 3')
        else:
            break

    if Choice_1_1 == 1:
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
        #if Fl == 'n':

    if Choice_1_1 == 2:
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
                    print(item[str(Chosen_history)])