import pygame

#button class
class Button():
	'''
	class 'Button' creates objects that can be interacted with by the user
	'''
	def __init__(self, x_pos, y_pos, image, scale_by):
		'''
		This method initializes the button with the attributes of the self.click, self.image, self.rect .
		Inputs:
		x_pos is the x position on the board that we want the button to be at
		y_pos is the y position on the board that we want the button to be at
		image is the png file which will be scaled by the parameter scale_by

		Outputs:
		Initializes the instance attributes of 
		self.click 
		self.image using image input
		self.rect at position (x_pos,y_pos)
		'''
		self.click = False
		self.image = pygame.transform.scale(image, (int(image.get_width() * scale_by), int(image.get_height() * scale_by)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x_pos, y_pos)
		

	def draw(self, surface):
		'''
		This method draws the button on the surface (which is input as a parameter)
		Inputs:
		surface - surface denotes which of the layers that the button will be projected onto

		Outputs:
		'blit' the button onto the screen 
		'''
		exit_screen = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
				# this conditional implements in the built in functions in pygame so that when the button is pressed, self.click and
				# exit.screen are set to True with the image blit onto the surface 
				self.click = True
				exit_screen = True
		surface.blit(self.image, (self.rect.x, self.rect.y))
		if pygame.mouse.get_pressed()[0] == 0:
			self.click = False

		return exit_screen
