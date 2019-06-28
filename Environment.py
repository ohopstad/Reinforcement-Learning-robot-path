
class Location:
    def __init__(self, name):
        self.__paths = []
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)

    def addPath(self, location):
        self.__paths.append(location)

    def getPaths(self):
        return self.__paths


class Floor:
    def __init__(self, len : int, wid : int):
        self.floor = [[Location(str(u) + ":" + str(i)) for i in range(wid)] for u in range(len)]
        self.setActions()
    
    def setActions(self):
        for i in range(len(self.floor)):
            for u in range(len(self.floor[i])):
                if i != 0:
                    self.floor[i][u].addPath(self.floor[i-1][u])
                if i != len(self.floor) -1:
                    self.floor[i][u].addPath(self.floor[i+1][u])
                if u != 0:
                    self.floor[i][u].addPath(self.floor[i][u-1])
                if u != len(self.floor[i]) -1:
                    self.floor[i][u].addPath(self.floor[i][u+1])

    def getStates(self):
        ret = []
        for row in self.floor:
            retNext = []
            for location in row:
                retNext.append(location)
            ret.append(retNext)
        return ret
    
    def getPaths(self):
        ret = []
        for row in self.floor:
            retNext = []
            for location in row:
                retNext.append(location.getPaths())
            ret.append(retNext)
        return ret

if __name__ == "__main__":
    floor = Floor(3, 3)
    actions = floor.getStates()
    paths = floor.getPaths()

    print(actions)
    print()
    print(paths)