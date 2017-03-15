import sys
import pygame
from Classes.Ball import Ball
from Classes.Paddle import Paddle
from Classes.Cannon import Cannon

pygame.init()

clock = pygame.time.Clock()

score = 5
size = width, height = 960, 720
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = Ball(width, height)
paddleL = Paddle(30, True)
paddleR = Paddle(width, False)
cannon = Cannon(width / 2, height)

def run():
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        getInput()
        loop()
        draw()


def getInput():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN] and ball.speed == [0, 0]:
        ball.go()

    if keys[pygame.K_DOWN] and paddleL.rect.bottom <= height:
        paddleL.down()
    if keys[pygame.K_UP] and paddleL.rect.top >= 0:
        paddleL.up()
    if keys[pygame.K_LEFT] and cannon.rect.left >= 0:
        cannon.left()
    if keys[pygame.K_RIGHT] and cannon.rect.right <= width:
        cannon.right()


def loop():
    global score

    ball.slide()
    paddleR.followBall(ball.rect.centery, screen)

    if ball.rect.colliderect(paddleL.rect) and ball.movingLeft():
        ball.rect.left = 31
        ball.bounceX()
    elif ball.rect.right >= width - 30 and ball.movingRight():
        ball.rect.right = width - 31
        ball.bounceX()
    elif (ball.rect.top < 0 and ball.movingUp()) or (ball.rect.bottom > height and ball.movingDown()):
        ball.bounceY()
    elif ball.rect.left < 0:
        ball.reset(width, height)
        score += 1


def draw():
    screen.fill(black)
    screen.blit(ball.sprite, ball.rect)
    screen.blit(paddleL.sprite, paddleL.rect)
    screen.blit(paddleR.sprite, paddleR.rect)
    screen.blit(cannon.sprite, cannon.rect)
    pygame.display.flip()


if __name__ == '__main__':
    run()
