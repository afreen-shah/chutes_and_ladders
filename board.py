
# import libraries 
import pygame
import random

pygame.init()

#colors
blue = (0,150,250)
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)


'''
Step 1: Generating the screens: we have two main interfaces that will be accessed by the code.
screen is a display that the object will be projected onto, but the chutes, ladders, and board will be built into using blit functions which is 
demonstrated and explained further in the code
end_screen is a surface which holds different characteristics than a display. The surface, when called, will overlay blit objects and the screen
underneath it according to the hierarchy of interfaces in pygame
'''
screen = pygame.display.set_mode((750,750))    #sets up screen with length 650 and height 500
end_screen = pygame.Surface((750, 750)) # IMPORTANT: end_screen is a surface on pygame which means that it is locked and can be displayed on top of the screen
pygame.display.set_caption("Chutes and Ladders")   #sets game caption to Snakes and Ladders
screen.fill(black)


#Board block
'''
This block creates a board on the interface of the pygame. The board includes 
the coordinates of each of the positions of the board which is accessible to other classes/functions
Note that the board is a pygame surface which means that it is layered on top of the screen
'''
length = 600                          #board length
height = 600                          #board height
background_surface = pygame.Surface((length+2, height+2)) 
background_surface.fill(black)
num_rows_colums=10                                
square_size = int(length/num_rows_colums)
pos_coordinates = {1:(30,570),2:(90,570),3:(150,570),4:(210,570),5:(270,570),6:(330,570),7:(390,570),8:(450,570),9:(510,570),10:(570,570),11:(570,510),12:(510,510),13:(450,510),14:(390,510),15:(330,510),16:(270,510),17:(210,510),18:(150,510),19:(90,510),20:(30,510),21:(30,450),22:(90,450),23:(150,450),24:(210,450),25:(270,450),26:(330,450),27:(390,450),28:(450,450),29:(510,450),30:(570,450),31:(570,390),32:(510,390),33:(450,390),34:(390,390),35:(330,390),36:(270,390),37:(210,390),38:(150,390),39:(90,390),40:(30,390),41:(30,330),42:(90,330),43:(150,330),44:(210,330),45:(270,330),46:(330,330),47:(390,330),48:(450,330),49:(510,330),50:(570,330),51:(570,270),52:(510,270),53:(450,270),54:(390,270),55:(330,270),56:(270,270),57:(210,270),58:(150,270),59:(90,270),60:(30,270),61:(30,210),62:(90,210),63:(150,210),64:(210,210),65:(270,210),66:(330,210),67:(390,210),68:(450,210),69:(510,210),70:(570,210),71:(570,150),72:(510,150),73:(450,150),74:(390,150),75:(330,150),76:(270,150),77:(210,150),78:(150,150),79:(90,150),80:(30,150),81:(30,90),82:(90,90),83:(150,90),84:(210,90),85:(270,90),86:(330,90),87:(390,90),88:(450,90),89:(510,90),90:(570,90),91:(570,30),92:(510,30),93:(450,30),94:(390,30),95:(330,30),96:(270,30),97:(210,30),98:(150,30),99:(90,30),100:(30,30)}

for x in range(0,length+square_size,square_size):    
    pygame.draw.line(background_surface,blue,(1,x),(length,x),2)
    pygame.draw.line(background_surface,blue,(x,1),(x,length),2)
    #pygame.display.update()

for key in pos_coordinates:
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(str(key), True, white,black)
    textRect = text.get_rect()
    textRect.center = (pos_coordinates[key])
    background_surface.blit(text, textRect)

