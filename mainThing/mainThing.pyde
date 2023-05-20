from enemy import Enemy
from item import Item
from npc import Npc
from obstacle import Obstacle
from player import Player
from sign import Sign

#why can you freeze a water type hello??

def setup():
    size(600, 600)
    frameRate(24)
    print("hello gamer welcom to epic spell adventure game smiley face =)")
    #don't ask
    global gameState, ghoul, skeleton, zombie, spider, debugMode, gamer, keyPresses, bkgrnd, enemyList, currentEnemy, skltnimg, ghlimg, spdrimg, zomimg, attacktype, turn, blocks, fightbackground, animationWaitTimer, endWaiting, attackImage, turn1wait, turn2wait, turn3wait, wizard, cactus, cactusimg, hpotcount, daggercount, chestimg, chestopened, amogus, sandBoss, sandimg, skltnbossimg, castleimg, skltnBoss, castleBoss, hasArmor, blockFile, coins, merchant, shopimg, hasRock, shopBackground, signimg, signs, bushBlock, sandBlock, skeletonBossBeaten, sandBossBeaten, icons, itemsOwned
    
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
    signimg = loadImage("Sign.png")
    bushBlock = loadImage("Bush Blocking area.png")
    sandBlock = loadImage("Sandstone blocking area.png")
    icons = []
    icons.append(loadImage("icons/Fire Icon.png"))
    icons.append(loadImage("icons/Water Icon.png"))
    icons.append(loadImage("icons/Grass Icon.png"))
    icons.append(loadImage("icons/Lightning Icon.png"))
    icons.append(loadImage("icons/Ice Icon.png"))
    icons.append(loadImage("icons/Rock Icon.png"))
    icons.append(loadImage("icons/Poison Icon.png"))
    
    #enemy declarators or smth
    ghoul = Enemy(50, "ghoul", "fire", 500, 500, ghlimg, "none", 20, False)
    skeleton = Enemy(100, "skeleton", "grass", 200, 400, skltnimg, "none", 20, False)
    spider = Enemy(42, "spider", "fire", 200, 200, spdrimg, "none", 20, False)
    zombie = Enemy(153, "zombie", "water", 300, 100, zomimg, "none", 20, False)
    cactus = Enemy(200, "cactus", "grass", 150, 300, cactusimg, "none", 30, False)
    sandBoss = Enemy(300, "Sand Boss", "fire", 300, 1400, sandimg, "none", 40, True)
    skltnBoss = Enemy(400, "Skeleton Boss", "grass", 2500, 1600, skltnbossimg, "none", 40, True)
    castleBoss = Enemy(500, "Final Boss", "fire", 1600, 200, castleimg, "none", 50, True)
    enemyList = [ghoul, skeleton, spider, zombie, cactus, sandBoss, skltnBoss, castleBoss] 
    hpotcount = 0
    daggercount = 0 #these will both change after bosses or smth like that yay
    
    gamer = Player(400, 400, 100, wizard) 

    
    itemsOwned = []
    itemsOwned.append(Item("Coins", 0, 20.0))
    itemsOwned.append(Item("Health Pots", 0, 0))
    itemsOwned.append(Item("Daggers", 0, 0))
    itemsOwned.append(Item("Armor", 0, "leather"))
    
    blocks = []
    makeBlocks()
    
    signs = []
    signs.append(Sign(725, 600, "This is a sign", signimg, 32, 1))
    signs.append(Sign(725, 700, "This is a sign\nwith a line break :O", signimg, 16, 2))
    signs.append(Sign(725, 800, "Two\nline\nbreaks", signimg, 12, 3))
    signs.append(Sign(725, 900, "Small text with one line wowie", signimg, 10, 1))
    
    #animations
    turn1wait = 50
    turn2wait = 30
    turn3wait = 60
    animationWaitTimer = 0
    endWaiting = False

    #other stuff
    gameState = "map"
    attackType = []
    currentEnemy= -1
    coins = 10.0
    chestopened = False
    hasArmor = False
    hasRock = False
    amogus  = True #amogus is like hax mode, where during this u can hack in more health pots and daggers and funi stuff
    debugMode = True 
    skeletonBossBeaten = False
    sandBossBeaten = False
    keyPresses = [False, False, False, False]
    turn = 1
    attackImage = loadImage("WaterBolt.png")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def draw():
    global gameState, currentEnemy, enemyList, ghoul, skeleton, turn, animationWaitTimer, gamer, endWaiting, attackType, chestimg, daggercount, hpotcount, chestopened, hasArmor, coins, merchant, shoping, hasRock, shopBackground, signs, sandBossBeaten, skeletonBossBeaten
    #??????????????????????????????????????????????????????
    #if you wanna edit values of global variables you have to put them here
    
