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

Intro (optional)
If your game is not well known or has modified the rules of a pre-existing game, please use this space to describe the rules and/or modified rules. You may wish to include a link to the instructions. 
Our game is the popular game called chutes and ladders. We have implemented red lines to represent the chutes and green lines to represent the ladders. There are 2 players. Player 1 clicks the button to roll the die, and his die is displayed on the screen. He moves the same number of positions along the board as the number on the die he rolls. If he lands on the end of a chute, he moves down to the starting position of the chute, but if he lands on the starting position of the ladder, he moves up to the end of the ladder. After player 1 has moved, player 2 is given the opportunity to roll the die and move along the board. Whichever player reaches the end of the board first wins and his total number of rolls to reach the end of the board are displayed along with a clickable exit button.

Project Approval
Specify if your project was approved and by which TA. If you changed any features or other aspects of your game from your initial project, please also specify this here. 
Project approved by Dominic
We added additional features to our game, explained in further detail in the extra credit section.

Instructions
Explain how users should start your program or game. Include specific terminal commands if necessary. If you utilize an external library or anything that the reader will need to download in order to play your game, please specify this. 

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
A list of the 2 - 3 features that you listed in your project proposal. If this has changed, only discuss the most up-to-date features
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

Lists & Script Variables
Description of the lists and script variables in your project, and how you utilized them (what makes the lists non-trivial, etc.)
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

Function Table
Each row will describe the functionality of one custom block/function, with the relevant information placed in the relevant columns (as defined above). You must include a separate row for EVERY custom block/function you create
** We have multiple py files in order to organize and segregate our codes. I have color coordinated the table in order to indicate where you can find the functions/blocks/ methods

Button.py - yellow
Board.py - blue
Test_board.py - pink

*** We have also created multiple classes so I included the methods inside those classes as well and decided to add a column to denote which class or if the function is in a class

Class
Block / Function/ Method Name
Domain (inputs)
Range (outputs)
Behavior (role in the context of the project)
Button
. Dunder init function
x_pos is the x position on the board that we want the button to be at
y_pos is the y position on the board that we want the button to be at
image is the png file which will be scaled by the parameter scale_by


Outputs:
		Initializes the instance attributes of 
		self.click 
		self.image using image input
		self.rect at position (x_pos,y_pos)
Initializes a Button object 
Button
draw
surface - surface denotes which of the layers that the button will be projected onto
'blit' the button onto the screen
This method draws the button on the surface (which is input as a parameter)
Not a class
Board block
Length of the board

Height of the board

Positions of the spots
Creates a surface that lays inside of the screen display


The board becomes a part of the screen rather than laying on top of it. It is now a characteristic of the board
Not in a class
make_chutes_and_ladders
Choice - string will determine if either a ladder or chute will be made 

Color - the color of the apparatus made on the board

Quantity - how many chutes/ladders will be created on the board



Projects the apparatuses made onto the board
Adds key value pairs of the beginning and end spot of apparatus to the chute/ladder dictionaries. The apparatus will be projected to the background surface, therefore doing the equivalent of ‘merging’ with the screen rather than laying over the interface
Player
Dunder init function
Player_image - png of an image that we want the player to be

Phrase - the name of the player as a string 

Color - the color that we want the text used to correspond to the player
Initializes the instance attributes of

Self.phrase

Self.player_image as the loaded and scaled image 

Self.player_rect - creates a new rect with the size of the image 

self.color
Initializes a player object
Player
set_position
Position of the player
blits the player onto the new position that it has been assigned and returns its new location
This method sets the position of the player 
Player
player_button
Current-player - boolean that is either set to true or false depending if it is that players turn
Alternates the player to either true or false (ie if it is the players turn now then they will be set to false for the following turn and vice versa)
Displays which player should press the spacebar in order to move
Player
move_player
Position - takes in the current position of the player

Current_player - takes in whether or not it is the current player (True or False)
Displays the character in its new position like in the conventional chutes and ladders game
This method enables the player object to move to a new position on the board
Player (helper function in method move_player)
clean_dirty
Position - the position of the object
blits the background surface with the dimensions of the spot on top of the spot to remove the previous 'stamp' of the blit image
This helper function will hide the effects of the dirty blit that occur when the players are moving around the screen. An issue with 
            pygame is that when a sprite is 'blit' onto a surface, it will leave a stamp of its image there. When the characters to move, it will 
            leave a trail of where it previously was by nature of the 'blit' function so we need to manually get rid of the previous blits
            This helper function utilizes the pygame 'surface', 'rect', and 'blit' functions
            background_surface is a surface of the board that was captured. Since the board, chutes, and ladders are on the board, but the players
            interact on the screen, we blit the background surface onto the spot the player that moved was previously on. 
            i.e. if the player moved from 2 to 4, we need to 'erase' the image of the player that is at 2.
            surface is the top most interface.
Player (helper function in method move_player)
random_roll()
No input
Returns tuple where index 0 is the image and index 1 is the number that will be the corresponding number as an int
This function randomly generates a number and then corresponds that number to its corresponding dice image
Player (helper function in method move_player in random_roll())
dice_images
List of images as png
List of the loaded images
This helper function makes the list of the loaded images that will accessed by random_roll
Player (helper function in method move_player)
check_game_over
Position - position of the player
Returns true or false for if the game is over
The method will check if the 'spot' is within the dictionary of coordinates. 
            If it is, then the game will continue.
            If the spot of a player is 100, then that means the player has won the game. The screen will fill and indicate which player has won
            and will inform how many rolls it took to win
TestBoard
test_chutes_dict
self
OK if assert declaration is true 
this test sees if the chutes are all accurate to resembling a 'slide down'
        Since algorithm takes in the key and then moves the player to the value
        we will test to see that all keys are more than (therefore further up)
        than their associate value
TestBoard
test_ladders_dict
self
OK if assert declaration is true 
this test sees if the ladders are all accurate to resembling a 'climb up'
        Since algorithm takes in the key and then moves the player to the value
        we will test to see that all keys are less than (therefore further down)
        than their associate value


Extra Credit (optional)
Use this space to discuss justification and implementation of any extra credit.
We implemented numerous other features listed below:
We made an algorithm that for every game, there are different chutes and different ladders. The angle of the chutes/ladders and the size of the chutes/ladders differs every time a new game is played. Rather than making stagnant chutes and ladders dictionaries, we made functions that create new chutes and ladders for each time the game is played. This shows extra complexity since an algorithm must create the dictionaries that contain a number of chutes and ladders. The chutes function checks to ensure that the key is greater than the value and the ladder checks for vice versa and also that the key and value do not lie in the same row. This demonstrates complexity rather than hard coding two dictionaries for the chutes and ladders.

Advanced use of Python Library:
We showed advanced understanding of the pygame library and how the graphics of the library appear. One of the key distinctions of using pygame is understanding how the screens, surfaces, and sprites interact with each other. In order to make sure that there are not side effects when each are called or lingering effects of previous calls on the interface for the user. We learned how to situate players on the board in the center of each spot.

Advanced Use of OOP:
Multiple Classes: We made both a player class with multiple methods that control the players movement and placement on the board in addition to creating a Button class for the exit button.