'''
Step 2: Making the Chutes and Ladders. The chutes and ladders will be randomly generated with each game through the following loops where 
we will mutate a copy of the pos_coordinated library that excludes position 1 and 100 for the sake of the game (no fun if player automatically is on a ladder
or chute from the first position or if a ladder/chute is on the last spot). With each new chute and ladder made, those coordinates are deleted from the dictionary
so that no neither anymore chutes nor ladders will use those spots
'''
coordinates_copy = {k:v for k,v in pos_coordinates.items() if k > 1 if k < 100}
def make_chutes_and_ladders(choice, color,quantity): 
    """
    this functions will create chutes and ladders
    Input: 
    -choice (whether to make a chute or ladder)
    -color (tuple of a color that the apparatus will be)
    -quantity (how many chutes/ladders will be made)
    Output:
    The funciton mutates the ladder/chute dictionaries by adding key value pairs of the beginning and end of each 
    chute/ladder. It will then blit the background surface onto the screen in order to preserve the board 
    """
    dict = {}
    for x in range(quantity): 
        random_pos1 = random.choice(list(coordinates_copy))          
        del coordinates_copy[random_pos1]
        without_pos1row = {k:v for k,v in coordinates_copy.items() if v[1] != list(pos_coordinates[random_pos1])[1]}  # the chutes should not start and end on the the same row so we create a variable that stores all the values that are in the same row as our first position   
        random_pos2 = random.choice(list(without_pos1row)) # pos 2 will not be in the same row as pos 1
        del coordinates_copy[random_pos2]        
        pygame.draw.line(background_surface, color, pos_coordinates[random_pos1], pos_coordinates[random_pos2], 4)
        pygame.display.update() 
        if choice == 'ladders': 
            order = random_pos1 < random_pos2 
        elif choice == 'chutes':
            order = random_pos1 > random_pos2
        if order:
            start = random_pos1
            end = random_pos2
        else:
            start = random_pos2
            end = random_pos1
        dict[start] =end
        '''
        if choice == 'ladders': 
            ladders[start] = end
        elif choice == 'chutes':
            chutes[start] = end
        '''
    
    screen.blit(background_surface, (0, 0))    
    pygame.display.update()
    return dict
'''
Step 3: Making Player Class
Player class accesses the chutes and ladders made in the previous loops therefore, since python interprets code consecutievly we must put the clas
under the loops
'''

#Player Class
# Positions must be mutable and have side effects, so they can be made into global variables
# making these 4 functions into lists makes them mutable in the class methods 
player1_position = [1]
player2_position = [1]
position1_currentplayer = [False]
position2_currentplayer = [True]

# make the ladders and chutes 
                          
ladders = make_chutes_and_ladders('ladders', green , 3) #This is a dictionary of ladders with keys = postion start of ladder and value = position of end of ladder
chutes = make_chutes_and_ladders('chutes', red, 3) #This is a dictionary of chutes with keys = postion start of chutes and value = position of end of chutes


