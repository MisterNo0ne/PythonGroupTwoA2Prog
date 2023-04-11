#zac=k did alla dis

class Enemy(object):
    def __init__(self, health, type, element, xpos, ypos):
        #health = 50
        self.health = health
        self.type = type
        self.element = element
        self.weakness = []
        self.resistance = []
        self.xpos=xpos
        self.ypos=ypos
        #defining respective elemental weaknesses and resistances
        if self.element == "fire":
             self.weakness.append("water")
             self.weakness.append("rock")
             self.resistance.append("ice")
             self.resistance.append("grass")
             self.resistance.append("fire")
    #3 resistances including it's own element and 2 weaknesses kinda like Pokemon

    #idea: some enemies have regenerative abilities
    #defining hit function for when the enemy gets hit, 
    #in other words this is the damage calculator
    #this is run in a for loop because attackType will combine 2 or 3 elements

    def hit(self, initialDamage, attackType):
        damage = initialDamage
        for i in attackType:
            print("evaluating attackType " + i)
            print(self.weakness) 
            if i in self.weakness:
                damage=damage*2
                print("Your attack was super effective against the opposing " + self.element + " type!")
            if i in self.resistance:
                damage=damage/2
                print("Your attack was not very effective...")
        self.health -= damage
        if self.health <= 0:
            print("you did " + str(damage) + " damage! the monster's health is now " + str(self.health))
            print("the monster is kil!")
        else:
            print("you did " + str(damage) + " damage! the monster's health is now " + str(self.health))
        return self.health
        #later add a mechanic for dying where the enemy disappears or soemthing
        
        #rendering on the screen in map mode. For now this will just be a triangle before we implement any actual 
        #enemy sprites with variation and coloration or indicators for elements. 
    def mapDisplay(self, xpos, ypos):
        stroke(255,0,0)
        strokeWeight(5)
        triangle(self.xpos, self.ypos, self.xpos+50,self.ypos,self.xpos+25, self.ypos+50)
        
