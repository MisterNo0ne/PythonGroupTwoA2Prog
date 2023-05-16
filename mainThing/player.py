class Player(object):
    def __init__(self, mapPosX, mapPosY, health, playerImage):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.mapOrthogonalSpeed = 8.0
        self.health = health
        self.maxHealth = health
        self.mapDiagonalSpeed = 5.66 #orthogonal means up down left right
        self.playerImage = playerImage
        self.boundRadius = 15
        
    def showOnMap(self):
        stroke(0)
        strokeWeight(4)
        fill(255)
        image(self.playerImage, (width/2)-32, (height/2)-32)
        
    def moveOnMap(self, keyHits, obs):
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
            
        """
        Code for collision detection inspired by - https://gamedev.stackexchange.com/questions/586/what-is-the-fastest-way-to-work-out-2d-bounding-box-intersection
        works by calculating the distance between the boxes' centers and then seeing if that's bigger than half their widths 
        (like intersecting circles) but does it on both x and y axes instead of a 2d distance
        """
        hitObstacle = False
        for o in obs:
            #check to see if player is intersecting with o
            xDist = abs(self.mapPosX - (o.xPos + (o.w/2)))
            yDist = abs(self.mapPosY - (o.yPos + (o.h/2)))
            if xDist < self.boundRadius+(o.w/2) and yDist < self.boundRadius+(o.h/2):
                hitObstacle = True
                #break
        
        #Resolve collisions
        if hitObstacle: 
            #negate the player movement that just happened
            if xMov != 0 and yMov != 0: #if moving diagonally
                self.mapPosX -= xMov * self.mapDiagonalSpeed
                self.mapPosY -= yMov * self.mapDiagonalSpeed
            else: #if moving orthogonally
                self.mapPosX -= xMov * self.mapOrthogonalSpeed
                self.mapPosY -= yMov * self.mapOrthogonalSpeed
            
    def showInFight(self):
        image(self.playerImage, 0, 260, 320, 340)
        
        #health bar
        strokeWeight(4)
        stroke(0)
        fill(255)
        rect(280, 500, 300, 40)
        fill(255, 0, 0)
        noStroke()
        rect(282, 502, 297*(float(self.health)/self.maxHealth), 37)
        
        #reset settings
        rectMode(CORNER)
        stroke(0)
        
