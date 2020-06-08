import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('forest_background.png')
bg = pygame.transform.scale(background, (800, 600))

pygame.display.set_caption('Apple catcher')

icon = pygame.image.load('physics.png')
pygame.display.set_icon(icon)

mixer.music.load('background.wav')
mixer.music.play(-1)

bowl = pygame.image.load('bowl.png')
# bowl = pygame.transform.scale(bowlnor, (128, 100))
bowlX = 380
bowlY = 480
bowlX_change = 0

bomb = []
bombX = []
bombY = []
bombX_change = []
bombY_change = []
num_of_bombs = 1

for i in range(num_of_bombs):
    bomb.append(pygame.image.load('bomb.png'))
    bombX.append(380)
    bombY.append(-80)
    bombX_change.append(0)
    bombY_change.append(2.4)

apple = []
appleX = []
appleY = []
appleX_change = []
appleY_change = []
num_of_apples = 1

for i in range(num_of_apples):
    apple.append(pygame.image.load('fruit.png'))
    appleX.append(540)
    appleY.append(-170)
    appleX_change.append(0)
    appleY_change.append(2)

banana = []
bananaX = []
bananaY = []
bananaX_change = []
bananaY_change = []
num_of_bananas = 1

for i in range(num_of_apples):
    banana.append(pygame.image.load('banana.png'))
    bananaX.append(440)
    bananaY.append(-10)
    bananaX_change.append(0)
    bananaY_change.append(2.4)


def print_apple(x, y, i):
    screen.blit(apple[i], (x, y))

def collision_cheak(appleX, appleY, bowlX, bowlY):
    distance = math.sqrt((math.pow(appleX - bowlX, 2) + (math.pow(appleY - bowlY, 2))))

    if distance <= 10:
        return True
    else:
        return False

def print_banana(x, y, i):
    screen.blit(banana[i], (x, y))

def collision_test(bananaX, bananaY, bowlX, bowlY):
    distance = math.sqrt((math.pow(bananaX - bowlX, 2) + (math.pow(bananaY - bowlY, 2))))

    if distance <= 10:
        return True
    else:
        return False


def print_bomb(x, y, i):
    screen.blit(bomb[i], (x, y))


def print_bowl():
    screen.blit(bowl, (bowlX, bowlY))


def is_collision(bombX, bombY, bowlX, bowlY):
    distance = math.sqrt((math.pow(bombX - bowlX, 2) + (math.pow(bombY - bowlY, 2))))

    if distance <= 10:
        return True
    else:
        return False


score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_fontX = 10
score_fontY = 10


def print_score():
    score_render = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (score_fontX, score_fontY))


game_over = pygame.font.Font('freesansbold.ttf', 64)
fontX = 200
fontY = 270


def print_game_over():
    game_over_ = game_over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over_, (fontX, fontY))


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bowlX_change = -4
            elif event.key == pygame.K_RIGHT:
                bowlX_change = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bowlX_change = 0
            elif event.key == pygame.K_RIGHT:
                bowlX_change = 0
    for i in range(num_of_bombs):

        collision = is_collision(bombX[i], bombY[i], bowlX, bowlY)
        if collision:
            bombY[i] = 480
            bursted = mixer.Sound('explosion.wav')
            bursted.play()
            print_game_over()

        if bombY[i] >= 536:
            bombY[i] = -80
            bombX[i] = random.randint(200, 600)

        print_bomb(bombX[i], bombY[i], i)
        bombY[i] += bombY_change[i]

    for i in range(num_of_apples):
        if appleY[i] >= 536:
            for j in range(num_of_apples):
                appleX[j] = random.randint(200, 600)
                score -= 1
                appleY[j] = -150

        collision = collision_cheak(appleX[i], appleY[i], bowlX, bowlY)
        if collision:
            score += 1
            appleY[i] = random.choice([-150, -170])
            appleX[i] = random.randint(300, 600)
            apple_bite = mixer.Sound('bite.wav')
            apple_bite.play()

        print_apple(appleX[i], appleY[i], i)

        appleY[i] += appleY_change[i]

    for i in range(num_of_bananas):
        if bananaY[i] >= 536:
            for j in range(num_of_bananas):
                bananaX[j] = random.randint(200, 600)
                score -= 2
                bananaY[j] = -10

        collision = collision_cheak(bananaX[i], bananaY[i], bowlX, bowlY)
        if collision:
            score += 2
            bananaY[i] = random.choice([-10, -11])
            bananaX[i] = random.randint(300, 600)
            banana_bite = mixer.Sound('bite.wav')
            banana_bite.play()

        print_banana(bananaX[i], bananaY[i], i)

        bananaY[i] += bananaY_change[i]
    print_score()
    print_bowl()
    bowlX += bowlX_change
    pygame.display.update()
