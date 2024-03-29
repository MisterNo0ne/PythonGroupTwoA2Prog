# Spell Based Adventure Game

###

### Description
This game will be a spell based adventure that involves exploring a world, discovering new spells, learning how the elements interact, and fighting enemies. Search the island looking for secrets, knowledge, and special weapons so that you can defeat the final boss!

### How to use
On the map screen, use WASD or the arrow keys to move around. (If you run out of enemies to fight in the plains, press 'i' to respawn them.)
In a battle, press 'H' to heal. Otherwise just left click on the element of choice for your attack when it is your turn.
In the shop, click on the buttons shown to buy health pots, daggers, and armor. To exit, click the button in the bottom right.

## Features
Added a debugMode that can be toggled to display important statistics and information for debugging.

### Map game state
Added new 'obstacle' class that players aren't allowed to walk through. They act as walls to corall the player. It has a toggleable mode to turn on or off showing the hitboxes.
Added a new variable for a list of variables that can looped over to detect collisions to move the player in case of in-game collision. 

Added mapPosX and mapPosY variables to both the player and enemies so that both can render on the map. Additionally, the player and enemy have a showOnMap() and mapDisplay() function respectively to render each.

Added key detection variables, so that if for example the 'w' key is pressed, a boolean will turn to true. Furthermore, this has been hooked up to player.py to allow player movement

Added collision detection between player and enemies. When they collide, the gameState will change to fight mode, and players will enter a fight with enemies. Currently, though, there is no battle functionality.

Added a secret island.

Added highly detailed map background with many zones including high quality trees, cactuses, and a dangerous castle zone. We also have many easter eggs such as an impostor in the sea.

Added a button that can be pressed to respawn enemies.

### Fight game state
Added weakness and resistance lists to the enemy class for damage calculation. This adds an element of strategy, so players have to think about the best way to attack a particular type of enemy.

Added a damage calculator to enemy class. Now, the enemy class has a function called hit() that will take in variables for damage and element types to calculate the real damage. For example, if a player tries to attack a fire enemy with a grass attack, the damage will be halved. If they try a water type instead, the damage will be doubled. The calculations are based on the enemy's weakness and resistance stats.

Added new fight background.

Added PNGs for the enemies and character.

Added health bar to both enemies and character to show current health percentage. The bar decreases based on how much damage you dealt or taken.

Added animations to the current possible attacks.

Added turns to have animations inbetween the player's turn, the enemy's turn, and status resolution.

6 possible elements, each with unique interactions and possible combos, such as lightning doing more damage if the enemy was made wet by a previous water attack.

Added inventory system.

Made enemies drop certain loot based on their health.

Added a jumpscare.

### Store game state
Added color-changing buttons for things to buy .

Added background to the shop.

Added a display that shows the prices of each item.

## Development

### Roles
Micah: player.py and obstacle.py and all of their class functions, as well as keyPress system and gameState transition. Also made the map, enemies sprinkled around the map, the jumpscare, all the obstacles for collisions, animation system, respawning enemies, and changing enemy fight backgrounds based on the terrain.

Zack: enemy images, attack sprites,  enemy.py, mapDisplay() and the damage calculator, as well as the element and status effect system, turn system, boss gimmicks, the store, inventory display, health bar display, health pot functionality, armor and coin functionality. 

Eddie: item.py, weapon.py, class extension, npc.py, and a basic dialogue file that npc can access
Class extension works by having 'child' classes inherit data from 'parent' classes, so the weapon class can have values of the item class. There isnt a thing on it on the main processing documentation page either so its tough

Maksim: Majority of the images and sprites including attack icons, some enemy images, the player, attacks, the shop, the shopkeeper, npcs, bosses, and basic functionality of data folder
Basically the animations in the battles work by having 2 variables for x and y change and have an image render at those coordinates; the image changes based on the attack

### [Source Code](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing)

### [Assets](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing/data)

### Running Program Mockups
![New Map (Sea)](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/New%20Map%20(Sea).png?raw=true)

![Castle](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/assets/111779779/f1f419e4-30fa-4ce3-bd23-15614cc7b793)

![Fight Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Fight%20Example.png?raw=true)

![Animation Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Animation%20Example.png?raw=true)

## To-do List

### Done
- obstacles
- signs
- healing
- rock, ice, lightning
- removable obstales for the forest and desert bosses
- item class
- item list
- add arrow key functionality (micah)
- isplay costs in shop
- make the shop buying boxes change colors if the player can afford it 
- obstacle speedrun
- get moving enemies to work for epic jumpscare
- get armor sprite visible in fight and map mode
- brainstorm the gimmicks we'll do on Sunday
- Different backgrounds for different areas
- get bosses with gimmicks working (like multiple phases? or changing elements stuff like that. maybe immunity to statuses for one)
  - to be specific we need castle boss, forest boss, and desert boss. 
- make player spawn in the middle of the map and move all the enemies to actual places
