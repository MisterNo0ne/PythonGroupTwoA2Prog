
#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

def setup():
    size(400, 600)
    
    global gameState
    gameState = "map"
    
    
    #zacks stuff
    #ghoul = enemy(50,"ghoul")

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
    link("http://www.agar.io")
