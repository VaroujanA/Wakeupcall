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

    def insertFirst(self,data):
        node = Node(data)
        if self.head == None:
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def insertLast(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def removeFirst(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def removeLast(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        else:
            if self.head != self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
        self.size -=1

    def insertAfter(self, key, data):
        cur = self.head
        while cur:
            if cur.next == None and cur.data == key:
                self.insertLast(data)
                return
            elif cur.data == key:
                node = Node(data)
                nxt = cur.next
                cur.next = node
                node.next = nxt
                nxt.prev = node
            cur = cur.next
        self.size += 1

    def insertBefore(self, key, data):
        cur = self.head
        while cur:
            if cur.prev == None and cur.data == key:
                self.insertFirst(data)
            elif cur.data == key:
                node = Node(data)
                prev = cur.prev
                prev.next = node
                cur.prev = node
                node.next = cur
            cur = cur.next
        self.size += 1

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
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


def main():
    dll = DoubleLiknedList()
    dll.insertFirst(5)
    dll.insertFirst(40)
    dll.insertLast(4)
    dll.insertLast(0)
    dll.print()
    dll.insertAfter(40,20)
    dll.insertBefore(40,60)
    dll.print()
    dll.removeFirst()
    dll.removeLast()
    dll.print()
    dll.insertAfter(40, 30)
    dll.insertBefore(40, 50)
    dll.print()
    dll.first()
    dll.last()
main()