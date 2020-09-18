import folium

stations = []
class Stations:
    def __init__(self,code,name,destination):
        self.name = name
        self.code = code
        self.destination = destination

    def marker(self):
        m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)
        folium.Marker(self.destination, popup=( self.name,self.code), tooltip='click').add_to(m)
        m.save('test.html')

    def marker_with_rad(self):
        s.marker()
        m = folium.Map(location=[40.1776, 44.5126], zoom_start=15)
        m.add_child(folium.LatLngPopup())

        folium.Circle(radius=500, location=self.destination, color='green').add_to(m)
        marker = {"Destination": self.destination}
        for i in marker.items():
            folium.Marker(location=i[1], popup=i[0]).add_to(m)
            print(i)
        m.save('map.html')

    def create_dic(self):
        markers= {}
        markers.update({self.name : self.destination})
        return markers

s1 = Stations("s1", "France Square 1", [40.187821, 44.514453])
stations.append(s1)
s2 = Stations("s2", "France Square 2", [40.187891, 44.515820])
stations.append(s2)
s3 = Stations("s3", "France Square 3", [40.1876707, 44.5160554])
s4 = Stations("s4", "Mesrop Mashtots 1", [40.184753, 44.512428])
s5 = Stations("s5", "Mesrop Mashtots 2", [40.1847592, 44.5119651])
s6 = Stations("s6", "Mesrop Mashtots 3", [40.1813081, 44.507997])
s7 = Stations("s7", "Mesrop Mashtots 4", [40.1813081, 44.507997])
s8 = Stations("s8", "Mesrop Mashtots 5", [40.1787796, 44.5050988])
s9 = Stations("s9", "Mesrop Mashtots 6", [40.1783644, 44.5048064])
s10 = Stations("s10", "Kaskad", [40.1881197, 44.5154458])
s11 = Stations("s11", "Central bus station", [40.1725216, 44.4732186])
s12 = Stations("s12", "Baghramyan", [40.192003, 44.505178])

user_station = input("please tell me your station")
for s in stations:
    if s.code == user_station:
        s.marker()

for m in stations:
    if m.code == m.code:
        p = m.create_dic()
        print(p)
