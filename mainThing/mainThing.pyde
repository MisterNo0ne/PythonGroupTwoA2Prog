import enemy
import item
import obstacle
import player
import npc

#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

#Element list: ice, water, rock, poison, fire, electric, grass

def setup():
    size(400, 600)
    
    #initialize variables
    gameState = "map"
    block = obstacle(100, 100, 50, 25)
    #ghoul = enemy(50, "ghoul", "ice")

def draw():
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)
        obstacle.display(True)
        
    
    
