import json
import folium


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

    def test(self):
        Code = str(input("""
        please type in the numerical code """))
        dictionary.get(Code)

    def show_marker(self, code):
        info = self.find_info(code)
        Destination = [info[2], info[3]]
        m = folium.Map(location= Destination, zoom_start=15)
        m.add_child(folium.LatLngPopup())

        folium.Circle(radius=500, location=Destination, color='green').add_to(m)
        folium.Marker(location= Destination, popup='<b>Destination</b>'+'\n'+'<i>'+info[0]).add_to(m)
        m.save('map.html')

    def find_info(self, code):
        raw = self.get(code)
        name = raw["name"]
        code = float(raw["code"])
        latitude = float(raw["lat"])
        longitude = float(raw["long"])
        return name, code, latitude, longitude

def dict_to_hashmap(dict_to_be_transformed):
    hashmap = HashMap()
    code = 0
    for key, value in dict_to_be_transformed.items():
        name = key
        lat = value[0]
        long = value[1]
        code = code + 1
        hashmap.put(str(code), {"name": name,
                                "lat": lat,
                                "long": long,
                                "code": code})
    return hashmap


def update_Stations_json():
        m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)

        m.add_child(folium.LatLngPopup())

        with open("Stations.json") as data_file:
            markers = json.load(data_file)
        code = 0
        for l in markers.items():
            code = code+1
            folium.Marker(location=l[1], popup='<b>'+l[0]+'</b>'+"\n"+'code:'+str(code)).add_to(m)
            print(l)

        m.save('Stations_map.html')


with open("Stations.json") as data_file:
    dictionary = json.load(data_file)
dictionary = dict_to_hashmap(dictionary)
Code = str(input("""
        please type in the numerical code """))
dictionary.show_marker(Code)
