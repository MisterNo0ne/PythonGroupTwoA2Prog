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
        
    def moveOnMap(self, keyHits):
        if keyHits[0]: #w pressed
            self.mapPosY -= self.mapSpeed
        if keyHits[1]: #a pressed
            self.mapPosX -= self.mapSpeed
        if keyHits[2]: #s pressed
            self.mapPosY += self.mapSpeed
        if keyHits[3]: #d pressed
            self.mapPosX += self.mapSpeed
            
   # def bumbIntoObstaclesOnMap(self, obstacles):
