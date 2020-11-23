class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last == None:
            self.last = node
        self.size += 1

    def pop(self):
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

    def peek(self):
        return self.first

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
    d = Stack()
    d.push(5)
    d.push(25)
    d.push(40)
    d.print()
    d.pop()
    d.print()
    d.peek()

main()

