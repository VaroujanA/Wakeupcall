class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            self.tail = None
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data


    def first(self):
        return self.head

    def last(self):
        return self.tail

    def size(self):
        return self.size

    def display(self):
        if self.size == 0:
            print("Queue is empty")
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


    def print_arrows(self):
        if self.size == 0:
            print("Queue is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <-- ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
