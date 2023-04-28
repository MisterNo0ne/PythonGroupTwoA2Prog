from enemy import Enemy
from item import Item
from npc import Npc
from obstacle import Obstacle
from player import Player

#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

def setup():
    size(600, 600)
    
    global gameState, ghoul, skeleton, zombie, spider, block, debugMode, gamer, keyPresses, bkgrnd, enemyList, freeRam, currentEnemy, skltnimg, ghlimg, spdrimg, zomimg
    skltnimg = loadImage("Player.png")
    zomimg = loadImage("Player.png")
    spdrimg = loadImage("smallenemyspider.png")
    ghlimg = loadImage("spookyGhoul.png")
    bkgrnd = loadImage("grassBackground.png")
    gameState = "map"
    currentEnemy= -1
    
    #testing to see if enemy being called and enemy being hit works
    ghoul = Enemy(50, "ghoul", "fire", 500, 500, ghlimg)
    skeleton = Enemy(100, "skeleton", "ice", 100, 400, skltnimg)
    spider = Enemy(42, "spider", "poison", 200, 200, spdrimg)
    zombie = Enemy(153, "zombie", "water", 300,100, zomimg)
    block = Obstacle(100, 100, 300, 100)
    debugMode = True #displays obstacles
    freeRam = False
    gamer = Player(width/2, height/2, 100)
    keyPresses = [False, False, False, False]
    
    #Enemy list is a list of all of the enemies, and grows with each time we add a new enemy 
    #Later on we can add something so that if any item in this list is off screen we don't render it
    enemyList = [ghoul, skeleton, spider, zombie]
    
    
    

def draw():
    global gameState, currentEnemy, enemyList, ghoul, skeleton
    #??????????????????????????????????????????????????????
    #if you wanna edit values of global variables ig you have to put them here lmao
    #i spent an hour and a half here i stg this is so dumb
    
    background(0)
    if gameState == "fight":
        
        background(200)
        gamer.showInFight()
        textSize(24)
        fill(0)
        text("Health bar of player here \n" + str(gamer.health), 340, 550)
        text("place to type spell here", 340, 480)
        text("Enemy health: " + str(enemyList[currentEnemy].health) + " ", 50, 50)
        text("type: " + enemyList[currentEnemy].type + "\n enemyID: " + str(currentEnemy) + "\nsd enemy element: " + enemyList[currentEnemy].element, 50, 120)
        textSize(32)
        text("enemy here", 425, 90)
        if enemyList[currentEnemy].health<=0:
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            
    else: #gameState is in map mode
        image(bkgrnd,-gamer.mapPosX,-gamer.mapPosY)
        if freeRam:
            textSize(32)
            textAlign(RIGHT)
            text("click here please :)", width-25, height-30)
        block.display(debugMode)
        gamer.showOnMap()
        gamer.moveOnMap(keyPresses)
        for e in enemyList:
            e.mapDisplay(gamer.mapPosX, gamer.mapPosY)
            if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, e.mapPosX-50, e.mapPosY-50, 100, 100): 
                currentEnemy = enemyList.index(e)
                print("you ran into a " + enemyList[currentEnemy].element +" " + enemyList[currentEnemy].type + " D:")
                gameState = "fight"
        
def mousePressed():
    if gameState == "map" and mouseY > height-100 and mouseX > width-300 and freeRam:
        link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i512j0i10i512l6j0i512l2.2697j0j7&sourceid=chrome&ie=UTF-8")
    elif gameState == "fight":
        enemyList[currentEnemy].hit(20,["water","grass"]) 
    
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
        
def pointInsideRectangle(a, b, x, y, w, h):
    # just returns whether or not the coordinate of the first 2 parameters is in the rectangle defined by the last 4 parameters
    return ((a>x) and (a<x+w)) and ((b>y) and (b<y+h))
