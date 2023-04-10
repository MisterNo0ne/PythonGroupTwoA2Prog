class player(object):
    def __init__(self, mapPosX, mapPosY):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
    
    def printValues(self):
        println(str(self.knownElements[0]) + str(self.knownElements[1]))
