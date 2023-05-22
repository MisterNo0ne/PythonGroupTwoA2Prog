from enemy import Enemy
from item import Item
from item import Weapon
from npc import Npc
from obstacle import Obstacle
from player import Player
from sign import Sign

#why can you freeze a water type hello??

def setup():
    size(600, 600)
    frameRate(24)
    print("hello gamer welcom to epic spell adventure game smiley face =)")

    global gameState, ghoul, skeleton, zombie, spider, debugMode, gamer, keyPresses, bkgrnd, enemyList, currentEnemy, skltnimg, ghlimg, spdrimg, zomimg, attacktype, turn, blocks, fightbackgrounds, animationWaitTimer, endWaiting, attackImage, turn1wait, turn2wait, turn3wait, wizard, cactus, cactusimg, chestimg, chestopened, amogus, sandBoss, sandimg, skltnbossimg, castleimg, skltnBoss, castleBoss, blockFile, merchant, shopimg, hasRock, shopBackground, signimg, signs, bushBlock, sandBlock, skeletonBossBeaten, sandBossBeaten, icons, itemsOwned, weaponsOwned, weaponImgs, switchingWeapon, currentWeapon
    
    #load files
    fightbackgrounds = []
    fightbackgrounds.append(loadImage("plainsfightbackground.png"))
    fightbackgrounds.append(loadImage("epicfightbackground.jpeg"))
    fightbackgrounds.append(loadImage("desertfightbackground.png"))
    fightbackgrounds.append(loadImage("volcanofightbackground.png"))
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
    weaponImgs = []
    weaponImgs.append(loadImage("weapons/sword.png"))
    weaponImgs.append(loadImage("weapons/bow.png"))
    weaponImgs.append(loadImage("weapons/dagger.png"))
    weaponImgs.append(loadImage("weapons/spear.png"))
    weaponImgs.append(loadImage("weapons/mace.png"))
    
    #enemy declarators or smth
    cactus = Enemy(200, "cactus", "grass", 150, 300, cactusimg, "none", 30, False, 0)
    ghoul = Enemy(50, "ghoul", "fire", 500, 500, ghlimg, "none", 20, False, 0)
    skeleton = Enemy(100, "skeleton", "grass", 200, 400, skltnimg, "none", 20, False, 0)
    spider = Enemy(42, "spider", "fire", 200, 200, spdrimg, "none", 20, False, 0)
    zombie = Enemy(153, "zombie", "water", 300, 100, zomimg, "none", 20, False, 0)
    sandBoss = Enemy(300, "Sand Boss", "fire", 300, 1400, sandimg, "none", 40, True, 2)
    skltnBoss = Enemy(400, "Skeleton Boss", "grass", 2500, 1600, skltnbossimg, "none", 40, True, 1)
    castleBoss = Enemy(500, "Final Boss", "fire", 1600, 200, castleimg, "none", 50, True, 3)
    enemyList = [cactus, ghoul, skeleton, spider, zombie, sandBoss, skltnBoss, castleBoss] 
    
    gamer = Player(1400, 1300, 100, wizard) 
    
    itemsOwned = []
    itemsOwned.append(Item("Coins", 10.0))
    itemsOwned.append(Item("Health Pots", 0))
    itemsOwned.append(Item("Daggers", 0))
    itemsOwned.append(Item("Armor", "leather"))
    
    #REMEMBER: order is fire, water, grass, lightning, ice, rock
    weaponsOwned = []
    weaponsOwned.append(Weapon("Sword", 25.0, [1, 1, 1.5, 0.5, 1, 1], [0.8, 1, 1, 0.8, 1, 1.5], weaponImgs[0]))
    weaponsOwned.append(Weapon("Bow", 20.0, [1, 0.8, 1, 0.8, 1.5, 1], [0.8, 1, 1, 1.5, 1.2, 0.5], weaponImgs[1]))
    
    blocks = []
    makeBlocks()
    
    signs = []
    signs.append(Sign(725, 600, "This is a sign", signimg, 32, 1))
    signs.append(Sign(725, 700, "This is a sign\nwith a line break :O", signimg, 16, 2))
    signs.append(Sign(725, 800, "Two\nline\nbreaks", signimg, 12, 3))
    signs.append(Sign(725, 900, "Small text with one line wowie", signimg, 10, 1))
    signs.append(Sign(1400, 1300, "Welcome to the land of spellaria!\nYou have been chosen to defeat the\n3 great evils of this land!", signimg, 12, 3))
    signs.append(Sign(1300, 1300, "To the west lies your first challenge, the\ngreat sand behemoth. Defeat it andyou'll\ngain access to a powerful new spell.", signimg, 11, 3))
    signs.append(Sign(1500, 1300, "To the east lies the formidable skeleton\nlord in the dark forest. Defeat it to\nobtain yet another powerful spell", signimg, 12, 3))
    signs.append(Sign(1400, 1200, "To the north lies your final foe, the\nevil presence residing in the Dark Castle.\n Defeat it and you'll have become the\nmost powerful wizard in the land.", signimg, 10, 4))
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
    currentWeapon = 0
    chestopened = False
    hasRock = False
    amogus  = True #amogus is like hax mode, where during this u can hack in more health pots and daggers and funi stuff
    debugMode = True 
    skeletonBossBeaten = False
    sandBossBeaten = False
    switchingWeapon = False
    keyPresses = [False, False, False, False]
    turn = 1
    attackImage = loadImage("WaterBolt.png")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def draw():
    global gameState, currentEnemy, enemyList, ghoul, skeleton, turn, animationWaitTimer, gamer, endWaiting, attackType, chestimg, chestopened, merchant, shoping, hasRock, shopBackground, signs, sandBossBeaten, skeletonBossBeaten, itemsOwned, weaponsOwned
    #??????????????????????????????????????????????????????
    #if you wanna edit values of global variables you have to put them here
    
