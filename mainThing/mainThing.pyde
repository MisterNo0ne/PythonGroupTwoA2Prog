import enemy
import item
import npc
import obstacle
import player
#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling
gameState = "fight"

def setup():
    size(400, 600)

    gameState = "map"
    
    
    
    #zacks stuff
    ghoul = enemy(50,"ghoul")

    
    #initialize variables
    global gameState
    #global block
    global ghoul
    gameState = "map"
    #block = obstacle(100, 100, 50, 25)
   # ghoul = enemy(50, "ghoul", "ice")
    #print(str(ghoul.health))

def draw():
    background(0)
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)

       # block.display(True)
        

    
    
