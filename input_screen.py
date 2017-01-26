import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


'''
This function takes the pygame display, 
question string and
input restriction flag as arguments and 
returns the value of user input after 
the user has pressed enter
'''

def Input_field(disp, ask, digits_only):
	screen = pygame.Surface((400, 200))
	value = ""
	font = pygame.font.Font(None, 50)
	while True:
		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				if evt.unicode.isdigit() and len(value) < 8:
					value += evt.unicode
				if evt.unicode.isalpha() and len(value) < 8 and digits_only == False:
					value += evt.unicode
				elif evt.key == K_BACKSPACE:
					value = value[:-1]
				elif evt.key == K_RETURN:
					return value

		screen.fill((0, 0, 0))

		block = font.render(value, True, (255, 255, 255))
		rect = block.get_rect()
		rect.center = screen.get_rect().center
		fontobject = pygame.font.Font(None,46)
		screen.blit(fontobject.render(ask, 1, (255,255,255)), (screen.get_width()/2-fontobject.size(ask)[0]/2, screen.get_height()/2-75))
		screen.blit(block, rect)
		disp.blit(screen, (disp.get_width()/2-screen.get_width()/2,disp.get_height()/2-screen.get_height()/2))
		pygame.display.flip()


'''
This function takes the pygame display, 
question string and the selectable options as arguments and 
returns the selected option after 
the user has pressed enter
'''

def Select_field(disp, question, options):
	screen = pygame.Surface((len(options)*200, 200))
	font = pygame.font.Font(None, 50)

	selection = 0


	while True:
		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				if evt.key == K_LEFT:
					if selection == 0:
						selection = len(options) - 1
					else:
						selection -= 1
				elif evt.key == K_RIGHT:
					if selection == len(options) - 1:
						selection = 0
					else:
						selection += 1
				elif evt.key == K_RETURN:
					return options[selection]

		screen.fill((0, 0, 0))

		for i in range(len(options)):
			block_width = screen.get_width()/len(options)
			block = pygame.Rect(i*block_width + 10, screen.get_height()/2, block_width - 20, 75)
			if i == selection:
				pygame.draw.rect(screen, (100,100,255), block, 3)
			else:
				pygame.draw.rect(screen, (255,255,255), block, 1)
			fontobject = pygame.font.Font(None,46)
			screen.blit(fontobject.render(options[i], 1, (255,255,255)), (i*block_width + 10, screen.get_height()/2))
		
		fontobject = pygame.font.Font(None,46)
		screen.blit(fontobject.render(question, 1, (255,255,255)), (screen.get_width()/2-fontobject.size(question)[0]/2, screen.get_height()/2-75))
		disp.blit(screen, (disp.get_width()/2-screen.get_width()/2,disp.get_height()/2-screen.get_height()/2))
		pygame.display.flip()