#-------------------------------------------------------------------------------FIGHT MODE-------------------------------------------------------------------
    
    if gameState == "fight":
        cEnemy = enemyList[currentEnemy]
        cType = cEnemy.type
        cStatus = cEnemy.status
        cHealth = cEnemy.health
        cElement = cEnemy.element
        
        # Display logic
        #background(200)
        image(fightbackgrounds[cEnemy.area], 0, 0, width, height)
        
        renderAttackButtons() #look at the extra fxns section
    
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
        text("You have " + str(itemsOwned[2].value) + " daggers!", width-200, height-30)
        text("You have " + str(itemsOwned[1].value) + " health potions!", width-520, height-30)
        text("Press H to heal!", width-520, height-60)
        textSize(32)
        
        text(str(animationWaitTimer), width-100, 100)
        text(str(turn), width-100, 140)
        
        
            ##KILLED ENEMY LOGIC
        if endWaiting or cHealth<=0: 
            if cEnemy.isBoss == True: 
                print("yippee you killed the " + cType + " congrations you found 100 coins, 5 potions, and 5 daggers!")
                itemsOwned[1].value+=5
                itemsOwned[2].value+=5
                itemsOwned[0].value+=90
                #if hasArmor == False:
                 #   print("You found an iron chestplate! This will provide 25% damage reduction from enemy attacks!") 
                  #  hasIronArmor = True
                if cType == "Sand Boss": 
                    hasRock = True
                    sandBossBeaten = True
                    del blocks[0]
                if cType == "Skeleton Boss":
                    #poison added here
                    skeletonBossBeaten = True
                    if not sandBossBeaten:
                        del blocks[1]
                    else:
                        del blocks[0]
            del enemyList[currentEnemy]
            gameState = "map"
            currentEnemy = 12345
            endWaiting = False
            itemsOwned[0].value += (0.25*cEnemy.maxHealth)   # <-- idea is the amount of gold u get scales with enemy hp
            #itemsOwned[0].value+=10
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
        
        ##ENEMY HIT LOGIC
        if animationWaitTimer == 20 and turn == 2: 
            cw = weaponsOwned[currentWeapon]
            if attackType[0] == "lightning" or attackType[0] == "rock": 
                damage = 30
            if attackType[0] == "heal":
                damage = 0
            if attackType[0] == "grass" or attackType[0] == "fire" or attackType[0] == "water" or attackType[0] == "ice": #dont attack if the player healed thats dumb
                damage = 20
            cEnemy.hit(damage, attackType, cw)
        
        ##PLAYER HIT LOGIC
        if turn == 2 and animationWaitTimer == 0:
            enemyHitDamage = cEnemy.strength
            
            if itemsOwned[3].value == "iron": 
                enemyHitDamage *= 0.75
            if itemsOwned[3].value == "diamond": 
                enemyHitDamage *= 0.5
            if cStatus == "frozen" or (cElement == "fire" and cStatus == "wet") or cStatus == "zapped": 
                enemyHitDamage *= 0.6
            if cStatus == "tangled" and cElement == "grass": 
                enemyHitDamage*=1.25
                print("The grass " + cType + " grows stronger from the vegetation! (1.25x)")
            if cStatus == "overgrown" and cElement == "grass": 
                enemyHitDamage*=1.5
                print("The grass " + cType + " grows super strong from the overgrown vines! (1.5x)")
            
            gamer.health -= enemyHitDamage
            println("The gamer was hurt for " + str(enemyHitDamage) + " damage!")
            turn = 3
            animationWaitTimer = turn2wait
        
