import sys, pygame

class Ball:
    speed = [1, 1]

    def __init__(self, side):
        if side == "left":
            self.position = [0, 10]
        else:
            self.position = [10, 0]
        self.sprite = pygame.image.load("Resources\\Images\\ball.png")
        self.rect = self.sprite.get_rect()
        self.speed = [1, 1]

    def slide(self):
        self.rect = self.rect.move(self.speed)
    def bounceX(self):
        self.speed[0] = -self.speed[0]
        print "bounceX"
    def bounceY(self):
        self.speed[1] = -self.speed[1]
        print "bounceY"
