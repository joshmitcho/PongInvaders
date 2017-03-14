import pygame
import math


class Paddle:

    velocity = 10

    def __init__(self, position, isLeft):
        if isLeft:
            self.sprite = pygame.image.load("Resources\\Images\\paddleL.png")
        else:
            self.sprite = pygame.image.load("Resources\\Images\\paddleR.png")

        self.rect = self.sprite.get_rect()
        self.rect.right = position
        self.speed = [0, 0]

    def down(self):
        self.speed[1] = self.velocity
        self.rect.move_ip(self.speed)

    def up(self):
        self.speed[1] = -self.velocity
        self.rect.move_ip(self.speed)

    def followBall(self, ball, screen):
        self.speed[1] = math.floor(-0.05*(self.rect.centery - ball))
        self.rect.move_ip(self.speed)
        self.rect.clamp_ip(screen.get_rect())
