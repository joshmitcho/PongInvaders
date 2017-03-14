import pygame
import random


class Ball:

    def __init__(self, width, height):
        self.sprite = pygame.image.load("Resources\\Images\\ball.png")
        self.rect = self.sprite.get_rect()
        self.reset(width, height)
        self.velocity = 3

    def slide(self):
        print self.speed
        self.rect.move_ip(self.speed)

    def bounceX(self):

        if self.speed[0] > 0:
            self.speed[0] = -self.velocity
        else:
            self.speed[0] = self.velocity

        if random.choice([True, False]):
            self.speed[1] += 1

        self.velocity += 1

    def bounceY(self):
        self.speed[1] = -self.speed[1]

    def movingUp(self):
        return self.speed[1] <= 0

    def movingDown(self):
        return self.speed[1] >= 0

    def movingLeft(self):
        return self.speed[0] <= 0

    def movingRight(self):
        return self.speed[0] >= 0

    def reset(self, width, height):
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speed = [0, 0]

    def go(self):
        self.speed = [self.velocity, self.velocity]
