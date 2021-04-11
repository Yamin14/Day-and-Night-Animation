import pygame
from math import *
pygame.init()

screen = pygame.display.set_mode((720, 1440))
running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
gray = (70, 70, 70)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
light_blue = (0, 200, 255)

#bg
bg = light_blue
x1, y1 = 360, 320
x2, y2 = 360, 1720
speed = 0
const = 1

while running:
	screen.fill(bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#sun
	pygame.draw.circle(screen, yellow, (x1, y1), 100)
	x1 = 360 - (720*sin(radians(speed)))
	y1 = 1020 + (720*cos(radians(speed)))
	
	#moon
	pygame.draw.circle(screen, grey, (x2, y2), 50)
	x2 = 360 - (720*sin(radians(speed-180)))
	y2 = 1020 + (720*cos(radians(speed-180)))
	
	speed += const

	#day and night
	if y1 <= 1020:
		bg = light_blue
	else:
		bg = gray
	
	pygame.display.flip()

pygame.quit()
