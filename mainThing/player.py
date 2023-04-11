class Player(object):
    def __init__(self, mapPosX, mapPosY):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.mapSpeed = 3
        
    def showOnMap(self):
        rectMode(CENTER)
        stroke(0)
        strokeWeight(4)
        fill(255)
        rect(self.mapPosX, self.mapPosY, 50, 50)
        rectMode(CORNER)
        
    def moveOnMap(self):
        if keyPresses[0]: #w
            self.mapPosY -= 3
            """
        if keyPresses[1]: #a
            self.mapPosX -= self.mapSpeed
        if keyPresses[2]: #s
            self.mapPosY += self.mapSpeed
        if keyPresses[3]: #d
            self.mapPosX += self.mapSpeed
            """
