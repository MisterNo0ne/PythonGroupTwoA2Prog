from enemy import Enemy
from item import Item
from npc import Npc
from obstacle import Obstacle
from player import Player

# **for right now, I have multipled speed by 10 for testing purposes**
# **for right now smiley face i promise

#2 Main game states that always need to be separated:
    #Map mode: player walking around a map
    #Fight mode: player battling

def setup():
    size(600, 600)
    frameRate(24)
    
    #don't ask
    global gameState, ghoul, skeleton, zombie, spider, debugMode, gamer, keyPresses, bkgrnd, enemyList, freeRam, currentEnemy, skltnimg, ghlimg, spdrimg, zomimg, attacktype, turn, blocks, fightbackground, animationWaitTimer, endWaiting, attackImage, turn1wait, turn2wait, turn3wait, wizard, cactus, cactusimg, hpotcount, daggercount, chestimg, chestopened, amogus, sandBoss, sandimg
    
    #load images
    fightbackground = loadImage("epicfightbackground.jpeg")
    skltnimg = loadImage("skeletonIdle.png")
    zomimg = loadImage("Zombie.png")
    spdrimg = loadImage("smallenemyspider.png")
    ghlimg = loadImage("spookyGhoul.png")
    bkgrnd = loadImage("MapBackground.png")
    wizard = loadImage("Wizard.png")
    cactusimg = loadImage("Angry buff cactus.png") 
    chestimg = loadImage("chest.png")
    sandimg = loadImage("sandboss.png")
    #other stuff
    chestopened = False
    gameState = "map"
    currentEnemy= -1
    attackType = []
    
    #enemy declarators or smth
    ghoul = Enemy(50, "ghoul", "fire", 500, 500, ghlimg, "none", 20, False)
    skeleton = Enemy(100, "skeleton", "grass", 100, 400, skltnimg, "none", 20, False)
    spider = Enemy(42, "spider", "fire", 200, 200, spdrimg, "none", 20, False)
    zombie = Enemy(153, "zombie", "water", 300, 100, zomimg, "none", 20, False)
    cactus = Enemy(200, "cactus", "grass", 150, 300, cactusimg, "none", 30, False)
    sandBoss = Enemy(300, "sandBoss", "fire", 300, 1400, sandimg, "none", 40, True)
    enemyList = [ghoul, skeleton, spider, zombie, cactus, sandBoss] 
    hpotcount = 0
    daggercount = 0 #these will both change after bosses or smth like that yay
    
    #amogus is like hax mode, where during this u can hack in more health pots and daggers and funi stuff
    amogus  = True
    
    blocks = []
    makeBlocks()
    
    gamer = Player(400, 400, 100, wizard) 
    
    turn1wait = 50
    turn2wait = 30
    turn3wait = 60
    animationWaitTimer = 0
    endWaiting = False
    
    debugMode = True #displays obstacles
    freeRam = False
    keyPresses = [False, False, False, False]
    turn = 1
    attackImage = loadImage("WaterBolt.png")
    waitTimer = 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def draw():
    global gameState, currentEnemy, enemyList, ghoul, skeleton, turn, animationWaitTimer, gamer, endWaiting, attackType, waitTimer,chestimg, daggercount, hpotcount
    #??????????????????????????????????????????????????????
    #if you wanna edit values of global variables you have to put them here
    
