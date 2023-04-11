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
    
    global gameState, ghoul, block, debugMode, gamer, keyPresses, bkgrnd
    bkgrnd = loadImage("grassBackground.png")
    image(bkgrnd,0,0)
    gameState = "map"
    
    #testing to see if enemy being called and enemy being hit works
    ghoul = Enemy(50,"ghoul", "fire",500,500)
    ghoul.hit(20,["water","rock"])
    block = Obstacle(100, 100, 300, 100)
    debugMode = True #displays obstacles
    gamer = Player(width/2, height/2)
    keyPresses = [False, False, False, False]

def draw():
    background(0)
    if gameState == "fight":
        background(200)
    else: #gameState is in map mode
        background(0, 200, 0)
        # --- 
        textSize(32)
        textAlign(RIGHT)
        text("click here please :)", width-25, height-30)
        # ---
        block.display(debugMode)
        gamer.showOnMap()
        gamer.moveOnMap()
        ghoul.mapDisplay()
def mousePressed():
    if gameState == "map" and mouseY > height-100 and mouseX > width-300:
        link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i512j0i10i512l6j0i512l2.2697j0j7&sourceid=chrome&ie=UTF-8")
    
def keyPressed():
    if key == 'w':
        keyPresses[0] = True
    if key == 'a':
        keyPresses[1] = True
    if key == 's':
        keyPresses[2] = True
    if key == 'd':
        keyPresses[3] = True
    
def keyReleased():
    if key == 'w':
        keyPresses[0] = False
    if key == 'a':
        keyPresses[1] = False
    if key == 's':
        keyPresses[2] = False
    if key == 'd':
        keyPresses[3] = False
