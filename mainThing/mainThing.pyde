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
    
    global gameState, ghoul
    gameState = "map"
    
    
    #zacks stuff: alll zackk !)0%55%%%%
    ghoul = Enemy(50,"ghoul", "fire")
    #ghoul.hit(10,"water")

def draw():
    background(0)
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)
    textSize(32)
    textAlign(CENTER)
    text("click please :)", width/2, height/2)
    
def mousePressed():
    link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i10i512l2j0i10i433i512j0i10i512l2j0i10i433i512l2j0i10i512j0i10i433i512.3017j0j7&sourceid=chrome&ie=UTF-8")