class Player(pygame.sprite.Sprite):
    
    count = 0 # the total amount of rolls throughout a game
    # This class inherits from pygame 
    def __init__(self, player_image , phrase, color):
        '''
        We initialize the object player with the first position (at 1). Each player
        is represented on the board by an image.
        '''
        self.phrase = phrase    
        self.player_image = pygame.transform.scale(pygame.image.load(player_image), (50, 50))
        self.player_rect = self.player_image.get_rect() 
        self.color = color        
        
    
    def set_position(self,  position):
        '''
        Input: position of the player
        This method sets the initial position of the players on the board 
        Output and side effects: blits the player onto the new position that it has been assigned and returns its new location
        '''
        self.player_rect.center = pos_coordinates[position]
        screen.blit(self.player_image, self.player_rect)
        return pos_coordinates[position]
    
    def player_button(self, current_player):
        '''
        Input: self, current_player which is a boolean that denotes if the obejct is the one that is currently supposed to move
        This method instructs which player should press the space button in order to move and will determine which player will move
        Output: Boolean ( True or False) 
        '''
        if current_player[0] == True:
            font = pygame.font.Font('freesansbold.ttf', 25)
            text = font.render(f"{self.phrase} Press the SpaceBar to Roll", True, white, self.color)
            playerRect = text.get_rect()
            playerRect.center = (375,675)
            screen.blit(text, playerRect)
            return False
        else:
            return True

    def move_player(self, position, current_player):
        '''
        This method enables the player to move and create new positions
        The argument position takes in one of the global variables that MUST be a list or global variable in order for the 
        assignment of the variable to mutate
        Inputs: Takes in position of the player and whether it is the current player 
        Outputs: blits the current player onto its new position 
        '''
        #There are 3 total helper functions in the move_player method
        #Helper function 1: clean dirty
        def clean_dirty(position):
            '''
            This helper function will hide the effects of the dirty blit that occur when the players are moving around the screen. An issue with 
            pygame is that when a sprite is 'blit' onto a surface, it will leave a stamp of its image there. When the characters to move, it will 
            leave a trail of where it previously was by nature of the 'blit' function so we need to manually get rid of the previous blits
            This helper function utilizes the pygame 'surface', 'rect', and 'blit' functions
            background_surface is a surface of the board that was captured. Since the board, chutes, and ladders are on the board, but the players
            interact on the screen, we blit the background surface onto the spot the player that moved was previously on. 
            i.e. if the player moved from 2 to 4, we need to 'erase' the image of the player that is at 2.
            surface is the top most interface.

            Input: the position of the object
            Output: blits the background surface with the dimensions of the spot on top of the spot to remove the previous 'stamp' of the blit image
            '''
            screen.blit(background_surface, (position[0]-30,position[1]-30), pygame.Rect((position[0]-30,position[1]-30), (60, 60)))

        #Helper function: Random roll function
        def random_roll():
            '''
            Input: None
            This function randomly generates a number and then corresponds that number to its corresponding dice image
            Return: A tuple of the image and number which can then be accessed by other functions/methods
            '''
            def dice_images(dice_png_list):
                '''
                This helper function makes the list of the loaded images that will accessed by random_roll
                Input: list of the images
                Output: list of the images loaded into pygame
                '''
                images_loaded = [] #non trivial list - stores the loaded images that can accessed and make the code very efficient rather than making if conditionals for each loaded image
                for each_image in dice_png_list:
                    dice = pygame.image.load(each_image)
                    images_loaded.append(dice)
                return images_loaded
            dice_images_list = dice_images(["side_1_of_dice.png","side_2_of_dice.png","side_3_of_dice.png","side_4_of_dice.png","side_5_of_dice.png","side_6_of_dice.png"])
            dice_number = random.randint(1,6)              #Function that returns random number and the correspoding dice image 
            dice_image = dice_images_list[dice_number - 1] # list index starts with 0 so dice image corresponding with 1 is actually at index 0 
            return dice_image,dice_number # this is a tuple where index 0 is the image and index 1 is the number that will be accessible as a number 

        #Helper Function 3: checks if an player has reached the final position
        def check_game_over(spot): 
            '''
            The method will check if the 'spot' is within the dictionary of coordinates. 
            If it is, then the game will continue.
            If the spot of a player is 100, then that means the player has won the game. The screen will fill and indicate which player has won
            and will inform how many rolls it took to win
            Input:
            position ie 1 or 99
            Output:
            update disply to show which player has won
            return true or false for if the game is over 
            '''
            game_over = False
            if spot == 100:   
                game_over = True         
                end_screen.fill(self.color) 
                font = pygame.font.Font('freesansbold.ttf', 25)
                text = font.render(f"{self.phrase} has won. It took {round(Player.count/2)} rolls.", True, white,self.color) # having the {round(Player.count/2)} ensures that the count is always correct since the total rolls when player 1 wins will be odd and even when player 2 wins
                player1Rect = text.get_rect()
                player1Rect.center = (375,375)
                end_screen.blit(text, player1Rect)
            return game_over 
        

        current_player[0] = Player.player_button(self,current_player)
        # conditional to make sure only one player will move at a time 
        if current_player[0] == True:
            Player.count += 1
            roll = random_roll()
            screen.blit(roll[0], (620,300))
            clean_dirty(pos_coordinates[position[0]])
            if position[0] + roll[1] >= 100:
                position[0] = 100
            else:
                position[0] += roll[1]
            # the following conditional tests to see when the player should move. It will first test if the game is over, and if not then the player will move to its new position
            if check_game_over(position[0]) == True:
                check_game_over(position[0])
            else:
                # if game is not over, then players will 'move' by checking if the position is in a chute, ladder, or neither which will determine the next spot
                if position[0] in chutes:
                    position[0] = chutes[position[0]]  
                elif position[0] in ladders:
                    position[0] = ladders[position[0]]
                Player.set_position(self,position[0])
                pygame.display.flip()
    

    
       

    



