# chutes_and_ladders


Group Members
Afreen Shah 
Jaskaran Mohem 

##Project Vision
We will be implementing the popular game known as chutes and ladders, a popular board game that involves rolling a dice to move the player x number of steps along a 10x10 board until the player reaches the end. However, along the way, there are ladders that can boost a player up along the board and chutes that can move a player down the board.  There will be 2 players for this game.


##How will someone use your project?
We plan on implementing clickable buttons. When the start button is clicked, the game will start. When the roll die button is clicked, the computer will generate a number between 1-6 to move along the positions of the board. 


##What are the three features you want to build?
We will be creating a 10x10 board with empty positions, positions with snakes (red lines), and positions with ladders (green lines).
We will implement a button called roll die and when clicked a function will generate a random number and then display a dice image of the number rolled. The player will click the roll die button and move an x number of positions (based on the random number) along the empty positions of the board. If, however, the player lands on a position with a ladder, the player will move up to the position where the ladder ends. If the player lands in a position where there is a chute, the player will move down to where the chute ends. The AI will do the same without clicking the roll button.
The game will end when the player reaches the last position (position 100) on the board. There will be a score function on the side that will count the number of rolls it took the player to reach the end of the board.

##Language
We will be implementing this in Python.

