class Player(object):
    def __init__(self, mapPosX, mapPosY):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        
    def showOnMap(self):
        rectMode(CENTER)
        stroke(0)
        strokeWeight(4)
        fill(255)
        rect(self.mapPosX, self.mapPosY, 50, 50)
        rectMode(CORNER)
