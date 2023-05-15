#zack did alla dis

class Enemy(object):
    def __init__(self, health, type, element, mapPosX, mapPosY, img, status):
        self.health = health
        self.maxHealth = health
        self.type = type
        self.element = element
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.img = img
        self.status = status
    #    self.hitbox=hitbox
        #defining respective elemental weaknesses and resistances
        self.weakness = []
        self.resistance = []
        if self.element == "fire":
             self.weakness.append("water")
             self.weakness.append("rock")
             self.resistance.append("ice")
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
             self.resistance.append("air")
        if self.element == "grass": 
             self.weakness.append("fire")
             self.weakness.append("ice")
             self.resistance.append("rock")
             self.resistance.append("water")
             self.resistance.append("grass")
       # if self.element == "lightning": 
          #   self.weakness.append("fire")
            # self.weakness.append("rock")
           #  self.resistance.append("water")
          #   self.resistance.append("lightning")
         #    self.resistance.append("grass")
      #  if self.element == "rock": 
        #     self.weakness.append("water")
        #     self.weakness.append("grass")
         #    self.resistance.append("fire")
          #   self.resistance.append("rock")
           #  self.resistance.append("ice")
        #3 resistances including it's own element and 2 weaknesses kinda like Pokemon
        #idea: some enemies have regenerative abilities


    def hit(self, initialDamage, attackType):
        """
        defining hit function for when the enemy gets hit, 
        in other words this is the damage calculator
        this is run in a for loop because attackType will combine 2 or 3 elements
        """
        damage = initialDamage
        #print("Your initial attack was " + str(initialDamage) + " damage")
        for i in attackType:
            if i in self.weakness:
                damage=damage*2
                print("Your " + i + " attack was super effective against the opposing " + self.element + " type! (x2 damage)")
            if i in self.resistance:
                damage=damage/2
                print("Your " + i + " attack was not very effective against the opposing " + self.element + " type... (x0.5 damage)")
            #fire attacks against overgrown should go crazy
            if self.status == "overgrown" and i == "fire":
                damage=damage*10
                print("The overgrown vines burst into overwhelming flames! (x10 damage)")
            if i == "fire":
                self.status = "burning"
            if i == "water":
                self.status = "wet"
            if i == "grass":
                self.status = "tangled"
        self.health -= damage
    
        print("You did " + str(damage) + " damage!")
            
        
        return self.health
        #return self.status
        #later add a mechanic for dying where the enemy disappears or soemthing
        
        
    def mapDisplay(self, playerX, playerY):
        """
        rendering on the screen in map mode. For now this will just be a triangle before we implement any actual 
        enemy sprites with variation and coloration or indicators for elements. 
        """
        stroke(255,0,0)
        strokeWeight(5)
        image(self.img, self.mapPosX-playerX+(width/2), self.mapPosY-playerY+(height/2))
        
        textSize(16)
        fill(0)
        text(self.element + " " + self.type, self.mapPosX-playerX+(width/2), self.mapPosY-playerY+(height/2)+50)
        
    def healthBarInFight(self):
        fractionOfHealth = self.health/self.maxHealth
        print(fractionOfHealth)
    def display(self, imag): 
        image(imag, 220,50,420,250)
