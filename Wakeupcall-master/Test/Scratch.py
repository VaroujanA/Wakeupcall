import os
from playsound import playsound
import json

class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class SingleLinkedList():

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # DONE TESTING
    def insertFirst(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    # DONE TESTING
    def removeFirst(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    # DONE TESTING
    def insertLast(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    # DONE TESTING
    def removeLast(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        while tmp.next != self.last:
            tmp = tmp.next
        tmp.next = None
        self.last = tmp
        self.size -= 1

    # DONE TESTING
    def get_size(self):
        return self.size

    # DONE TESTING
    def get_first(self):
        return self.first

    # DONE TESTING
    def get_last(self):
        return self.last

    # DONE TESTING
    def remove(self, data):
        node = self.first
        previous = None
        while node != None:
            if node.data == data:
                if previous != None:
                    previous.next = node.next
                else:
                    self.first = node.next
                self.size -= 1
                return
            else:
                previous = node
                node = node.next

    def remove_nth(self):
        if self.size != 0:
            self.display_items()
            n = input("which do u want to select?")
            if int(n) > self.size:
                print("the number is higher than the amount of options, please try again")
                self.remove_nth()
            else:
                current_node = self.first
                for i in range(int(n) - 1):
                    current_node = current_node.next
                self.remove(current_node.data)
        else:
            print("its empty")
            return None

    def remove_all(self):
        if self.size == 0:
            return
        else:
            while self.size > 0:
                self.removeLast()



    def to_json(self):
        dictionary = {}
        music_list = []
        if self.size != 0:
            current_node = self.first
            while current_node is not None:
                music_list.append(current_node.data)
                current_node = current_node.next
            dictionary["music"] = music_list
        else:
            print("The list is empty")
        return dictionary

    def display_items(self):
        i = 1
        if self.size != 0:
            current_node = self.first
            while current_node is not None:

                print(str(i)+")", current_node.data)
                i = i+1
                current_node = current_node.next
        else:
            print("The list is empty")

    def display_nth_item(self, folder):
        n = input("which do u want to select?")
        if self.size != 0:
            current_node = self.first
            for i in range(int(n)-1):
                current_node = current_node.next
            print(current_node.data)
            playsound("C:/Users/varou/PycharmProjects/Wakeupcall-master/test/"+str(folder)+"/"+str(current_node.data))
            return current_node.data
        else:
            print("its empty")
            return None

    def remove_nth_item(self):
        n = input("which do u want to delete?")
        if self.size != 0:
            current_node = self.first
            for i in range(int(n)-1):
                current_node = current_node.next
            print(current_node.data)
            return current_node.data
        else:
            print("its empty")
            return None

    def save_all(self):
        self.choose_folder_and_convert_all_music_to_list_and_json()
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        music = SingleLinkedList()
        for e in dictionary["music"]:
            music.insertLast(e)
        cur_node = self.first
        while cur_node is not None:
            music.insertLast(cur_node.data)
            cur_node = cur_node.next
        with open('music_library.json', "w") as file:
            json.dump(music.to_json(), file, indent=2)
        music.remove_all()
        self.remove_all()

    def remove_choice(self):
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        for e in dictionary["music"]:
            self.insertLast(e)
        print()
        self.display_items()
        choice = str(self.remove_nth_item())
        self.remove(choice)
        print()
        self.display_items()
        with open('music_library.json', "w") as file:
            json.dump(self.to_json(), file, indent=2)
        self.remove_all()


    def save_choice(self):
        folder = self.choose_folder_and_convert_all_music_to_list_and_json()
        choice = str(self.display_nth_item(folder))
        print(choice) #remove
        with open("music_library.json") as data_file:
            dictionary = json.load(data_file)
        music = SingleLinkedList()
        for e in dictionary["music"]:
            music.insertLast(e)
        music.insertLast(choice)
        with open('music_library.json', "w") as file:
            json.dump(music.to_json(), file, indent=2)
        music.remove_all()
        self.remove_all()



    def choose_folder_and_convert_all_music_to_list_and_json(self):
        n = input("insert folder name")
        paths = os.listdir(n)
        music_key = {}
        music_list = []
        for path in paths:
            if path.endswith(".mp3"):
                music_list.append(path)
        music_key["music"] = music_list
        for e in music_key["music"]:
            self.insertLast(e)
        self.display_items()
        return n








