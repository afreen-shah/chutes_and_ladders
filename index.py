import pygame
import board
import button

clock=pygame.time.Clock()

#Initialize
pygame.init()     #initialized pygame
blue = (0,150,250)
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
transparent = (0,0,0,0)

#load button image
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#button instance
exit_button = button.Button(260, 500, exit_img, 0.9)

#Game Loop
player_turn = 0
running=True

while running == True:
    if exit_button.draw(board.end_screen):
        running=False
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running=False
        
        
        #Initialize Player 1 Object
        player1 = board.Player("player1_figure.png", "Player 1", blue)
    
        #Initialize Player 2 Object
        player2 = board.Player("player2_figure.png",'Player 2', red)
        if player_turn == 0:
            #when the player turn is 0, that means that the game has not begun yet therefore the players must be placed onto the board
                player2.set_position(1)
                player1.set_position(1)
                player1.player_button([True])

        # game starting
        if board.player1_position[0] < 100 and board.player2_position[0] < 100:
            #this first conditional tests to see if both players are elligible to move (ie they have not ended at position 100 yet)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_turn += 1
                    if player_turn % 2 == 1:
                        player1.player_button(board.position1_currentplayer)
                    else:
                        player2.player_button(board.position2_currentplayer)
                    
                    player1.move_player(board.player1_position, board.position1_currentplayer)
                    player2.move_player(board.player2_position, board.position2_currentplayer)
                    player1.set_position(board.player1_position[0])
                    player2.set_position(board.player2_position[0])
        elif board.player1_position[0] == 100 or board.player2_position[0] == 100:
            #this elif statement signals the end screen to be blit onto the screen which overlayers all objects on the screen
            board.screen.blit(board.end_screen,(0,0))

                   
            
        clock.tick(60)
        pygame.display.flip()
                
            
#Ending the loop
pygame.quit()





