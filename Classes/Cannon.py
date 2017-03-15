import pygame


class Cannon:

    velocity = 10

    def __init__(self, width, height):
        self.sprite = pygame.image.load("Resources\\Images\\cannon.png")
        self.rect = self.sprite.get_rect()
        self.rect.right = width
        self.rect.bottom = height
        self.speed = [0, 0]

    def left(self):
        self.speed[0] = -self.velocity
        self.rect = self.rect.move(self.speed)

    def right(self):
        self.speed[0] = self.velocity
        self.rect = self.rect.move(self.speed)


