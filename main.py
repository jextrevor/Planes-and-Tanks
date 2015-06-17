import pygame
from pygame import *
import threading
import socket
import time
import sys
import os
import netifaces
from pygame.locals import *
import pygame.font, pygame.event, pygame.draw, string
mode = 0
textbox = None
hostsocket = None
hostthread = None
current_name = ""
#0 for main menu
#1 for hosting
#2 for joining
#3 for gameplay
pygame.init()
#print pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)
#[(1680, 1050), (1600, 1024), (1600, 900), (1440, 900), (1400, 1050), (1366, 768)
#, (1280, 1024), (1280, 960), (1280, 800), (1280, 720), (1152, 864), (1024, 768),
# (800, 600), (640, 480)]

# input lib

# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,100)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    600,100), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    604,104), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((320,240))
  print ask(screen, "Name") + " was entered"

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
name = pygame.image.load('pics/name.png').convert()
text = pygame.image.load('pics/text.png').convert()
go = pygame.image.load('pics/go.png').convert()
cancel = pygame.image.load('pics/cancel.png').convert()
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
	screen.blit(title,(offsetx,offsety))
	screen.blit(host,(offsetx,offsety+250))
	screen.blit(join,(offsetx,offsety+400))
	screen.blit(exit,(offsetx,offsety+550))
	screen.blit(by,(offsetx,offsety+700))
	pygame.display.update()
def main():
	global textbox, current_name
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == MOUSEBUTTONDOWN:
				if mode == 0:
					offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
					offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 800)/2
					mouse = pygame.mouse.get_pos()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+250 and mouse[1] < offsety+350:
						hostgame()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+400 and mouse[1] < offsety+500:
						joingame()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+550 and mouse[1] < offsety+650:
						endgame()
				if mode == 1:
					offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
					offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 550)/2
					mouse = pygame.mouse.get_pos()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+450 and mouse[1] < offsety+550:
						mainmenu()
					if mouse[0] > offsetx and mouse[0] < offsetx+600 and mouse[1] > offsety+300 and mouse[1] < offsety+400:
						makegame()
			if event.type == KEYDOWN:
				if mode == 1:
					if event.key == K_BACKSPACE:
						current_name = current_name[:-1]
					elif event.key <= 127:
						asdfasdfasdf = chr(event.key)
						all_keys = pygame.key.get_pressed()
						if all_keys[pygame.K_LSHIFT] or all_keys[pygame.K_RSHIFT]:
							asdfasdfasdf = asdfasdfasdf.upper()
						if len(current_name) < 10:
							current_name += asdfasdfasdf
		#Rendering stuffs
		if mode == 1:
			offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
			offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 550)/2
			screen.fill((255,255,255))
			screen.blit(name,(offsetx,offsety))
			screen.blit(text,(offsetx,offsety+150))
			screen.blit(go,(offsetx,offsety+300))
			screen.blit(cancel,(offsetx,offsety+450))
			#textbox.update(events)
			#textbox.draw(screen)
			font = pygame.font.SysFont('monospace',100)
			screen.blit(font.render(current_name, 1, (0,0,0)),(offsetx,offsety+150))
			pygame.display.update()
		if mode == 0:
			offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
			offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 800)/2
			screen.fill((255,255,255))
			screen.blit(title,(offsetx,offsety))
			screen.blit(host,(offsetx,offsety+250))
			screen.blit(join,(offsetx,offsety+400))
			screen.blit(exit,(offsetx,offsety+550))
			screen.blit(by,(offsetx,offsety+700))
			pygame.display.update()
		if mode == 2:
			pass
def hostgame():
	global mode, textbox
	offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
	offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 550)/2
	#textbox = Input(maxlength=10, color=(0,0,0), prompt='')
	#print "hi"
	#textbox.set_font(pygame.font.SysFont('monospace',100))
	#print "hi2"
	#textbox.set_pos(offsetx,offsety+150)
	#print "hi3"
	mode = 1
	screen.fill((255,255,255))
	screen.blit(name,(offsetx,offsety))
	screen.blit(text,(offsetx,offsety+150))
	screen.blit(go,(offsetx,offsety+300))
	screen.blit(cancel,(offsetx,offsety+450))
	pygame.display.update()
def makegame():
	global hostsocket, hostthread
	hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	hostsocket.bind((myip, 2999))
	hostsocket.listen(5)
	hostthread = threading.Thread(None,hostfunction)
	hostthread.daemon = True
	hostthread.start()
def endgame():
	sys.exit(0)
def joingame():
	global mode
	offsetx = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][0] - 600)/2
	offsety = (pygame.display.list_modes(0,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)[0][1] - 550)/2
	startstring = ".".join(myip.split('.')[0:-1]) + '.'
	for i in range(1,256):
		#print "Checking ip "+startstring+str(i)
		if DoesServiceExist(startstring+str(i),2999):
			pass
	mode = 2
def hostfunction():
	global hostsocket,current_name
	while True:
		(connection, address) = hostsocket.accept()
		print address
		connection.send(current_name)
def DoesServiceExist(host, port):
    host_addr = ""

    try:
        host_addr = socket.gethostbyname(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        s.connect((host, port))
        s.close()
    except:
        return False

    return True
gws = netifaces.gateways()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gws['default'].values()[0][0], 0))
myip = s.getsockname()[0]

main()