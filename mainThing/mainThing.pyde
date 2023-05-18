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
    #Store mode: player buying stuff from store guy/blacksmith(?)

def setup():
    size(600, 600)
    frameRate(24)
    print("hello gamer welcom to epic spell adventure game smiley face =)")
    #don't ask
    global gameState, ghoul, skeleton, zombie, spider, debugMode, gamer, keyPresses, bkgrnd, enemyList, freeRam, currentEnemy, skltnimg, ghlimg, spdrimg, zomimg, attacktype, turn, blocks, fightbackground, animationWaitTimer, endWaiting, attackImage, turn1wait, turn2wait, turn3wait, wizard, cactus, cactusimg, hpotcount, daggercount, chestimg, chestopened, amogus, sandBoss, sandimg, skltnbossimg, castleimg, skltnBoss, castleBoss, hasArmor, blockFile, coins, merchant, shopimg, hasRock, shopBackground
    
    #load files
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
    skltnbossimg = loadImage("Skeleton Boss.png")
    castleimg = loadImage("evilCastle.png")
    blockFile = loadStrings("blockData.txt")
    merchant = loadImage("Shopkeeper.png")
    shopimg = loadImage("Shop.png")
    shopBackground = loadImage("grassBackground.png")
    #other stuff
    
    chestopened = False
    gameState = "map"
    currentEnemy= -1
    attackType = []
    hasArmor = False
    coins = 10.0
    hasRock = False
    
    #enemy declarators or smth
    ghoul = Enemy(50, "ghoul", "fire", 500, 500, ghlimg, "none", 20, False)
    skeleton = Enemy(100, "skeleton", "grass", 200, 400, skltnimg, "none", 20, False)
    spider = Enemy(42, "spider", "fire", 200, 200, spdrimg, "none", 20, False)
    zombie = Enemy(153, "zombie", "water", 300, 100, zomimg, "none", 20, False)
    cactus = Enemy(200, "cactus", "grass", 150, 300, cactusimg, "none", 30, False)
    sandBoss = Enemy(300, "Sand Boss", "fire", 300, 1400, sandimg, "none", 40, True)
    skltnBoss = Enemy(400, "Skeleton Boss", "grass", 2200, 1600, skltnbossimg, "none", 40, True)
    castleBoss = Enemy(500, "Final Boss", "fire", 1600, 200, castleimg, "none", 50, True)
    enemyList = [ghoul, skeleton, spider, zombie, cactus, sandBoss, skltnBoss, castleBoss] 
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
    global gameState, currentEnemy, enemyList, ghoul, skeleton, turn, animationWaitTimer, gamer, endWaiting, attackType, waitTimer, chestimg, daggercount, hpotcount, chestopened, hasArmor, coins, merchant, shoping, hasRock, shopBackground
    #??????????????????????????????????????????????????????
    #if you wanna edit values of global variables you have to put them here
    
#-------------------------------------------------------------------------------FIGHT MODE-------------------------------------------------------------------

    if gameState == "fight":
        # Display logic
        #background(200)
        image(fightbackground, 0, 0, width, height)
        
        gamer.showInFight()
        
        #rendering the attack buttons yayayy
        textSize(18)
        #fire
        fill(245,141,12)
        rect(350,400,100,25)
        fill(0)
        text("fire", 370,400,100,25)
        #water
        fill(127,97,252)
        rect(475,400,100,25)
        fill(0)
        text("water", 495,400,100,25)
        #grass
        fill(44,185,17)
        rect(350,450,100,25)
        fill(0)
        text("grass", 370,450,100,25)
        #dagger
        fill(127)
        rect(475,450,100,25)
        fill(0)
        text("dagger", 495,450,100,25)
        
        
        #lightning
        fill(202,176,25)
        rect(350,350,100,25)
        fill(0)
        text("lightning", 370,350,100,25)
        #ice
        fill(8,187,209)
        rect(475,350,100,25)
        fill(0)
        text("ice", 495,350,100,25)
        #rock
        if hasRock: 
            fill(113,80,81)
            rect(225,350,100,25)
            fill(0)
            text("rock", 245,350,100,25)
        
        fill(255)
        noStroke()
        rect(45, 25, 250, 250) #highlight box
        fill(0)
        textSize(18)
        text("Player health: " + str(gamer.health) + "/" + str(gamer.maxHealth), 350, 525)
        textSize(24)
        
        if debugMode:
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
        fill(255)
        text("You have " + str(daggercount) + " daggers!", width-200, height-30)
        text("You have " + str(hpotcount) + " health potions!", width-520, height-30)
        textSize(32)
        
        text(str(animationWaitTimer), width-100, 100)
        text(str(turn), width-100, 140)
        
        
            ##KILLED ENEMY LOGIC
        if endWaiting or enemyList[currentEnemy].health<=0: 
            if enemyList[currentEnemy].isBoss == True: 
                print("yippee you killed the " + enemyList[currentEnemy].type + " congrations you (probably) got loot!11!!11!")
                hpotcount+=5
                daggercount+=5
                coins+=90
                #if hasArmor == False:
                 #   print("You found an iron chestplate! This will provide 25% damage reduction from enemy attacks!") 
                  #  hasArmor = True
                if enemyList[currentEnemy].type == "Sand Boss": 
                    hasRock = True
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            endWaiting = False
            #coins += (0.5*enemyList[currentEnemy].health)    <-- idea is the amount of gold u get scales with enemy hp
            coins+=10
            turn = 1
            animationWaitTimer = 0
