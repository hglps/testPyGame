#Space invader bases on YouTube video
import pygame
import random as rd
from pygame.locals import *
ScrRes = {'width':800, 'height':600}

pygame.init()
screen = pygame.display.set_mode((ScrRes['width'], ScrRes['height']))

#Icon and title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# User
playerImg = pygame.image.load('userimg.png')
playerXY = {'x':370,'y':480}
playerChange = 0


#Enemy
enemyImg = pygame.image.load('alien.png')
enemyXY = {'x':rd.randint(64,ScrRes['width']-64),'y':50}
enemyChange = 0

#Functions

def showPlayer(img, x,y):
    screen.blit(img, (x,y))
def showEnemy(img,x,y):
    screen.blit(img,(x,y))

#LOOP
while True:

    #Background color
    screen.fill((120,80,120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                playerChange = -1
            if event.key == K_RIGHT:
                playerChange = 1
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                playerChange = 0

    
    print(playerXY['x'],"   ",playerXY['y'])
    playerXY['x'] += playerChange
    playerXY['x'] = playerXY['x'] % ScrRes['width']
    showPlayer(playerImg,playerXY['x'],playerXY['y'])
    showEnemy(enemyImg, enemyXY['x'],enemyXY['y'])
    pygame.display.update()
