import pygame


class Alien:

    jump = 10

    def __init__(self, position):
        self.sprite = pygame.image.load("Resources\\Images\\alien1.png")

        self.rect = self.sprite.get_rect()
        self.rect.right = position

    def down(self):
        self.rect.move_ip([0, self.jump])

    def left(self):
        self.rect.move_ip([-self.jump, 0])

    def right(self):
        self.rect.move_ip([self.jump, 0])
