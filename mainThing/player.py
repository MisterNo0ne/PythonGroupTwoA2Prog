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
        xMov = 0 #horizontal movement (-1, 0, or 1)
        yMov = 0 #vertical movement (-1, 0, or 1)
        if keyHits[0]: #w pressed
            yMov -= 1
        if keyHits[1]: #a pressed
            xMov -= 1
        if keyHits[2]: #s pressed
            yMov += 1
        if keyHits[3]: #d pressed
<<<<<<< Updated upstream
            self.mapPosX += self.mapSpeed
            
=======
            xMov += 1
        
        if xMov != 0 and yMov != 0: #if moving diagonally
            print("diagonal movement")
        else:
            self.mapPosX += xMov * self.mapSpeed
            self.mapPosY += yMov * self.mapSpeed
        
"""
    def bumbIntoObstaclesOnMap(self, obstacles):
        for ob in obstacles:
"""
>>>>>>> Stashed changes
