# Spell Based Adventure Game

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
![Spell Based Adventure 1](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sbaMockup1.PNG?raw=true)

![Spell Based Adventure 2](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sbaMockup2.PNG?raw=true)

![Spell Based Adventure 3](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sbaMockup3.PNG?raw=true)

### Current Program
![New Map (Sea)](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/New%20Map%20(Sea).png?raw=true)

![Castle](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/assets/111779779/f1f419e4-30fa-4ce3-bd23-15614cc7b793)

![Fight Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Fight%20Example.png?raw=true)

![Animation Example](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/Animation%20Example.png?raw=true)


### Class Diagram
![Spell Based Adventure Class Diagram](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/classDiagram.PNG?raw=true)
