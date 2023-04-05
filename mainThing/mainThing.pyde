
#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling
gameState = "fightgvbjhjknnh"

def setup():
    size(400, 600)
    gameState = "map"
    
    
    
    #zacks stuff
    ghoul = enemy(50,"ghoul")

def draw():
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)
    
    
