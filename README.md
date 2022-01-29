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


README

Chutes and Ladders
Afreen Shah and Jaskaran Mohem
Project TA: Dominic

Navigate to the file in the terminal 
In the command line type: python3 index.py
(For my macbook it was: 
cd Documents
cd AfreenShah_JaskaranMohem_FinalProject
python3 index.py
)

To get to the test cases, navigate to the file in the terminal
In the command line type: python3 test_board.py

Features
We will be creating a 10x10 board with empty positions, positions with snakes (red lines), and positions with ladders (green lines).
We will implement a button called roll die and when the space bar is pressed a function will generate a random number and then display a dice image of the number rolled. The player will click the roll die button and move an x number of positions (based on the random number) along the empty positions of the board. If, however, the player lands on a position with a ladder, the player will move up to the position where the ladder ends. If the player lands in a position where there is a chute, the player will move down to where the chute ends. 
The game will end when the player reaches the last position (position 100) on the board. There will be a score function on the side that will count the number of rolls it took the player to reach the end of the board. The end screen must properly display with no lingering objects or ‘dirty blits’ on the screen. 

Justification for Complexity
A brief justification for why the project should receive full credit for complexity:
How did your features contribute to complexity?
Did you use trickier concepts that we taught in class and what were they? How did you implement them?
Did you make use of some more advanced features of Snap?
How did you break up complicated tasks? 
Other points that show your project has complexity
	The features used in this project include making custom functions to be implemented throughout the game. When creating the board, we implemented functions from pygame in order to make the background and position the board, instructional button, and the chutes and ladders. 
For the movement of players,  we made custom methods in our Player class like setting the players position, creating a loop that alternates the players actions, and a custom method to move the players as well. We employed helper functions within methods as well, particularly in the case of the move_player method which demonstrates our ability to see patterns and avoid redundancy in the code. 
Throughout the game, we tactfully employed lists, local variables, and global variables depending on whether we needed to mutate and return a changed value. This demonstrates our understanding of scope.

Lists & Script Variables: Description of the lists and script variables in project
The nontrivial list employed in our code is in the helper function random_roll() in our method move_player in our Player class. We created a helper function (dice_images) that appends loaded images of our dice into a list, images_loaded that is returned. This list stores and indexes all the images which we index to get the images associated with the number of the randomly generated roll. 

In the button class’s draw method, the script variable exit_screen is assigned as False. This script variable determines if the exit_screen is true or false and therefore should be drawn
dict in make_chutes_and_ladders is assigned which is a script variable. It is first an empty dictionary that keys and values will be added into. This dict will then be returned and can be stored, as demonstrated in line 120 and 121 where the chutes and ladders are created
Script variables random_pos1 and random_pos2 store the randomly assigned values from the coordinates copy dictionary 
Without_pos1row store the keys and values of the spots that are within the same row as the first randomly assigned position (random_pos1)
 images_loaded in board.py in helper function random_roll() is created and assigned to an empty list. The list will be appended with the loaded images.
dice_images_list is assigned the value of the dice_images function called with a list of dice images
dice_number is assigned the random value between 1 and 6
Dice_image is assigned the image corresponding to dice_number 
game_over in the helper function check_game_over is assigned a boolean to determine if the game is over
In move_player method,roll is assigned to the output of random_roll so it stores the tuple of the image of the dice and the integer of the roll


