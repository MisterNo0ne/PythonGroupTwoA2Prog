class Player(object):
    def __init__(self, mapPosX, mapPosY):
        self.knownElements = [True, True, False, True]
        self.itemsOwned = [] #items is already a thing ig
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.speed = 2
        
    def showOnMap(self):
        rectMode(CENTER)
        stroke(0)
        strokeWeight(4)
        fill(255)
        rect(self.mapPosX, self.mapPosY, 50, 50)
        rectMode(CORNER)
        
   # def move(self):
#        if leftPressed = true: 
  #          self.mapPosX-=self.speed
  #      if rightPressed = true:
   #         self.mapPosX+=self.speed
   #     if upPressed = true:
   #         self.mapPosY-=self.speed
    #    if downPressed = true:
     #       self.mapPosY+=self.speed
