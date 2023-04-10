from enemy import Enemy
from item import Item
from npc import Npc
from obstacle import Obstacle
from player import Player

#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

def setup():
    size(800, 600)
    
    global gameState, ghoul, block, debugMode
    gameState = "map"
    ghoul = Enemy(50,"ghoul", "fire")
    ghoul.hit(10, ["water", ""])
    block = Obstacle(100, 100, 300, 100)
    debugMode = True #displays obstacles

def draw():
    background(0)
    if gameState == "fight":
        background(200)
    else: #gameState is in map mode
        background(0, 200, 0)
        block.display(debugMode)
    
    textSize(32)
    textAlign(CENTER)
    text("click please :)", width/2, height/2)
    
def mousePressed():
    link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i512j0i10i512l6j0i512l2.2697j0j7&sourceid=chrome&ie=UTF-8")
