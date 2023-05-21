class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value #e.g. amount of money, number of health pots
    
#ctrl+shift+o then go to basics/objects/inheritance to see how this works
class Weapon(Item):
    def __init__(self, name, value, damageModifiersEnemy, damageModifiersAttack, img):
        super(Weapon, self).__init__(name, value)
        self.damageModifiersEnemy = damageModifiersEnemy
        self.damageModifiersAttack = damageModifiersAttack
        self.img = img
        #value is base damage, 
        #damageModifiersEnemy is a list of floats to multiply by damage, e.g. if the enemy is rock type, arrow does less damage
        #damageModifiersAttack is a list of floats to multiply by damage, e.g. if the attack was fire type, arrow does more damage