#-------------------------------------------------------------------------------FIGHT MODE-------------------------------------------------------------------
    
    if gameState == "fight":
        # Display logic
        #background(200)
        image(fightbackground, 0, 0, width, height)
        
        renderAttackButtons() #look at the extra fxns section

        cEnemy = enemyList[currentEnemy]
        cType = cEnemy.type
        cStatus = cEnemy.status
        cHealth = cEnemy.health
        cElement = cEnemy.element
    
        #show enemy stuff
        if debugMode:
            fill(255)
            noStroke()
            rect(45, 25, 250, 250) #highlight box
            fill(0)
            textSize(24)
            text("Enemy health: " + str(cHealth) + " ", 50, 50)
            text("type: " + cType + "\n enemyID: " + str(currentEnemy) + "\n enemy element: " + cElement, 50, 120)
            text("status: " + cStatus, 50, 240)
            textSize(32)
            stroke(0)
        cEnemy.display()
        cEnemy.displayStatus()
        cEnemy.healthBarInFight()
        
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
        if endWaiting or cHealth<=0: 
            if cEnemy.isBoss == True: 
                print("yippee you killed the " + cType + " congrations you (probably) got loot!11!!11!")
                hpotcount+=5
                daggercount+=5
                coins+=90
                #if hasArmor == False:
                 #   print("You found an iron chestplate! This will provide 25% damage reduction from enemy attacks!") 
                  #  hasArmor = True
                if cType == "Sand Boss": 
                    hasRock = True
                    sandBossBeaten = True
                    del blocks[0]
                if cType == "Skeleton Boss":
                    skeletonBossBeaten = True
                    if not sandBossBeaten:
                        del blocks[1]
                    else:
                        del blocks[0]
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            endWaiting = False
            #coins += (0.5*cEnemy.maxHealth)    <-- idea is the amount of gold u get scales with enemy hp
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
            enemyHitDamage = cEnemy.strength
            if hasArmor == True: 
                enemyHitDamage *= 0.75
            if cStatus == "frozen" or (cElement == "fire" and cStatus == "wet"): 
                enemyHitDamage *= 0.6
            gamer.health -= enemyHitDamage
            println("The gamer was hurt for " + str(enemyHitDamage) + " damage!")
            turn = 3
            animationWaitTimer = turn2wait
            
            ##ENEMY HIT LOGIC
        if animationWaitTimer == 20 and turn == 2: 
            if attackType[0] == "none": 
                cEnemy.hit(50, attackType) 
            elif attackType[0] == "heal": 
                rect(0,0,0,0)
            elif attackType[0] == "lightning" or attackType[0] == "rock": 
                cEnemy.hit(30, attackType)
            else: 
                cEnemy.hit(20, attackType)
        
## 3rd turn
        ##Displays player hurting
        if turn == 3 and animationWaitTimer != 0:
            #player getting hurt
            fractionOfAnimLeft = float(animationWaitTimer)/turn2wait
            gamer.showInFight(fractionOfAnimLeft)
        else:
            gamer.showInFight(0)
            
        ##Resolve statuses
        if turn == 3 and animationWaitTimer == 0:
            enemyFighting = cEnemy
            
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
            if cHealth<=0:
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
        #cEnemy.status = cStatus
        #cEnemy = cEnemy
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
        #i moved the armor text into debugMode at the bottom of mapMode
        
    #chest
        #so currently chest hitbox is super jank sorry
        if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, 450-gamer.mapPosX+(width/2), 200-gamer.mapPosY+(height/2), 100, 100) and chestopened == False: 
            daggercount+=10
            hpotcount+=10
            chestopened = True
        if chestopened == False:      #<-- this would mean deleting the chest but that might look weird
            image(chestimg, 380-gamer.mapPosX+(width/2), 160-gamer.mapPosY+(height/2)+50, 75, 75 )   
        
        gamer.showOnMap()
    
        for s in signs:
            s.showSign(gamer.mapPosX, gamer.mapPosY)
        
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
            e.mapDisplay(gamer.mapPosX, gamer.mapPosY, debugMode)
            if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, e.mapPosX-32, e.mapPosY-32, 132, 132) and gamer.health>0: 
                currentEnemy = enemyList.index(e)
                print(" ==-== " + enemyList[currentEnemy].element + " " + enemyList[currentEnemy].type + " ==-== ")
                gameState = "fight"
        
        if debugMode:
            text("iron armor", 5, height-100)
            for o in blocks:
                o.display(gamer.mapPosX, gamer.mapPosY)
        
        if not sandBossBeaten:
            image(sandBlock, 247-gamer.mapPosX+(width/2), 1220-gamer.mapPosY+(height/2))
        if not skeletonBossBeaten:
            image(bushBlock, 1900-gamer.mapPosX+(width/2), 1680-gamer.mapPosY+(height/2))
        
