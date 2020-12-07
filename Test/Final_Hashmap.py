class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self._capacity = 20
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break
        return self._hashtable[tmpInd].value

    def _hash(self, element):
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[i] = Entry(key, value)
                self._size += 1
                return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    return True
            else:
                return False

    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    self._hashtable[i].key = None
                    self._hashtable[i].value = None
            else:
                return None

    def size(self):
        return self._size

    def print(self):
        #print("printing hashset elements")
        for e in self._hashtable:
            while e is not None:
                print("\t", e.key, ":", e.value)
                break

    def nested_print(self):
        def specific_print(hashmap, quantity_var):
            quantity_var += 1
            for e in self._hashtable:
                while e is not None:
                    if type(e.value) != int and type(e.value) != str:
                        tab = "\t" * quantity_var
                        print(tab, e.key, ":")
                        specific_print(e.value, quantity_var)
                        break
                    else:
                        tab = "\t" * quantity_var
                        print(tab, e.key, ":", e.value)
                        break
        dig_number = 0
        specific_print(self, dig_number)
