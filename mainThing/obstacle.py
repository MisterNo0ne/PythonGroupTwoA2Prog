#micah did this
class Obstacle(object):
    #only on map screen
    def __init__(self, xPos, yPos, w, h):
        self.xPos = xPos
        self.yPos = yPos
        self.w = w
        self.h = h
        
    def display(displayOn):
        if displayOn: #so that you can turn off showing the obstacles if you want
            stroke(255, 0, 0)
            strokeWeight(3)
            noFill()
            rect(self.xPos, self.yPos, self.w, self.h)
        
