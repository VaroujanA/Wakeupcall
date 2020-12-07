class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class SingleLinkedList():

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insertFirst(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

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
            n = input("which do u want to remove?")
            if int(n) > self.size :
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

    def display_nth_item_and_return(self):
        n = input("which do u want to select?")
        if self.size != 0:
            current_node = self.first
            for i in range(int(n)-1):
                current_node = current_node.next
            print(current_node.data)
            return current_node.data
        else:
            print("its empty")
            return None

    def display_items(self):
        i = 1
        if self.size != 0:
            current_node = self.first
            while current_node is not None:

                print(str(i)+")", current_node.data)
                i = i+1
                current_node = current_node.next
        else:
            print("""
    music history is empty""")

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

    def get_size(self):
        return self.size

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last










