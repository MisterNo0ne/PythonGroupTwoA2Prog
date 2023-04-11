# PythonGroupTwoA2Prog
Weve decided to make a spell-based adventure game.

## [Spell Based Adventure Game](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/SpellBattleGame)

### Description
Text-based adventure games are electronic games that uses a text-based user interface. This game concept allows the player to fully direct and make in-game decisions through input. Our game idea will be a spell casting game that involves exploring a world, discovering new spells, and fighting bosses.

## Features

### Map game state
Added new 'obstacle' class that players aren't allowed to walk through. It has a toggleable mode to turn on or off showing the hitboxes, but currently the obstacles have no effect.

Added mapPosX and mapPosY variables to both the player and enemies so that both can render on the map. Additionally, the player and enemy have a showOnMap() and mapDisplay() function respectively to render each.

Added key detection variables, so that if for example the 'w' key is pressed, a boolean will turn to true. Furthermore, this has been hooked up to player.py to allow player movement

Added collision detection between player and enemies. When they collide, the gameState will change to fight mode, and players will enter a fight with enemies. Currently, though, there is no battle functionality.

Added a simple grass background for flavor, and as a quick demonstration of how to use images in proccessing's python mode.

### Fight game state
Added weakness and resistance lists to the enemy class for damage calculation. This adds an element of strategy, so players have to think about the best way to attack a particular type of enemy.

Added a damage calculator to enemy class. Now, the enemy class has a function called hit() that will take in variables for damage and element types to calculate the real damage. For example, if a player tries to attack a fire enemy with a grass attack, the damage will be halved. If they try a water type instead, the damage will be doubled. The calculations are based on the enemy's weakness and resistance stats.

### Roles
Micah: player.py and obstacle.py and all of their class functions, as well as keyPress system and gameState transition

Zach: ghoul image, enemy.py, mapDisplay() and the damage calculator, as well as the basics of the element system

Eddie: item.py, npc.py, and a basic dialogue file that npc can access

Maksim: Skeleton image and basic functionality of data folder

### [Source Code](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing)

### [Assets](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/tree/main/mainThing/data)

### Running Program Mockups
![Spell Based Adventure 1](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sba1.png?raw=true)

![Spell Based Adventure 2](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sba2.png?raw=true)

![Spell Based Adventure 3](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/sba3.png?raw=true)

### Class Diagram
![Spell Based Adventure Class Diagram](https://github.com/MisterNo0ne/PythonGroupTwoA2Prog/blob/main/images/classDiagram.PNG?raw=true)
