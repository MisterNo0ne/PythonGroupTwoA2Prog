#zack did alla dis

class Enemy(object):
    def __init__(self, health, type, element, mapPosX, mapPosY, enemyID):
        self.health = health
        self.maxHealth = health
        self.type = type
        self.element = element
        self.mapPosX = mapPosX
        self.mapPosY = mapPosY
        self.enemyID = enemyID
        
        #defining respective elemental weaknesses and resistances
        self.weakness = []
        self.resistance = []
        if self.element == "fire":
             self.weakness.append("water")
             self.weakness.append("rock")
             self.resistance.append("ice")
             self.resistance.append("grass")
             self.resistance.append("fire")
        #3 resistances including it's own element and 2 weaknesses kinda like Pokemon
        #idea: some enemies have regenerative abilities


    def hit(self, initialDamage, attackType):
        """
        defining hit function for when the enemy gets hit, 
        in other words this is the damage calculator
        this is run in a for loop because attackType will combine 2 or 3 elements
        """
        damage = initialDamage
        print("Your initial attack was " + str(initialDamage) + " damage")
        for i in attackType:
            if i in self.weakness:
                damage=damage*2
                print("Your " + i + " attack was super effective against the opposing " + self.element + " type!")
            if i in self.resistance:
                damage=damage/2
                print("Your " + i + " attack was not very effective against the opposing " + self.element + " type...")
        self.health -= damage
        print("You did " + str(damage) + " damage! The monster's health is now " + str(self.health))
        if self.health <= 0:
            print("The monster died!")
        return self.health
        #later add a mechanic for dying where the enemy disappears or soemthing
        
        
    def mapDisplay(self):
        """
        rendering on the screen in map mode. For now this will just be a triangle before we implement any actual 
        enemy sprites with variation and coloration or indicators for elements. 
        """
        stroke(255,0,0)
        strokeWeight(5)
        triangle(self.mapPosX, self.mapPosY, self.mapPosX+50,self.mapPosY,self.mapPosX+25, self.mapPosY+50)
        
        textSize(24)
        fill(0)
        text("not a yield sign", self.mapPosX-100, self.mapPosY+25)
        
    def healthBarInFight(self):
        fractionOfHealth = self.health/self.maxHealth
        print(fractionOfHealth)
        
