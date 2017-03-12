import sys, pygame
from Classes.Ball import Ball

ball = Ball("left")

pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0
screen = pygame.display.set_mode(size)

def run():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        loop()
        draw()

def loop():
    ball.slide()
    if ball.rect.left < 0 or ball.rect.right > width:
        ball.bounceX()
    if ball.rect.top < 0 or ball.rect.bottom > height:
        ball.bounceY()

def draw():
    screen.fill(black)
    screen.blit(ball.sprite, ball.rect)
    pygame.display.flip()

if __name__ == '__main__':
    run()