## 3rd turn
        ##Displays player hurting
        if turn == 3 and animationWaitTimer != 0:
            #player getting hurt
            fractionOfAnimLeft = float(animationWaitTimer)/turn2wait
            gamer.showInFight(fractionOfAnimLeft)
        else:
            gamer.showInFight(0)
          
        ##kills the player to death    
        if gamer.health<=0 and turn == 3 and animationWaitTimer == 0:
            turn = 5
            animationWaitTimer = 50
            print("oh no!1!11!1!11 uy deied!!11! you are loser L game over")
            
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
        
## 5th turn
        # Gamer death logic
        if turn == 5 and animationWaitTimer !=0: 
            fill(0)
            rect(0,0,width,height)
            fill(255)
            text("You passed out!",(width/2)-50, (height/2))
        if turn == 5 and animationWaitTimer == 0: 
            gameState = "map"
            gamer.mapPosX = 1400
            gamer.mapPosY = 1300
            gamer.health = (gamer.maxHealth/2)
            print("You managed to escape, but lost some coins")
            itemsOwned[0].value-=15
            if itemsOwned[0].value<=0: 
                itemsOwned[0].value = 0
            turn = 1
    
#----------------------------------------------------------------------MAP MODE------------------------------------------------------------------------------

    if gameState == "map":
        gamer.moveOnMap(keyPresses, blocks)
        
        background(12, 89, 183)
        image(bkgrnd,(width/2)-gamer.mapPosX,(height/2)-gamer.mapPosY)
        
        stroke(0)
        strokeWeight(4)
        #starting platform thingy
        fill(127)
        rect(1300-gamer.mapPosX+(width/2),1200-gamer.mapPosY+(height/2),200,200)
        
        #displaying health bar so the player actually knows what their hp is before fighting: 
        displayPlayerHealth()
    #chest
        #so currently chest hitbox is super jank sorry
        if pointInsideRectangle(gamer.mapPosX, gamer.mapPosY, 450-gamer.mapPosX+(width/2), 200-gamer.mapPosY+(height/2), 150, 100) and chestopened == False: 
            itemsOwned[2].value+=10
            itemsOwned[1].value+=10
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
            for o in blocks:
                o.display(gamer.mapPosX, gamer.mapPosY)
        
        if not sandBossBeaten:
            image(sandBlock, 247-gamer.mapPosX+(width/2), 1220-gamer.mapPosY+(height/2))
        if not skeletonBossBeaten:
            image(bushBlock, 1900-gamer.mapPosX+(width/2), 1680-gamer.mapPosY+(height/2))
        
        inventoryBox()
