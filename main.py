import pygame
import socket
import time

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
time.sleep(5)