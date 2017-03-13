import sys, pygame
from Classes.Ball import Ball
from Classes.Paddle import Paddle

pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = Ball(width, height)
paddleL = Paddle(20)
paddleR = Paddle(width-10)

ballBuffer = 20
ballBufferIncrement = 5


def run():
    count = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        loop(count)
        count = (count + ballBufferIncrement) % ballBuffer
        draw()


def loop(count):
    if count < ballBufferIncrement:
        ball.slide()
    if (ball.rect.left < 0 and ball.speed[0] <= 0) or (ball.rect.right > width and ball.speed[0] >= 0):
        ball.bounceX()
    elif (ball.rect.top < 0 and ball.movingUp()) or (ball.rect.bottom > height and ball.movingDown()):
        ball.bounceY()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        if paddleR.rect.bottom <= height:
            paddleR.down()
    if keys[pygame.K_UP]:
        if paddleR.rect.top >= 0:
            paddleR.up()
    if keys[pygame.K_s]:
        if paddleL.rect.bottom <= height:
            paddleL.down()
    if keys[pygame.K_w]:
        if paddleL.rect.top >= 0:
            paddleL.up()


def draw():
    screen.fill(black)
    screen.blit(ball.sprite, ball.rect)
    screen.blit(paddleL.sprite, paddleL.rect)
    screen.blit(paddleR.sprite, paddleR.rect)
    pygame.display.flip()

if __name__ == '__main__':
    run()