## 2nd turn 
        ##Displays gamer's attack
        timeForAnim = 30 #only the first 30 frames will get the animation
        if turn == 2 and animationWaitTimer >= turn1wait-timeForAnim and attackType[0] != "heal":
            #ellipse(160, 440, 20, 20)
            progressFraction = float(turn1wait-animationWaitTimer)/timeForAnim
            pushMatrix()
            translate(160+(progressFraction*200), 440-(progressFraction*200))
            rotate(radians(315)) #rotates to make the attack diagonal
            image(attackImage, 0, 0, 75, 75) #player attacking
            popMatrix()
        
        
        ##PLAYER HIT LOGIC
        if turn == 2 and animationWaitTimer == 0:
            enemyHitDamage = enemyList[currentEnemy].strength
            if hasArmor == True: 
                enemyHitDamage *= 0.75
            if enemyList[currentEnemy].status == "frozen" or (enemyList[currentEnemy].element == "fire" and enemyList[currentEnemy].status == "wet"): 
                enemyHitDamage *= 0.6
            gamer.health -= enemyHitDamage
            println("The gamer was hurt for " + str(enemyHitDamage) + " damage!")
            turn = 3
            animationWaitTimer = turn2wait
            
            ##ENEMY HIT LOGIC
        if animationWaitTimer == 20 and turn == 2: 
            if attackType[0] == "none": 
                enemyList[currentEnemy].hit(50, attackType) 
            elif attackType[0] == "heal": 
                rect(0,0,0,0)
            elif attackType[0] == "lightning" or attackType[0] == "rock": 
                enemyList[currentEnemy].hit(30, attackType)
            else: 
                enemyList[currentEnemy].hit(20, attackType)
        
## 3rd turn
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
            print("Your health is now " + str(gamer.health) + " out of " + str(gamer.maxHealth))
            if enemyList[currentEnemy].health<=0:
                print("The enemy died!")
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

    elif gameState == "map": #gameState is in map mode
        gamer.moveOnMap(keyPresses, blocks)
        
        background(12, 89, 183)
        image(bkgrnd,(width/2)-gamer.mapPosX,(height/2)-gamer.mapPosY)
        
        #rendering inventory box (currently just health pots and daggers): 
        stroke(0)
        strokeWeight(4)
        fill(120,60,60)
        rect(0,height-100, 250, 100)
        fill(0)
        textSize(28)
        text(str(daggercount) + " daggers", 5, height-65)
        text(str(hpotcount) + " health potions", 5, height-20)
        text(str(coins) + " coins", 133, height-65)
        if hasArmor == True: 
            text("iron armor", 5, height-100)
        if chestopened == False:      #<-- this would mean deleting the chest but that might look weird
            image(chestimg, 380-gamer.mapPosX+(width/2), 160-gamer.mapPosY+(height/2)+50, 75, 75 )   
        
        #so currently chest hitbox is super jank sorry
        if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, 450-gamer.mapPosX+(width/2), 150-gamer.mapPosY+(height/2)+50, 75, 75) and chestopened == False: 
            daggercount+=10
            hpotcount+=10
            chestopened = True
        gamer.showOnMap()
        
        image(merchant, 1600-gamer.mapPosX+(width/2), 1600-gamer.mapPosY+(height/2), 100, 100) # this aint rendering fo same reason
        image(shopimg, 1700-gamer.mapPosX+(width/2), 1615-gamer.mapPosY+(height/2), 150, 150)
        fill(0)
        textSize(22)
        text("Merchant", 1610-gamer.mapPosX+(width/2), 1710-gamer.mapPosY+(height/2))
        # fixed the hitbox :)
        if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, 2900-gamer.mapPosX+(width/2), 2870-gamer.mapPosY+(height/2), 200, 230): 
            print("You entered the merchant's shop!")
            gameState = "store"
            
        for e in enemyList:
            e.mapDisplay(gamer.mapPosX, gamer.mapPosY)
            if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, e.mapPosX, e.mapPosY, 100, 100) and gamer.health>0: 
                currentEnemy = enemyList.index(e)
                print(" ==-== " + enemyList[currentEnemy].element + " " + enemyList[currentEnemy].type + " ==-== ")
                gameState = "fight"
                
        if debugMode:
            for o in blocks:
                o.display(gamer.mapPosX, gamer.mapPosY)
