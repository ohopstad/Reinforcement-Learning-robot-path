class Location:
    def __init__(self):
        self.__paths = []

    def addPath(self, location : Location):
        self.__paths.append(location)


class Floor:
    def __init__(self, len : int, wid : int):
        self.floor = [[Location() for i in range(wid)] for u in range(len)]
        

class Robot:
    #Moove from one Locatio to the next, find a good movement
    def init(self, floor : Floor):
        self.floor = floor
    
    def __repr__(self):
        return "Robot()"

    def move(self, location):
        return
