class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Deque:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def insertFirst(self, obj):
        node = Node(obj, self._first)
        self._first = node
        if self._last == None:
            self._last = node
        self._size += 1

    def insertLast(self, obj):
        node = Node(obj, None)
        if self._last == None:
            self._first = node
            self._last = node
            self._size += 1
            return
        self._last.next = node
        self._last = node
        self._size += 1

    def removeFirst(self):
        if self._size == 0:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        self._first = self._first.next
        tmp.next = None
        self._size -= 1


    def removeLast(self):
        if self._size == 0:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        while tmp.next != self._last:
            tmp = tmp.next

        tmp.next = None
        self._last = tmp
        self._size -= 1

    def first(self):
        if self._size == 0:
            print("Deque is empty")
            return
        print(self._first.data)
        return self._first

    def last(self):
        if self._size == 0:
            print("Deque is empty")
            return
        print(self._last.data)
        return self._last

    def print(self):
        if self._size == 0:
            print("Deque is empty")
            return
        itr = self._first
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

def main():
    d = Deque()
    d.insertFirst(5)
    d.insertFirst(40)
    d.insertLast(4)
    d.insertLast(0)
    d.print()
    d.removeFirst()
    d.removeLast()
    d.print()
    d.first()
    d.last()

main()
