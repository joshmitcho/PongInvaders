import sys
import pygame
from Classes.Ball import Ball
from Classes.Paddle import Paddle
from Classes.Cannon import Cannon
from Classes.Bullet import Bullet


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

bulletList = []

def run():
    while 1:
        clock.tick(60)

        getDiscreteInput()
        getContinuousInput()
        update()
        draw()


def getDiscreteInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bulletList) == 0:
                bulletList.append(Bullet(cannon.rect.centerx, height - cannon.rect.height))
            if event.key == pygame.K_RETURN and ball.speed == [0, 0]:
                ball.go()


def getContinuousInput():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and paddleL.rect.bottom <= height:
        paddleL.down()
    if keys[pygame.K_UP] and paddleL.rect.top >= 0:
        paddleL.up()

    if keys[pygame.K_LEFT] and cannon.rect.left >= 0:
        cannon.left()
    if keys[pygame.K_RIGHT] and cannon.rect.right <= width:
        cannon.right()


def update():
    global score

    for b in bulletList:
        b.slide()
        if b.rect.bottom <= 0:
            bulletList.remove(b)

    ball.slide()
    paddleR.followBall(ball.rect.centery, screen)

    if ball.rect.colliderect(paddleL.rect) and ball.isMovingLeft():
        ball.rect.left = 31
        ball.bounceX(ball.rect.centery - paddleL.rect.centery)
    elif ball.rect.colliderect(paddleR.rect)  and ball.isMovingRight():
        ball.rect.right = width - 31
        ball.bounceX(ball.rect.centery - paddleR.rect.centery)
    elif (ball.rect.top < 0 and ball.isMovingUp()) or (ball.rect.bottom > height and ball.isMovingDown()):
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
    for b in bulletList:
        screen.blit(b.sprite, b.rect)
    pygame.display.flip()


if __name__ == '__main__':
    run()
