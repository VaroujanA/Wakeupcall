from abc import ABC, abstractmethod
import json


class ListADT(ABC):

    @abstractmethod
    def insertFirst(self, data):
        pass

    @abstractmethod
    def removeFirst(self):
        pass

    @abstractmethod
    def insertLast(self, data):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_last(self):
        pass

    @abstractmethod
    def insertBefore(self, data, data_to_check):
        pass

    @abstractmethod
    def insertAfter(self, data, data_to_check):
        pass

    @abstractmethod
    def remove(self, data):
        pass

    @abstractmethod
    def indexOf(self, data):
        pass

    @abstractmethod
    def get_size(self):
        pass


class Node:

    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next = next_node
        self.previous = previous


class SingleLinkedList(ListADT):

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
    def insertBefore(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            previous_node = None
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node)
                    if previous_node is None:
                        self.first = new_node
                    else:
                        previous_node.next = new_node
                    self.size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
        else:
            print("List is empty")

    # DONE TESTING
    def insertAfter(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node.next)
                    if current_node.next is None:
                        current_node.next = new_node
                        self.last = new_node
                    else:
                        current_node.next = new_node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
        else:
            print("List is empty")

    # DONE TESTING
    def remove(self, data):
        current_node = self.first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    # DONE TESTING
    def indexOf(self, data):
        current_node = self.first
        index = 0
        while current_node.next is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        print("No such data")

    def displayItems(self):
        if self.size != 0:
            current_node = self.first
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

        else:
            print("The list is empty")

    def to_json(self):
        dictionary = []
        if self.size != 0:
            current_node = self.first
            while current_node is not None:
                dictionary.append(current_node.data)
                current_node = current_node.next
        else:
            print("The list is empty")
        return dictionary


def main():
    dictionary_file = "../a.json"
    with open(dictionary_file) as data_file:
        dictionary = json.load(data_file)
    names_llist = SingleLinkedList()
    for element in dictionary:
        names_llist.insertFirst(element)

    print(names_llist.get_size())
    print(SingleLinkedList.get_size(names_llist))
    names_llist.displayItems()

    names_llist.insertFirst(input("Write a creature's name to be inputted ---- "))
    print(names_llist.get_size())
    with open('new_file.json', "w") as file:
        json.dump(names_llist.to_json(), file, indent=2)


main()
