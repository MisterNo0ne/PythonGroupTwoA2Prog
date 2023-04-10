class Enemy(object):
    def __init__(self, health, type, element):
        health = 50
        self.health = health
        self.type = type
        self.element = element
        self.weakness = []
        self.resistance = []
        #defining respective elemental weaknesses and resistances
        if self.element == "fire":
             self.weakness.append(["water", "rock"])
             self.resistance.append(["ice", "grass"])
        #3 resistances (including it's own element) and 2 weaknesses (think Pokemon)
    
    #idea: some enemies have regenerative abilities
    #defining hit function for when the enemy gets hit, 
    #in other words this is the damage calculator
    #this is run in a for loop because attackType will combine 2 (or 3) elements
    def hit(initialDamage, attackType):
        damage = initialDamage
        for i in attackType: 
            if i == self.element:
                damage=damage/2
            if i == self.weakness:
                damage=damage*2
            if i == self.resistance:
                damage=damage/2
        self.health -= damage
        return self.health
        print(self.health)
        #later add a mechanic for dying where the enemy disappears or soemthing
        
