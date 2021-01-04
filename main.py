
import os
import pygame
import math
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

BALL_SIZE = 5
gravity = -1


class Ball():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Velocity is (magnitude, radians)
        self.velocity = [0, -math.pi/2]
        self.draw()

    def update(self):
        self.undraw()
        self.velocity[0] += gravity
        self.x = self.x + self.velocity[0] * math.cos(self.velocity[1])
        self.y = self.y + self.velocity[0] * math.sin(self.velocity[1])
        self.draw()

    def draw(self):
        pygame.draw.circle(
            screen, WHITE, [self.x, self.y], BALL_SIZE)

    def undraw(self):
        pygame.draw.circle(screen, BLACK,
                           [self.x, self.y], BALL_SIZE)


def main():

    pygame.init()
    pygame.display.set_caption("Paintball")
    screen.fill(BLACK)

    done = False
    clock = pygame.time.Clock()
    ball = Ball(100, 100)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if ball.y >= 500:
            ball.y = 500
            ball.velocity[0] = -ball.velocity[0]
        ball.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
