import sys
import pygame


class Ball:

    def __init__(self, width, height):
        self.sprite = pygame.image.load("Resources\\Images\\ball.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = width/2 - (self.rect.right-self.rect.left)/2
        self.rect.top = height/2 - (self.rect.bottom-self.rect.top)/2
        self.speed = [1, 1]

    def slide(self):
        self.rect.move_ip(self.speed)

    def bounceX(self):
        self.speed[0] = -self.speed[0]

    def bounceY(self):
        self.speed[1] = -self.speed[1]

    def movingUp(self):
        return self.speed[1] <= 0

    def movingDown(self):
        return self.speed[1] >= 0