#-------------------------------------------------------STORE MODE--------------------------------------------------------------------#
    else: #gameState is in store mode                   also i apologize for the 1290380129 lines of code im bad ok
        #i have no clue what to do here yet, prolly something similar to fight mode though where if u have coins and
        #if u click in the boxes then u buy stuff and also render some store guy toob
        
        #background(127)
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
        text("Welcome to my shop. \nFeel free to  buy \nanything you need!\nunless we dont have it lol", 60, 75)
        
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
        
        #dagger
        fill(127)
        rect(250,400,100,25)
        
        #armor
        rect(400,400,100,25)
        fill(0)
        text("1 dagger", 250, 390)
        if hasArmor == False: 
            text("Iron armor", 400, 390)
        elif hasArmor == True: 
            text("no more armor sorry", 400, 390)
        
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
    
    if gameState == "fight" and gamer.health>=1 and turn == 1:
        if pointInsideCircle(mouseX, mouseY, 430, 400, 25) and daggercount>0: 
            attackImage = loadImage("epicSword.png")
            attackType = ["none", "none"]
            daggercount-=1
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 430, 330, 25): #fire
            attackImage = loadImage("FireBall.png")
            attackType = ["fire", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 490, 365, 25): #water
            attackImage = loadImage("WaterBolt.png")
            attackType = ["water", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 490, 435, 25): #grass
            attackImage = loadImage("LeafAttack.png")
            attackType = ["grass", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 430, 470, 25): #lightning
            attackImage = loadImage("lightningBolt.png")
            attackType = ["lightning", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 370, 435, 25): #ice
            attackImage = loadImage("icicleAttack.png")
            attackType = ["ice", "none"]
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 370, 365, 25) and hasRock: #rock
            attackImage = loadImage("rock1.png")
            attackType = ["rock", "none"]
            turn = 2
            animationWaitTimer = turn1wait
    
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
            
def keyPressed():
    if key == 'w' or keyCode == UP:
        keyPresses[0] = True
    if key == 'a' or keyCode == LEFT:
        keyPresses[1] = True
    if key == 's' or keyCode == DOWN:
        keyPresses[2] = True
    if key == 'd' or keyCode == RIGHT:
        keyPresses[3] = True
    
def keyReleased():
    global gamer, hpotcount, amogus, daggercount, turn, attackImage, gameState, attackType, animationWaitTimer, turn1wait
    if key == 'w' or keyCode == UP:
        keyPresses[0] = False
    if key == 'a' or keyCode == LEFT:
        keyPresses[1] = False
    if key == 's' or keyCode == DOWN:
        keyPresses[2] = False
    if key == 'd' or keyCode == RIGHT:
        keyPresses[3] = False
        
    if key == 'h' and hpotcount>0 and turn == 1 and gameState == "fight": 
        print("You used a health potion! You healed 30 hp!")
        gamer.health += 60
        hpotcount -= 1
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
    return (a>x) and (a<x+w) and (b>y) and (b<y+h)

def pointInsideCircle(a, b, x, y, r):
    #same as above but circle now; finds the distance between (a,b) and (x,y)
    return pow(pow(a-x, 2) + pow(b-y, 2), 0.5) < r
    
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

def renderAttackButtons():
    textSize(18)
    imageMode(CENTER)
    strokeWeight(2.5)
    fill(128)
    ellipse(430, 330, 50, 50)
    ellipse(490, 365, 50, 50)
    ellipse(490, 435, 50, 50)
    ellipse(430, 470, 50, 50)
    ellipse(370, 435, 50, 50)
    ellipse(370, 365, 50, 50)
    image(icons[0], 430, 330, 50, 50) #fire
    image(icons[1], 490, 365, 50, 50) #water
    image(icons[2], 490, 435, 50, 50) #grass
    image(icons[3], 430, 470, 50, 50) #lightning
    image(icons[4], 370, 435, 50, 50) #ice
    if hasRock:
        image(icons[5], 370, 365, 50, 50) #rock
    imageMode(CORNER)     

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
    return "No status inflicted"