#-------------------------------------------------------STORE MODE--------------------------------------------------------------------#
    if gameState == "store":
        #i have no clue what to do here yet, prolly something similar to fight mode though where if u have coins and
        #if u click in the boxes then u buy stuff and also render some store guy toob
        
        #background(127)
        image(shopBackground,0,0,600,600)
        image(shopimg, 375, 100, 300, 300)
        image(merchant, 300, 200, 100, 100)
        
        inventoryBox()
        
        fill(255)
        stroke(0)
        strokeWeight(4)
        rect(50,50,220,110)
        fill(0)
        textSize(22)
        text("Welcome to my shop. \nFeel free to  buy \nanything you need!\nunless we dont have it lol", 60, 75)
        
        #hpot
        fill(color(127) if itemsOwned[0].value<10 else color(100, 255, 100))
        rect(100,400,100,25)
        
        #dagger
        fill(color(127) if itemsOwned[0].value<5 else color(100, 255, 100))
        rect(250,400,100,25)
        
        #armor
        fill(color(127) if itemsOwned[0].value<100 else color(100, 255, 100))
        rect(400,400,100,25)
        
        
        #text for items
        fill(0)
        text("Health Potion", 100, 390)
        text("10 coins", 105, 420)
        
        text("Dagger", 250, 390)
        text("5 coins", 255, 420)
        
        if itemsOwned[3].value == "leather": 
            text("Iron armor", 400, 390)
            text("100 coins", 405, 420)
        elif itemsOwned[3].value == "iron":
            if skeletonBossBeaten: 
                text("Diamond Armor", 400, 390)
                text("300 coins", 405, 420)
            else: 
                text("No more armor", 400, 390)
        #text("100 coins", 405, 420)
        
        #Exit button
        fill(200,50,50)
        rect(440,500,200,25)
        fill(0)
        text("Exit to map...", 450, 490)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def mousePressed():
    global turn, attackImage, animationWaitTimer, attackType, hasRock, gameState, gamer, itemsOwned, currentWeapon, switchingWeapon
    
    if gameState == "fight" and gamer.health>=1 and turn == 1:
        if pointInsideCircle(mouseX, mouseY, 430, 400, 25): 
            switchingWeapon = not switchingWeapon
        if pointInsideCircle(mouseX, mouseY, 430, 330, 25): #fire
            attackImage = loadImage("FireBall.png")
            attackType = "fire"
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 490, 365, 25): #water
            attackImage = loadImage("WaterBolt.png")
            attackType = "water"
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 490, 435, 25): #grass
            attackImage = loadImage("LeafAttack.png")
            attackType = "grass"
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 430, 470, 25): #lightning
            attackImage = loadImage("lightningBolt.png")
            attackType = "lightning"
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 370, 435, 25): #ice
            attackImage = loadImage("icicleAttack.png")
            attackType = "ice"
            turn = 2
            animationWaitTimer = turn1wait
        if pointInsideCircle(mouseX, mouseY, 370, 365, 25) and hasRock: #rock
            attackImage = loadImage("rock1.png")
            attackType = "rock"
            turn = 2
            animationWaitTimer = turn1wait
    
    if gameState == "store": 
        if pointInsideRectangle(mouseX, mouseY, 100,400,100,25) and itemsOwned[0].value>=10:
            itemsOwned[1].value+=1
            itemsOwned[0].value-=10
        if pointInsideRectangle(mouseX, mouseY, 250,400,100,25) and itemsOwned[0].value>=5:
            itemsOwned[2].value+=1
            itemsOwned[0].value-=5
        if pointInsideRectangle(mouseX, mouseY, 400,400,100,25) and itemsOwned[0].value>=100 and itemsOwned[3].value == "leather":
            itemsOwned[3].value = "iron"
            itemsOwned[0].value-=100
            wizard = loadImage("IronWizard.png")
            gamer.playerImage = wizard
        if pointInsideRectangle(mouseX, mouseY, 400,400,100,25) and itemsOwned[0].value>=300 and itemsOwned[3].value == "iron":
            itemsOwned[3].value = "diamond"
            itemsOwned[0].value -= 300
            wizard = loadImage("DiamondWizard.png")
            gamer.playerImage = wizard
        if pointInsideRectangle(mouseX, mouseY, 440,500,200,25):
            gameState = "map"
            gamer.mapPosX=1650
            gamer.mapPosY=1750
            
