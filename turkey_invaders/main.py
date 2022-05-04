import pygame
import random
import math

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((900,700))
# background = pygame.image.load("images/background.jpg")

#title and icon
pygame.display.set_caption("Turkey Invasion")
icon = pygame.image.load("images/turkey.png")
pygame.display.set_icon(icon)

score = 0
#player
playerImg = pygame.image.load("images/spaceship2.png")
playerX = 400
playerY = 580
playerX_change = 0


def player(x,y):# drawing the image on the screen
    screen.blit(playerImg,(x, y))


#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 7


for i in range(0,num_of_enemies):
    enemyImg.append(pygame.image.load("images/turkey.png"))
    enemyX.append(random.randint(0,836))
    enemyY.append(random.randint(0,150))
    enemyY_change.append(0)
    enemyX_change.append(1)

def enemy(x,y,i):# drawing the image on the screen
    screen.blit(enemyImg[i],(x, y))

#bullet mechanics
bulletImg = pygame.image.load("images/bullet1.png")
bulletX = 0
bulletY = 580
bulletY_change = 3
bulletX_change = 0
bullet_state = "ready"


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+26,y+20))


def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 22:
        return True


#game loop
running = True
while running:
    #rgb colors
    screen.fill((0,0,0))

    # screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Events for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX+=playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 836:
        playerX = 836
    
    # enemy movement
    for i in range(0,num_of_enemies): 
        enemyX[i]+=enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY_change[i] = 30
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] >= 868:
            enemyX_change[i] = -1
            enemyY_change[i] = 30
            enemyY[i]+= enemyY_change[i]

        #collision
        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 580
            bullet_state = "ready"
            score+=1
            print(score)
            enemyX[i] = random.randint(0,900)
            enemyY[i] = random.randint(0,150)
        
        enemy(enemyX[i],enemyY[i],i)
    

    #bullet movement

    if bulletY <= 0:
        bulletY = 580
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change



    player(playerX,playerY)
    pygame.display.update()