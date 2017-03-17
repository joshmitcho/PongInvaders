import pygame


class Bullet:

    velocity = 25

    def __init__(self, positionX, positionY):
        self.sprite = pygame.image.load("Resources\\Images\\bullet.png")
        self.rect = self.sprite.get_rect()
        self.rect.centerx = positionX
        self.rect.bottom = positionY
        self.speed = [0, -self.velocity]

    def slide(self):
        self.rect.move_ip(self.speed)

