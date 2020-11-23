class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet():
    def __init__(self, capacity):
        self.hashtable = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def __iter__(self):
        for e in self.hashtable:
            if (e != None):
                self.elem = e
                break
        return self

    def __next__(self):
        if self.elem == None:
            raise StopIteration

        tmp = self.elem
        if (self.elem.next != None):
            self.elem = self.elem.next
        else:
            index = self.hash(self.elem.data)
            self.elem = None
            for i in range(index + 1, len(self.hashtable)):
                if (self.hashtable[i] != None):
                    self.elem = self.hashtable[i]
                    break
        return tmp.data

    def hash(self, element):
        return hash(element) % self.capacity

    def add(self, element):
        index = self.hash(element)
        if (self.hashtable[index] == None):
            self.hashtable[index] = Node(element)
        else:
            n = Node(element, self.hashtable[index])
            self.hashtable[index] = n
        self.size += 1

    def contains(self, element):
        index = self.hash(element)
        n = self.hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self.hash(element)
        n = self.hashtable[index]
        p = None
        while (n != None):
            if (n.data == element):
                if (p == None):
                    self.hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self.size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self.size

    def print(self):
        print("printing hashset elements")
        for e in self.hashtable:
            while (e != None):
                print(e.data)
                e = e.next

def main():
    HS = HashSet(100)
    HS.add("a")
    HS.add("b")
    HS.add(1)
    HS.add(3)
    HS.print()

main()