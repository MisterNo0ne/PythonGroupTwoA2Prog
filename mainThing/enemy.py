#zac=k did alla dis

class Enemy(object):
    def __init__(self, health, type, element):
        #health = 50
        self.health = health
        self.type = type
        self.element = element
        self.weakness = []
        self.resistance = []
        #defining respective elemental weaknesses and resistances
        if self.element == "fire":
             self.weakness.append(["water", "rock"])
             self.resistance.append(["ice", "grass", "fire"])
    #3 resistances including it's own element and 2 weaknesses kinda like Pokemon

    #idea: some enemies have regenerative abilities
    #defining hit function for when the enemy gets hit, 
    #in other words this is the damage calculator
    #this is run in a for loop because attackType will combine 2 or 3 elements

    def hit(self, initialDamage, attackType):
        damage = initialDamage
        for i in attackType: 
            if i in self.weakness:
                damage=damage*2
            if i in self.resistance:
                damage=damage/2
        self.health -= damage
        if self.health <= 0:
            print("the monster is kil!")
        else:
            print("hi")
            #print("you did " + damage + "damage! \n the monster's health is now" + self.health)
        return self.health
        #later add a mechanic for dying where the enemy disappears or soemthing
