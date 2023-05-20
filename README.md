# Spell Based Adventure Game

## To-do List

### Done
- obstacles
- signs
- healing
- rock, ice, lightning

### Friday
- removable obstales for the forest and desert bosses
- item class
- item list
- display costs in shop
- add arrow key functionality (micah)
- make the shop buying boxes change colors if the player can afford it 
- make player spawn in the middle of the map and move all the enemies to actual places
- Beeg thing is to change the attack system
  - Each attack has an element and a weapon (sword, dagger, bow+arrow, maybe other like mace or spear or whatever you can think of)
  - Certain weapons go good/bad with certain elements (arrow good with fire air and poison, bad with rock and water)
  - Something like this below, with the middle circle being clickable; when clicked the player can select what weapon they want to use
    - Add a weapons list separate from the items list to make this easier
![mockup of element wheel](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/mockupOfElementWheel.png?raw=true)

### Saturday
- obstacle speedrun
- get moving enemies to work for epic jumpscare
- get armor sprite visible in fight and map mode
- Make a staling mechanic where you cant use the same attack 100 times for easy win
- probably brainstorm the gimmicks we'll do on Sunday
- Turn 4 for death animations and post-battle things (money earned etc)

### Sunday
- get bosses with gimmicks working (like multiple phases? or changing elements stuff like that. maybe immunity to statuses for one)
  - to be specific we need castle boss, forest boss, and desert boss. 
- Balance literally everything, especially grass being really weak and fire being really op. 
  - Idea: if u do water attack twice or smth, they get doused and take more damage or smth idk. 
- make the readme look nice and pretty

- do everything in 5 days cuz we got extension yay =)

### Idea List
- add poison type that counters fire to balance game
- staling mechanic (same attacks weaken if used multiple times)
- balance rock (make rock only good with certain statuses and bad without that, or maybe rock could get really stale)
- have bosses have different phases/gimmicks. for the final boss, most likely a thing where it's element changes every turn (or every other turn) and all status effects are removed. Maybe have it heal a bit too when transitioning to a new phase. 
- have a shopkeeper and coin system, where killing enemies/bosses awards the player coins that they can use to buy items. basic items would just be health potions and daggers, but maybe have him sell ice/rock spells, armor, idk some other stuff etc. 
- have shopkeeper man sell different foods/buffs, so that u can eat them in the map mode to get buffs to certain attack, like eating ice cream makes ice attacks stronger, or eating spicy food makes fire type attacks stronger. 
- better boss loot and progression to make the game feel like it has order and not just kill anything

### Description
This game will be a spell based adventure that involves exploring a world, discovering new spells, learning how the elements interact, and fighting enemies.

### How to use
On the map screen, use WASD to move around. If you want to start a battle, walk towards the enemy in the bottom right corner (the red triangle). For now, "WASD" is the only usable layout, though arrow keys will be added soon. 

## Features

### Map game state
Added new 'obstacle' class that players aren't allowed to walk through. It has a toggleable mode to turn on or off showing the hitboxes, but currently the obstacles have no effect.
Added a new variable for a list of variables that can looped over to detect collisions to move the player in case of in-game collision. 

Added mapPosX and mapPosY variables to both the player and enemies so that both can render on the map. Additionally, the player and enemy have a showOnMap() and mapDisplay() function respectively to render each.

Added key detection variables, so that if for example the 'w' key is pressed, a boolean will turn to true. Furthermore, this has been hooked up to player.py to allow player movement

Added collision detection between player and enemies. When they collide, the gameState will change to fight mode, and players will enter a fight with enemies. Currently, though, there is no battle functionality.

Added highly detailed map background with many zones including high quality trees, cactuses, and a dangerous castle zone. We also have many easter eggs such as an impostor in the sea.

### Fight game state
Added weakness and resistance lists to the enemy class for damage calculation. This adds an element of strategy, so players have to think about the best way to attack a particular type of enemy.

Added a damage calculator to enemy class. Now, the enemy class has a function called hit() that will take in variables for damage and element types to calculate the real damage. For example, if a player tries to attack a fire enemy with a grass attack, the damage will be halved. If they try a water type instead, the damage will be doubled. The calculations are based on the enemy's weakness and resistance stats.

Added new fight background.
Added PNGs for the enemies and character.
Added health bar to both enemies and character to show current health percentage. The bar decreases based on how much damage you dealt or taken.

Added animations to the current possible attacks.

## Development

### Roles
Micah: player.py and obstacle.py and all of their class functions, as well as keyPress system and gameState transition. Also made the map/island. 

Zack: enemy images, attack sprites,  enemy.py, mapDisplay() and the damage calculator, as well as the element and status effect system. 

Eddie: item.py, npc.py, and a basic dialogue file that npc can access

Maksim: Images and animation, npcs, bosses, and basic functionality of data folder

### [Source Code](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing)

### [Assets](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing/data)

### Running Program Mockups
![New Map (Sea)](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/New%20Map%20(Sea).png?raw=true)

![Castle](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/assets/111779779/f1f419e4-30fa-4ce3-bd23-15614cc7b793)

![Fight Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Fight%20Example.png?raw=true)

![Animation Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Animation%20Example.png?raw=true)


### Class Diagram
![Spell Based Adventure Class Diagram](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/classDiagram.PNG?raw=true)
