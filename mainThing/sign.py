class Sign:
    def __init__(self, mapPosX, mapPosY, dispText, signImage, textDispSize, lines):
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.dispText = dispText
        self.signImage = signImage
        self.textDispSize = float(textDispSize)
        self.lines = lines
        
    def showSign(self, playerPosX, playerPosY):
        imageMode(CENTER)
        image(self.signImage, self.mapPosX-playerPosX+(width/2), self.mapPosY-playerPosY+(height/2), 50, 50)
        imageMode(CORNER)
        #no way pointInsideRectangle wont break this so im not even gonna try
        if playerPosX > self.mapPosX - 45 and playerPosX < self.mapPosX + 45 and playerPosY > self.mapPosY - 45 and playerPosY < self.mapPosY + 45:
            pushMatrix()
            translate(self.mapPosX-playerPosX+(width/2), self.mapPosY-playerPosY+(height/2))
            
            fill(255, 255, 255, 127)
            noStroke()
            rect(-100, 30, 200, 40)
            
            textAlign(CENTER)
            fill(0)
            textSize(self.textDispSize)
            textLeading(self.textDispSize) #line spacing
            text(self.dispText, 0, 30+(40/(self.lines+1))+(self.textDispSize/10)+(5 if self.lines == 1 else 0)) #dont ask idk either
            popMatrix()
            textAlign(LEFT)
