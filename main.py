import pygame
import socket
import time

pygame.init()
print pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)
screen.fill((255,255,255))
pygame.display.set_caption("Planes and Tanks")
test = pygame.image.load('airplane.png')
screen.blit(test,(0,0))
pygame.display.update()

time.sleep(5)