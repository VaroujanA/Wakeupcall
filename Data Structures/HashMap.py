class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap():
    def __init__(self):
        self.capacity = 20
        self.hashtable = [None] * self.capacity * 10
        self.size = 0

    def __iter__(self):
        for i in range(len(self.hashtable)):
            if (self.hashtable[i] != None):
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self.hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self.hashtable)
        for i in range(tmpInd + 1, len(self.hashtable)):
            if (self.hashtable[i] != None):
                self._index = i
                break

        return self.hashtable[tmpInd].value

    def hash(self, element):
        return ord(element[0]) % self.capacity

    def put(self, key, value):
        index = self.hash(key)
        for i in range(index, len(self.hashtable)):
            if (self.hashtable[i] != None):
                if key == self.hashtable[i].key:
                    oldValue = self.hashtable[i].value
                    self.hashtable[i].value = value
                    return oldValue
            else:
                self.hashtable[index] = Entry(key, value)
                self.size += 1
                return None


    def remove(self, key):
        index = self.hash(key)
        for i in range(index, len(self.hashtable)):
            if (self.hashtable[i] != None):
                if key == self.hashtable[i].key:
                    self.hashtable[i].key = None
                    self.hashtable[i].value = None
            else:
                return None

    def size(self):
        return self.size

    def print(self):
        print("printing hashset elements")
        for e in self.hashtable:
            while (e != None):
                print(e.key, e.value)
                e = e.next

def main():
    dictionary = HashMap()
    dictionary.put("A", {"fruits": "Apple, Apricot",
                              "Names": "Armen, Aaron"})
    dictionary.put("B", {"fruits": "Banana, Blueberry",
                              "Names": "Barkev, Baley"})
    dictionary.put("C", {"fruits": "Coconut, Cactus",
                            "Names": "Chris, Coco"})
    dictionary.print()
    print()

    dictionary.remove("C")
    dictionary.print()

main()