#-------------------------------------------------------------------------------FIGHT MODE-------------------------------------------------------------------

    if gameState == "fight":
        # Display logic
        background(200)
        image(fightbackground, 0, 0, width, height)
        
        gamer.showInFight()
        
        #rendering the grass, fire, and water attack buttons yayayy
        fill(245,141,12)
        rect(350,400,100,25)
        fill(127,97,252)
        rect(475,400,100,25)
        fill(44,185,17)
        rect(350,450,100,25)
        fill(127)
        rect(475,450,100,25)
        
        fill(255)
        noStroke()
        rect(45, 25, 250, 250) #highlight box
        textSize(24)
        fill(0)
        text("Enemy health: " + str(enemyList[currentEnemy].health) + " ", 50, 50)
        text("type: " + enemyList[currentEnemy].type + "\n enemyID: " + str(currentEnemy) + "\n enemy element: " + enemyList[currentEnemy].element, 50, 120)
        text("status: " + enemyList[currentEnemy].status, 50, 240)
        enemyList[currentEnemy].display(enemyList[currentEnemy].img)
        enemyList[currentEnemy].displayStatus()
        textSize(32)
        stroke(0)
        
        enemyList[currentEnemy].healthBarInFight()
        # Turn logic
        animationWaitTimer -= 2 if animationWaitTimer>0 else 0 #decrement the wait timer if it's above 0
        textSize(20)
        text("You have " + str(daggercount) + " daggers!", width-200, 25)
        textSize(32)
        text(str(animationWaitTimer), width-100, 100)
        text(str(turn), width-100, 140)
        
        if animationWaitTimer == 20 and turn == 2: 
            if attackType[0] == "none": 
                enemyList[currentEnemy].hit(40, attackType) 
            else: 
                enemyList[currentEnemy].hit(20, attackType)
            
        if endWaiting or enemyList[currentEnemy].health<=0: 
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            endWaiting = False
        #    gamer.health = gamer.maxHealth    why would they heal? shouldn't we have health potions or smth idk
            turn = 1
            animationWaitTimer = 0
            
        ##Displays gamer's attack
        timeForAnim = 30 #only the first 30 frames will get the animation
        if turn == 2 and animationWaitTimer >= turn1wait-timeForAnim:
            #ellipse(160, 440, 20, 20)
            progressFraction = float(turn1wait-animationWaitTimer)/timeForAnim
            pushMatrix()
            translate(160+(progressFraction*200), 440-(progressFraction*200))
            rotate(radians(315)) #rotates to make the attack diagonal
            image(attackImage, 0, 0, 75, 75) #player attacking
            popMatrix()
        ##Makes gamer get hurt
        if turn == 2 and animationWaitTimer == 0:
            enemyHitDamage = enemyList[currentEnemy].strength
            gamer.health -= enemyHitDamage
            println("The gamer was hurt for " + str(enemyHitDamage) + " damage!")
            turn = 3
            animationWaitTimer = turn2wait
        
        ##Displays player hurting
        if turn == 3 and animationWaitTimer != 0:
            #player getting hurt
            casdfawefawsdfawef = 1
        ##Resolve statuses
        if turn == 3 and animationWaitTimer == 0:
            enemyFighting = enemyList[currentEnemy]
            
            healthChange = fightTurnThreeHealth(enemyFighting.status, enemyFighting.element)
            displayText = fightTurnThreeDisplayText(enemyFighting.status, enemyFighting.element)
            if healthChange > 0:
                displayText += " Your attack healed the enemy by "
                displayText += str(healthChange) + " health."
            elif healthChange < 0:
                displayText += " Your attack hurt the enemy for an additional "
                displayText += str(-healthChange) + " damage."
            
            print(displayText)
            enemyFighting.health += healthChange
            enemyFighting.status = fightTurnThreeStatus(enemyFighting.status, enemyFighting.element)
            turn = 1
            
            # Enemy death logic
            print("The enemy's health is now " + str(enemyFighting.health))
            if enemyList[currentEnemy].health<=0:
                print("The enemy's health dropped below 0, and it died!")
                print("\nBack to the map...\n")
                endWaiting = True
                animationWaitTimer = turn3wait
            else:
                print(" ==-== New Cycle ==-==")
        
            # Gamer death logic
        if gamer.health<=0:
            print("oh no!1!11!1!11 uy deied!!11! you are loser L game over")
            gameState = "map"
            gamer.mapPosX = 400
            gamer.mapPosX = 400
            gamer.health = gamer.maxHealth
    
            """
        if turn == 1 and animationWaitTimer == 0 and endWaiting:
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            endWaiting = False
            gamer.health = gamer.maxHealth
            """
