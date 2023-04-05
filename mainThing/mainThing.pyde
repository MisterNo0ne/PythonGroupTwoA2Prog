
#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling
gameState = "fight"

def setup():
    size(400, 600)
    gameState = "map"


def draw():
    if gameState == "fight":
        print(gameState)
    else: #gameState is in map mode
        print(gameState)
    
