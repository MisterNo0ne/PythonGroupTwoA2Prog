from enemy import Enemy
from item import Item
from npc import Npc
from obstacle import Obstacle
from player import Player
#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

def setup():
    size(400, 600)
    
    global gameState
    gameState = "map"
    
    
    #zacks stuff: alll zackk !)0%55%%%%
    ghoul = Enemy(50,"ghoul", "fire")
   # ghoul.hit(10,"water")

def draw():
    background(0)
    textSize(32)
    textAlign(CENTER)
    text("click please :)", width/2, height/2)
    """
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)
    """
    
def mousePressed():
    link("agar.io")