def keyPressed():
    if key == 'w' or keyCode == UP:
        keyPresses[0] = True
    if key == 'a' or keyCode == LEFT:
        keyPresses[1] = True
        if switchingWeapon:
            currentWeapon-=1
            currentWeapon%=len(weaponsOwned)
    if key == 's' or keyCode == DOWN:
        keyPresses[2] = True
    if key == 'd' or keyCode == RIGHT:
        keyPresses[3] = True
        if switchingWeapon:
            currentWeapon+=1
            currentWeapon%=len(weaponsOwned)
    
def keyReleased():
    global gamer, amogus, turn, attackImage, gameState, attackType, animationWaitTimer, currentWeapon
    if key == 'w' or keyCode == UP:
        keyPresses[0] = False
    if key == 'a' or keyCode == LEFT:
        keyPresses[1] = False
    if key == 's' or keyCode == DOWN:
        keyPresses[2] = False
    if key == 'd' or keyCode == RIGHT:
        keyPresses[3] = False
    if key == 'h' and itemsOwned[1].value>0 and turn == 1 and gameState == "fight": 
        print("You used a health potion! You healed 40 hp!")
        gamer.health += 40
        itemsOwned[1].value -= 1
        attackImage = loadImage("LeafAttack.png")
        attackType = ["heal", "none"]
        turn = 2
        animationWaitTimer = turn1wait
    if key == 'v' and amogus: 
        itemsOwned[1].value+=1
    if key == 'q' and amogus: 
        itemsOwned[2].value+=1
    if key == 'm' and amogus: 
        itemsOwned[0].value+=10
        
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
    fill(200 if switchingWeapon else 170)
    circle(430, 400, 140)
    with pushMatrix():
        translate(430, 400)
        rotate(-PI/4)
        imgsize = 90 if switchingWeapon else 70
        image(weaponsOwned[currentWeapon].img, 0, 0, imgsize, imgsize)
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

def inventoryBox():
    stroke(0)
    strokeWeight(4)
    fill(120,60,60)
    rect(0,height-100, 250, 100)
    fill(0)
    textSize(28)
    text(str(itemsOwned[2].value) + " daggers", 5, height-65)
    text(str(itemsOwned[1].value) + " health potions", 5, height-20)
    text("c " + str(itemsOwned[0].value), 133, height-65)
    strokeWeight(2)
    line(140, height-80, 140, height-65)
    if itemsOwned[3].value == "iron":   #and debugMode
        textSize(16)
        text("iron armor", 5, height-100)
    if itemsOwned[3].value == "diamond": 
        text("Diamond Armor", 5, height-100)

def displayPlayerHealth(): 
    strokeWeight(4)
    stroke(0)
    fill(255)
    rect(280, 550, 300, 40)
    fill(255, 0, 0)
    noStroke()
    rect(282, 552, 297*(float(gamer.health)/gamer.maxHealth), 37)
    fill(0)
    textSize(18)
    textAlign(CENTER)
    text(str(gamer.health) + " / " + str(gamer.maxHealth), 430, 575)
    textSize(24)
    textAlign(LEFT)

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
            return "The fire quickly destroys the vines."
        if enemyType == "water": 
            return "The enemy shrivels and the vines grow enormous!"
        if enemyType == "grass": 
            return "Your grassy vines remain."
    if enemyStatus == "overgrown": 
        if enemyType == "fire": 
            return "The fire quickly destroys the vines."
        if enemyType == "water": 
            return "The vines completely dry the enemy!"
        if enemyType == "grass": 
            return "Your grassy vines remain."
    return "No status inflicted"
