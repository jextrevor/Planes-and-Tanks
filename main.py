import pygame
from pygame import *
import threading
import socket
import time
import sys
import os
import netifaces
mode = 0
#0 for main menu
#1 for hosting
#2 for joining
#3 for gameplay
pygame.init()
#print pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)
#[(1680, 1050), (1600, 1024), (1600, 900), (1440, 900), (1400, 1050), (1366, 768)
#, (1280, 1024), (1280, 960), (1280, 800), (1280, 720), (1152, 864), (1024, 768),
# (800, 600), (640, 480)]
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)
screen.fill((255,255,255))
pygame.display.set_caption("Planes and Tanks")
offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 800)/2
title = pygame.image.load('pics/title.png').convert()
host = pygame.image.load('pics/host.png').convert()
join = pygame.image.load('pics/join.png').convert()
exit = pygame.image.load('pics/exit.png').convert()
by = pygame.image.load('pics/by.png').convert()
screen.blit(title,(offsetx,offsety))
screen.blit(host,(offsetx,offsety+250))
screen.blit(join,(offsetx,offsety+400))
screen.blit(exit,(offsetx,offsety+550))
screen.blit(by,(offsetx,offsety+700))
pygame.display.update()
def mainmenu():
	global mode
	mode = 0
	screen.fill((255,255,255))
	offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
	offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 800)/2
	title = pygame.image.load('pics/title.png').convert()
	host = pygame.image.load('pics/host.png').convert()
	join = pygame.image.load('pics/join.png').convert()
	exit = pygame.image.load('pics/exit.png').convert()
	by = pygame.image.load('pics/by.png').convert()
	screen.blit(title,(offsetx,offsety))
	screen.blit(host,(offsetx,offsety+250))
	screen.blit(join,(offsetx,offsety+400))
	screen.blit(exit,(offsetx,offsety+550))
	screen.blit(by,(offsetx,offsety+700))
	pygame.display.update()
def main():
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				if mode == 0:
					mouse = pygame.mouse.get_pos()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+250 and mouse[1] < offsety+350:
						hostgame()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+400 and mouse[1] < offsety+500:
						joingame()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+550 and mouse[1] < offsety+650:
						endgame()
def hostgame():
	global mode
	mode = 1
	screen.fill((255,255,255))
	offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
	offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 550)/2
	name = pygame.image.load('pics/name.png').convert()
	text = pygame.image.load('pics/text.png').convert()
	go = pygame.image.load('pics/go.png').convert()
	cancel = pygame.image.load('pics/cancel.png').convert()
	screen.blit(name,(offsetx,offsety))
	screen.blit(text,(offsetx,offsety+150))
	screen.blit(go,(offsetx,offsety+300))
	screen.blit(cancel,(offsetx,offsety+450))
	pygame.display.update()
def endgame():
	sys.exit(0)
def joingame():
	print "hi2"


gws = netifaces.gateways()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gws['default'].values()[0][0], 0))
print s.getsockname()[0]

main()