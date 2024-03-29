#zack did alla dis

class Enemy(object):
    def __init__(self, health, type, element, mapPosX, mapPosY, img, status, strength, isBoss, area):
        self.health = health
        self.maxHealth = health
        self.type = type
        self.element = element
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.img = img
        self.status = status
        self.strength = strength
        self.isBoss = isBoss
        self.area = area
    #    self.hitbox=hitbox
        #defining respective elemental weaknesses and resistances
        self.weakness = []
        self.resistance = []
        if self.element == "fire":
             self.weakness.append("water")
             #self.weakness.append("rock") #this makes rock attack + frozen status + fire enemy do 600 damage so it gets gone
             self.resistance.append("ice")
             self.resistance.append("lightning")
             self.resistance.append("grass")
             self.resistance.append("fire")
       # if self.element == "ice": 
        #     self.weakness.append("fire")
         #    self.weakness.append("rock")
          #   self.resistance.append("ice")
           #  self.resistance.append("poison")
          #   self.resistance.append("grass")
        if self.element == "water": 
             self.weakness.append("lightning")
             self.weakness.append("ice")
             self.weakness.append("grass")
             self.resistance.append("water")
             self.resistance.append("fire")
             self.resistance.append("rock")
        if self.element == "grass": 
             self.weakness.append("fire")
             self.weakness.append("ice")
             self.resistance.append("water")
             self.resistance.append("grass")
       # if self.element == "lightning": 
          #   self.weakness.append("fire")
            # self.weakness.append("rock")
           #  self.resistance.append("water")
          #   self.resistance.append("lightning")
         #    self.resistance.append("grass")
        if self.element == "rock": 
             self.weakness.append("water")
             self.weakness.append("grass")
             self.weakness.append("lightning")
             self.resistance.append("fire")
             self.resistance.append("rock")
             self.resistance.append("ice")
        #3 resistances including it's own element and 2 weaknesses kinda like Pokemon
        #idea: some enemies have regenerative abilities


    def hit(self, initialDamage, attackType, weapon):
        damage = initialDamage
        damageMultiplier = 1
        
        #resistances and weaknesses
        if attackType in self.weakness:
            damageMultiplier=2
            print("Your " + attackType + " attack was super effective against the opposing " + self.element + " type! (+1x damage)")
        if attackType in self.resistance:
            damageMultiplier=0.5
            print("Your " + attackType + " attack was not very effective against the opposing " + self.element + " type... (-0.5x damage)")
            
        #Other damage modifiers
        """
        if self.element == "fire" and attackType == "water":
            damageMultiplier+=0.5
            print("The fire dies down in the flood! (+0.5x damage)")
        """
        if self.element == "rock" and attackType == "lightning":
            damageMultiplier+=2
            print("The rock shatters at its edges! (+2x damage)")
        if self.status == "tangled" and attackType == "fire":
            damageMultiplier+=1
            print("The vines burst into flames! (+1x damage)")
        if self.status == "overgrown" and attackType == "fire":
            damageMultiplier+=4
            print("The overgrown vines burst into overwhelming flames! (+4x damage)")
        if self.status == "frozen" and attackType == "rock": 
            damageMultiplier+=6
            print("The rock attack smashed through the brittle enemy, dealing massive damage! (+6x damage)")
        if self.status == "wet" and attackType == "lightning": 
            damageMultiplier+=3
            print("The lightning attack electrocuted the wet enemy, dealing extra damage! (+3x damage)")
            
        #Statuses
        if attackType == "fire":
            self.status = "burning"
        if attackType == "water":
            if self.status == "tangled" or self.status == "overgrown":
                self.status = "overgrown"
            else:
                self.status = "wet"
        if attackType == "grass":
            if self.status == "tangled" or self.status == "wet":
                self.status = "overgrown"
            else:
                self.status = "tangled"
        if attackType == "ice": 
            if self.status == "wet" or self.element == "water": 
                self.status = "frozen"
        if attackType == "lightning" and (self.status == "wet" or self.element == "water"):
            self.status = "zapped"
        
        damage *= damageMultiplier            
        self.health -= damage
    
        print("You did " + str(damage) + " damage!")
        
        return self.health
        #return self.status
        
    def mapDisplay(self, playerX, playerY, debugMode):
        stroke(255,0,0)
        strokeWeight(5)
        imagsize = 200 if self.isBoss else 100
        image(self.img, self.mapPosX-playerX+(width/2), self.mapPosY-playerY+(height/2), imagsize, imagsize)
        
        textSize(16)
        fill(0)
        text(self.element + " " + self.type, self.mapPosX-playerX+(width/2), self.mapPosY-playerY+(height/2)+50)
        
        if debugMode:
            noFill()
            stroke(0, 255, 255)
            rect(self.mapPosX-playerX+(width/2), self.mapPosY-playerY+(height/2), imagsize, imagsize)
        
    def healthBarInFight(self):
        fractionOfHealth = float(self.health)/self.maxHealth
        strokeWeight(4)
        fill(255)
        rect(40, 60, 300, 33)
        fill(255, 0, 0)
        noStroke()
        rect(42, 62, 297*(float(self.health)/self.maxHealth), 30)
        
    def display(self): 
        image(self.img, 220,50,420,250)
        if self.element == "grass": 
            tint(100,255,100,127)
        if self.element == "fire": 
            tint(255,0,0,127)
        if self.element == "water": 
            tint(75,75,255,127)
        image(self.img, 220,50,420,250) #tinted one
        
        tint(255,255,255) # <-- regular
        
    def displayStatus(self): 
        if self.status == "burning": 
            statusimg = loadImage("burning.png")
            image(statusimg,220,50,420,250)
        if self.status == "tangled":
            statusimg = loadImage("vines.png")
            image(statusimg,250,150,420,150)
        if self.status == "overgrown":
            statusimg = loadImage("vines.png")
            image(statusimg,250,50,420,275)
        if self.status == "wet": 
            statusimg = loadImage("puddle.png")
            image(statusimg,250,100,420,350)
        if self.status == "none": 
            rect(0,0,0,0)
            
        if self.status == "frozen": 
            statusimg = loadImage("Frozen.png") 
            tint(255,255,255,127)
            image(statusimg,180,60,420,350)
            tint(255,255,255)
        else: 
            rect(0,0,0,0)
            tint(255,255,255)
            
      #  return amogguss!!!!
