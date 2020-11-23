class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLiknedList:
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
        if self.head == None:
            print("The list is empty. Nothing to remove")
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def size(self):
        return self.size

    def print(self):
        if self.size == 0:
            print("List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <-- ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


def main():
    dll = DoubleLiknedList()
    dll.enqueue(20)
    dll.enqueue(4)
    dll.enqueue(0)
    dll.print()
    dll.dequeue()
    dll.print()
    dll.first()
    dll.last()
main()