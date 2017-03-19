import pygame
import random


class Ball:

    def __init__(self, width, height):
        self.sprite = pygame.image.load("Resources\\Images\\ball.png")
        self.rect = self.sprite.get_rect()
        self.reset(width, height)
        self.velocity = 3

    def slide(self):
        self.rect.move_ip(self.speed)

    def bounceX(self, delta):

        absSpeed = abs(self.speed[0])
        self.speed[0] = -(self.speed[0] / absSpeed) * (absSpeed + 1)

        if delta > 0:
            self.speed[1] = abs(self.speed[1])
        elif delta < 0:
            self.speed[1] = -abs(self.speed[1])
        if delta == 0 and random.choice([True, False]):
            self.speed[1] += 1

        self.velocity += 1

    def bounceY(self):
        self.speed[1] = -self.speed[1]

    def isMovingUp(self):
        return self.speed[1] <= 0

    def isMovingDown(self):
        return self.speed[1] >= 0

    def isMovingLeft(self):
        return self.speed[0] <= 0

    def isMovingRight(self):
        return self.speed[0] >= 0

    def reset(self, width, height):
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speed = [0, 0]
        self.velocity = 3

    def go(self):
        self.speed = [self.velocity, self.velocity]
