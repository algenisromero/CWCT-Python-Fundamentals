import webbrowser

class House:
    def __init__(self, mapurl) -> None:
        self.mapurl = mapurl

    def ShowMap(self):
        webbrowser.open(self.mapurl, new=2)

#Main program
#Paste map link to your house below...
myHouse = House("https://www.google.com/maps/@37.4223878,-122.0863817,17z")
myHouse.ShowMap()

