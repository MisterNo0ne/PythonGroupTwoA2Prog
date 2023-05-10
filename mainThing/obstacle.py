#micah did this
class Obstacle(object):
    #only on map screen
    def __init__(self, xPos, yPos, w, h):
        self.xPos = xPos
        self.yPos = yPos
        self.w = w
        self.h = h
        
    def display(self, playerX, playerY):
        """
        if displayOn: #so that you can turn off showing the obstacles if you want
            stroke(255, 0, 0)
            strokeWeight(3)
            noFill()
            rect(self.xPos, self.yPos, self.w, self.h)
        """
        stroke(255, 0, 0)
        strokeWeight(3)
        noFill()
        rect(self.xPos-playerX+(width/2), self.yPos-playerY+(height/2), self.w, self.h)
