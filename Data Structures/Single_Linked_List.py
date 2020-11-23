class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LList_Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def insertFirst(self, key):
        node = Node(key, self.first)
        self.first = node
        if self.last == None:
            self.last = node
        self.size += 1

    def insertLast(self, key):
        node = Node(key, None)
        if self.last == None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def removeFirst(self):
        if self.size == 0:
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

    def insertBefore(self, key, data):
        if self.first and self.last:
            node = self.first
            tmp = None
            while node != None:
                if node.data == data:
                    new = Node(key, node)
                    if tmp != None:
                        self.first = new
                    else:
                        tmp.next = new
                    self.size += 1
                    return
                else:
                    tmp = node
                    node = node.next

    def insertAfter(self, key, data):
        if self.first and self.last:
            node = self.first
            while node != None:
                if node.data == data:
                    new = Node(key, node.next)
                    if node.next == None:
                        node.next = new
                        self.last = new
                    else:
                        node.next = new
                    self.size += 1
                    return
                else:
                    node = node.next

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

    def first(self):
        return self.first

    def last(self):
        return self.last

    def size(self):
        return self.size

    def print(self):
        if self.size == 0:
            print("List is empty")
            return
        itr = self.first
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

def main():
    d = LList_Deque()
    d.insertFirst(5)
    d.insertFirst(40)
    d.insertLast(4)
    d.insertLast(0)
    d.print()
    d.removeFirst()
    d.removeLast()
    d.print()
    d.insertBefore(4.5,4)
    d.insertAfter(3,4)
    d.print()
    d.remove(4.5)
    d.print()

main()