#-------------------------------------------------------STORE MODE--------------------------------------------------------------------#
    else: #gameState is in store mode
        #i have no clue what to do here yet, prolly something similar to fight mode though where if u have coins and
        #if u click in the boxes then u buy stuff and also render some store guy toob
        background(127)
        image(shopBackground,0,0,600,600)
        image(shopimg, 375, 100, 300, 300)
        image(merchant, 300, 200, 100, 100)
        fill(255)
        stroke(0)
        strokeWeight(4)
        rect(50,50,220,110)
        fill(120,60,60)
        rect(0,height-100, 250, 100)
        fill(0)
        textSize(22)
        text("Welcome to my shop. \nFeel free to  buy \nanything you need!", 60, 75)
        textSize(28)
        text(str(daggercount) + " daggers", 5, height-65)
        text(str(hpotcount) + " health potions", 5, height-20)
        text(str(coins) + " coins", 133, height-65)
        if hasArmor == True: 
            text("iron armor", 5, height-100)
        textSize(22)
        #hpot
        fill(200,50,50)
        rect(100,400,100,25)
        fill(0)
        text("1 health potion", 100, 390)
        
        fill(127)
        #dagger
        rect(250,400,100,25)
        #armor
        rect(400,400,100,25)
        fill(0)
        text("1 dagger", 250, 390)
        if hasArmor == False: 
            text("Iron armor", 400, 390)
        elif hasArmor == True: 
            text("Sold out!", 400, 390)
        #Exit button
        fill(200,50,50)
        rect(500,500,100,25)
        fill(0)
        text("Exit to map", 450, 490)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def mousePressed():
    global turn, attackImage, animationWaitTimer, attackType, daggercount, hasRock, hpotcount, coins, hasArmor, gameState, gamer
    if gameState == "map" and mouseY > height-100 and mouseX > width-300 and freeRam:
        link("https://www.google.com/search?q=download+free+ram&rlz=1C5GCEA_enUS1042US1042&oq=download+free+ram&aqs=chrome..69i57j0i512j0i10i512l6j0i512l2.2697j0j7&sourceid=chrome&ie=UTF-8")
    if gameState == "store": 
        if pointInsideRectangle(mouseX, mouseY, 100,400,100,25) and coins>=5:
            hpotcount+=1
            coins-=5
        if pointInsideRectangle(mouseX, mouseY, 250,400,100,25) and coins>=5:
            daggercount+=1
            coins-=5
        if pointInsideRectangle(mouseX, mouseY, 400,400,100,25) and coins>=100 and hasArmor == False:
            hasArmor = True
            coins-=100
        if pointInsideRectangle(mouseX, mouseY, 500,500,100,25):
            gameState = "map"
            gamer.mapPosX=1650
            gamer.mapPosY=1750
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
        if pointInsideRectangle(mouseX, mouseY, 475, 350, 100, 25):
            attackImage = loadImage("icicleAttack.png")
            attackType = ["ice", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideRectangle(mouseX, mouseY, 350, 350, 100, 25):
            attackImage = loadImage("lightningBolt.png")
            attackType = ["lightning", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideRectangle(mouseX, mouseY, 225, 350, 100, 25) and hasRock:
            attackImage = loadImage("rock1.png")
            attackType = ["rock", "none"]
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
    global gamer, hpotcount, amogus, daggercount, turn, attackImage, gameState, attackType, animationWaitTimer, turn1wait
    if key == 'w':
        keyPresses[0] = False
    if key == 'a':
        keyPresses[1] = False
    if key == 's':
        keyPresses[2] = False
    if key == 'd':
        keyPresses[3] = False
    if key == 'h' and hpotcount>0 and turn == 1 and gameState == "fight": 
        print("You used a health potion! You healed 30 hp!")
        gamer.health+=30
        hpotcount-=1
        attackImage = loadImage("LeafAttack.png")
        attackType = ["heal", "none"]
        turn = 2
        animationWaitTimer = turn1wait
    if key == 'v' and amogus: 
        hpotcount+=1
    if key == 'q' and amogus: 
        daggercount+=1
        
def pointInsideRectangle(a, b, x, y, w, h):
    # just returns whether or not the coordinate of the first 2 parameters is in the rectangle defined by the last 4 parameters
    return ((a>x) and (a<x+w)) and ((b>y) and (b<y+h))


#don't ask idk either
def makeBlocks():
    for vals in blockFile:
        valList = []
        while len(valList) < 3:
            index = 0
            while vals[index] != ' ':
                index += 1
            valList.append(float(vals[:index]))
            vals = vals[index+1:]
        valList.append(float(vals))
        blocks.append(Obstacle(valList[0], valList[1], valList[2], valList[3]))
        
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
            return "wet"
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
        if enemyType == "water": 
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
    return "somefin happend idk what (this is a placeholder for no status being inflicted :P)"
