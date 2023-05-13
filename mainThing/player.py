class Player(object):
    def __init__(self, mapPosX, mapPosY, health):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.mapOrthogonalSpeed = 30
        self.health = health
        self.mapDiagonalSpeed = 20.12 #orthogonal means up down left right
        
    def showOnMap(self):
        rectMode(CENTER)
        stroke(0)
        strokeWeight(4)
        fill(255)
        wizard = loadImage("Wizard.png")
        
        image(wizard, width/2, height/2)
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
            xMov += 1
        
        if xMov != 0 and yMov != 0: #if moving diagonally
            self.mapPosX += xMov * self.mapDiagonalSpeed
            self.mapPosY += yMov * self.mapDiagonalSpeed
        else: #if moving orthogonally
            self.mapPosX += xMov * self.mapOrthogonalSpeed
            self.mapPosY += yMov * self.mapOrthogonalSpeed
            
    def showInFight(self):
        rectMode(CORNER)
        stroke(0)
        strokeWeight(4)
        fill(255)
        wizard = loadImage("Wizard.png")
        image(wizard, 0, 260, 320, 340)