#----------------------------------------------------------------------MAP MODE------------------------------------------------------------------------------

    else: #gameState is in map mode
        gamer.moveOnMap(keyPresses)
        background(0, 0, 255)
        image(bkgrnd,(width/2)-gamer.mapPosX,(height/2)-gamer.mapPosY)
        
        #rendering inventory box (currently just health pots and daggers): 
        stroke(0)
        strokeWeight(4)
        fill(120,60,60)
        rect(0,height-100, 200, 100)
        fill(0)
        textSize(28)
        text(str(daggercount) + " daggers", 5, height-65)
        text(str(hpotcount) + " health potions", 5, height-20)
        
        
        #i actually have zero clue why chest aint rendering ;-;
        image(chestimg, 50, 50, 75, 75)   
        gamer.showOnMap()
        
        for e in enemyList:
            e.mapDisplay(gamer.mapPosX, gamer.mapPosY)
            if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, e.mapPosX-50, e.mapPosY-50, 100, 100) and gamer.health>0: 
                currentEnemy = enemyList.index(e)
                print(" ==-== " + enemyList[currentEnemy].element + " " + enemyList[currentEnemy].type + " ==-== ")
                gameState = "fight"
                
        if debugMode:
            for o in blocks:
                o.display(gamer.mapPosX, gamer.mapPosY)
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def mousePressed():
    global turn, attackImage, animationWaitTimer, attackType, daggercount
    if gameState == "map" and mouseY > height-100 and mouseX > width-300 and freeRam:
        link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i512j0i10i512l6j0i512l2.2697j0j7&sourceid=chrome&ie=UTF-8")
    elif gameState == "fight" and gamer.health>=1 and turn == 1:
        if pointInsideRectangle(mouseX, mouseY, 475,450,100,25) and daggercount>0: 
            attackImage = loadImage("epicSword.png")
            attackType = ["none", "none"]
            daggercount-=1
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideRectangle(mouseX, mouseY, 350, 400, 100, 25):
            attackImage = loadImage("FireBall.png")
            attackType = ["fire", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideRectangle(mouseX, mouseY, 475, 400, 100, 25):
            attackImage = loadImage("WaterBolt.png")
            attackType = ["water", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideRectangle(mouseX, mouseY, 350, 450, 100, 25):
            attackImage = loadImage("LeafAttack.png")
            attackType = ["grass", "none"]
            turn = 2
            animationWaitTimer = turn1wait
            
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
    global gamer, hpotcount, amogus, daggercount
    if key == 'w':
        keyPresses[0] = False
    if key == 'a':
        keyPresses[1] = False
    if key == 's':
        keyPresses[2] = False
    if key == 'd':
        keyPresses[3] = False
    if key == 'h' and hpotcount>0: 
        gamer.health+=20
        hpotcount-=1
    if key == 'v' and amogus: 
        hpotcount+=1
    if key == 'q' and amogus: 
        daggercount+=1
        
def pointInsideRectangle(a, b, x, y, w, h):
    # just returns whether or not the coordinate of the first 2 parameters is in the rectangle defined by the last 4 parameters
    return ((a>x) and (a<x+w)) and ((b>y) and (b<y+h))

def makeBlocks():
    blocks.append(Obstacle(0, 0, 400, 200))
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------    
"""
processing python doesn't have a case switch option so these type charts are horribly ugly; do not venture below unless you want a headache
https://processing.org/reference/switch.html
https://www.pythonpool.com/match-case-python/
"""
def fightTurnThreeStatus(enemyStatus, enemyType):
    if enemyStatus == "burning": 
        if enemyType == "fire": 
            return "none"
        if enemyType == "water": 
            return "none"
        if enemyType == "grass": 
            return "burning"
    if enemyStatus == "wet": 
        if enemyType == "fire":   
            return "none"
        if enemyType == "water": 
            return "none"
    if enemyStatus == "tangled": 
        if enemyType == "fire": 
            return "none"
        if enemyType == "water": 
            return "overgrown"
    if enemyStatus == "overgrown": 
        if enemyType == "fire": 
            return "none"
    return enemyStatus
            
def fightTurnThreeHealth(enemyStatus, enemyType):
    if enemyStatus == "burning":   
        if enemyType == "fire": 
            return 20 #fire helps fire
        elif enemyType == "grass": 
            return -20 #fire hurts grass
    elif enemyStatus == "wet": 
        if enemyType == "fire": 
            return -20 #water hurts fire
        elif enemyType == "water": 
            return 20 #water helps water
        elif enemyType == "grass": 
            return 20 #water helps grass
    elif enemyStatus == "tangled":  
        if enemyType == "grass": 
            return 20 #grass helps grass
    elif enemyStatus == "overgrown": 
        if enemyType == "water": 
            return -40 #grass hurts water
    return 0

def fightTurnThreeDisplayText(enemyStatus, enemyType):
    if enemyStatus == "burning": 
        if enemyType == "fire": 
            return "The enemy grows stronger from more flames!"
        if enemyType == "water": 
            return "The flames die out quickly."
        if enemyType == "grass": 
            return "The enemy bursts into flames!"
    if enemyStatus == "wet": 
        if enemyType == "fire": 
            return "The water douses the flames!"
        if enemyType == "water": 
            return "The enemy grows stronger from more water!"
        if enemyType == "grass": 
            return "The plants grow stronger from the water!"
    if enemyStatus == "tangled": 
        if enemyType == "fire": 
            return "How did you tangle a fire enemy that's stupid"
        if enemyType == "water": 
            return "The enemy shrivels and the vines grow enormous!"
        if enemyType == "grass": 
            return "Your grassy vines remain."
    if enemyStatus == "overgrown": 
        if enemyType == "fire": 
            return "How did you tangle a fire enemy that's stupid"
        if enemyType == "water": 
            return "The enemy becomes much dryer!"
        if enemyType == "grass": 
            return "Your grassy vines remain."
    return "somefin happend idk what"
