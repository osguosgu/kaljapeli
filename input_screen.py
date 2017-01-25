'''
This function takes the pygame display and 
question string as arguments and 
returns the value of user input after 
the user has pressed enter
'''

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def Input_screen(ask):
	pygame.init()
	screen = pygame.display.set_mode((400, 200))
	value = ""
	font = pygame.font.Font(None, 50)
	while True:

		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				if evt.unicode.isalpha():
					value += evt.unicode
				elif evt.key == K_BACKSPACE:
					value = value[:-1]
				elif evt.key == K_RETURN:
					return value
			elif evt.type == QUIT:
				return

		screen.fill((0, 0, 0))
		block = font.render(value, True, (255, 255, 255))
		rect = block.get_rect()
		rect.center = screen.get_rect().center
		fontobject = pygame.font.Font(None,46)
		screen.blit(fontobject.render(ask, 1, (255,255,255)), (screen.get_width()/2-fontobject.size(ask)[0]/2, screen.get_height()/2-50))
		screen.blit(block, rect)
		pygame.display.flip()