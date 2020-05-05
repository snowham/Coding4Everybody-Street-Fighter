[![Run on Repl.it](https://repl.it/badge/github/snowham/Coding4Everybody-Street-Fighter)](https://repl.it/github/snowham/Coding4Everybody-Street-Fighter)

# Coding4Everybody-Street-Fighter

### 3/3
#### SATVIK 
- I added a punch feature. Reason why the arrows and spaces are in two seperate handlers is because the first handler can't detect prolonged pushes (effiecently, it can but repl.it crashes), and the second one cannot detect key releases. Added new images for punch, they are replacable (obviousely)

### 3/4
#### SOHAM/SATVIK 
- We made it so that the player/sprite cannot move pas the edge of the screen. Don't know if both entityPlayer and entitySprite are necessary... We should make it so that the player looks like he's running, because right now he's just sliding across the screen. We also should make it so that you can punch at the same time the player is running. I think we should change the images this set of images isn't enough. Arush and Niels if you want to learn the pygame basics this is a great start: https://www.youtube.com/watch?v=i6xMBig-pP4

### 3/11
#### SOHAM 
- I created a jump function. Entities can now jump. Yay. I've been having a problem with repl.it, it's really laggy.

### 4/25
#### NIELS 
- I rewrote most of the code to make future programming easier. There is a class called EntityFighter now which inherits from EntitySprite. This class should be called or edited whenever the player needs an action to be performed instead of writing the code into the main class. I also added hitboxes (enable SHOW_HITBOXES in the reference class to debug) Now if one fighter decides to throw a punch, you should call tryAttack from every other fighter and pass in the fighters active hitbox if it is of type hitbox.

### 4/25
#### ARUSH 
- Switched the keys that control the players so that Fighter 1 has w,a,d to move and x to punch. Fighter 2 has UP,RIGHT,LEFT to move and , to punch.
#### SOHAM 
- Switched the keys back because we're playing online, not on the same computer, and if only one person is using their computer, then it's easiest when the moving keys and the punch key are far apart.

<<<<<<< HEAD
<<<<<<< HEAD
[![Run on Repl.it](https://repl.it/badge/github/snowham/Coding4Everybody-Street-Fighter)](https://repl.it/github/snowham/Coding4Everybody-Street-Fighter)

# Coding4Everybody-Street-Fighter

### 3/3
#### SATVIK 
- I added a punch feature. Reason why the arrows and spaces are in two seperate handlers is because the first handler can't detect prolonged pushes (effiecently, it can but repl.it crashes), and the second one cannot detect key releases. Added new images for punch, they are replacable (obviousely)

### 3/4
#### SOHAM/SATVIK 
- We made it so that the player/sprite cannot move pas the edge of the screen. Don't know if both entityPlayer and entitySprite are necessary... We should make it so that the player looks like he's running, because right now he's just sliding across the screen. We also should make it so that you can punch at the same time the player is running. I think we should change the images this set of images isn't enough. Arush and Niels if you want to learn the pygame basics this is a great start: https://www.youtube.com/watch?v=i6xMBig-pP4

### 3/11
#### SOHAM 
- I created a jump function. Entities can now jump. Yay. I've been having a problem with repl.it, it's really laggy.

### 4/25
#### NIELS 
- I rewrote most of the code to make future programming easier. There is a class called EntityFighter now which inherits from EntitySprite. This class should be called or edited whenever the player needs an action to be performed instead of writing the code into the main class. I also added hitboxes (enable SHOW_HITBOXES in the reference class to debug) Now if one fighter decides to throw a punch, you should call tryAttack from every other fighter and pass in the fighters active hitbox if it is of type hitbox.

### 4/25
#### ARUSH 
- Switched the keys that control the players so that Fighter 1 has w,a,d to move and x to punch. Fighter 2 has UP,RIGHT,LEFT to move and , to punch. 
- Added attribute for entityFighter so we can add its own positions to easily change color and add extra moves
#### SOHAM 
- Switched the keys back because we're playing online, not on the same computer, and if only one person is using their computer, then it's easiest when the moving keys and the punch key are far apart.

### 4/26
#### SOHAM 
- I added a new character! He looks the same as our blue guy, but he's red. 
- I also created a start screen, and that made me create a start.py module and game_loop module. This cleaned up a BUNCH of main.py, so that all main.py does is acts as the admin module and actually executes the program.
#### Arush
- I changed all the variables in reference and entitySprite to be proportional with HEIGHT and WIDTH
=======
### 4/26
#### SOHAM
- I added a new character! He looks the same as our blue guy, but he's red. 
>>>>>>> origin/master
=======
### 4/26
#### SOHAM
- I added a new character! He looks the same as our blue guy, but he's red. 
>>>>>>> origin/master
