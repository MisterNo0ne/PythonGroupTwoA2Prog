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

def draw():
    background(0)
    textSize(32)
    textAlign(CENTER)
    text("click please :)", width/2, height/2)
    if gameState == "fight":
        background(100)
    else: #gameState is in map mode
        background(0, 200, 0)
    
def mousePressed():
    link("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
