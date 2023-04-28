# Castle-Wolfenstein
This game is an action-stealth based on Castle Wolfenstein c64. The purpose of the game is to collect all the keys from the treasures, kill all the enemies and escape. 
Instructions:
WASD: To move the character
Space: To fire
G: To throw a grenade
E: To open treasures
With a PS4 controller:
Left analog stick or arrows to move the character
R1 or L1 to fire and throw a grenade
Triangle to open treasures

The program initially imports the pygame and sys modules, as well as the os and json modules, which are needed for controller usage, specifically the PS4 controller. In our project, we had two PS4 controllers that were used. The program consists of the following 8 classes:
Player: The Player class initializes the necessary sprites and sounds in its __init__ method. It creates square objects (wall_rect) on each wall for collision detection. Other variables in this class are used for initializing various values used in this class and throughout the program. The get_damage, get_hp, and advanced_hp methods are responsible for updating the health bar based on the player's current health. The movement method handles player movements, level transitions, and changes in the player's position on the screen. It also controls the opening of doors when the corresponding key is obtained. The basic movement is determined by keyboard inputs, which modify the _pressed variables accordingly. Collision with the previously created wall squares is also checked. All of these behaviors change when transitioning between levels, as each level has its own walls and doors. The reset method resets the player's sprite position to zero when the player is idle. The update method, like other character update methods, works similarly and is responsible for updating the player's behavior.
Enemy: The Enemy class is similar to the Player class but with some differences. The __init__ method initializes similar attributes and includes detection logic to locate the player in specific positions and change directions accordingly. The movement method differs significantly from the Player class because it operates independently. It handles enemy movement and location changes in each level. Unfortunately, due to constraints during development, an alternative approach was taken instead of using lists and append to handle multiple enemies. The update method functions similarly to the Player class.
SecondEnemy: The SecondEnemy class is almost identical to the Enemy class, with changes in location and the use of level+1 instead of level-1 in arrays for lives and other elements to differentiate it from the Enemy class.
Bullet: The Bullet class controls the movement of bullets fired by the player's weapon. It takes into account the player's position and direction and checks for collisions with enemies or walls. It is called by the main program when the spacebar is pressed and supports multiple bullets on the screen using an array.
EnemyBullet: The EnemyBullet class is similar to the Bullet class but works in the opposite direction. It starts from the enemy and hits the player. It is called by the Enemy class when the enemy detects the player.
Grenade: This class is similar to the Bullet class but includes additional sprites and deals greater damage. The grenade explodes upon collision.
Chest: The Chest class is responsible for creating treasure chests in the game.
