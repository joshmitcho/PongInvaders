import sys, pygame


class Paddle:

    velocity = 1

    def __init__(self, position):
        self.sprite = pygame.image.load("Resources\\Images\\paddle.png")
        self.rect = self.sprite.get_rect()
        self.rect.right = position
        self.speed = [0, 0]

    def down(self):
        self.speed[1] = self.velocity
        self.rect = self.rect.move(self.speed)

    def up(self):
        self.speed[1] = -self.velocity
        self.rect = self.rect.move(self.speed)


