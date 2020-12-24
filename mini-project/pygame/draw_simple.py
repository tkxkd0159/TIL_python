import sys
import random
from math import sin, cos, radians
import pygame as pg
from pygame.locals import QUIT, Rect


def draw_rect(panel, shape):
    pg.draw.rect(panel, (255, 0, 0), shape)
    pg.draw.rect(panel, (0, 255, 0), shape.move(100, 120), 3)
    pg.draw.rect(panel, (0, 0, 255), shape.move(200, 250).inflate(20, 20), 10)


def draw_grid(panel, size):
    width = size[0]
    height = size[1]

    for xpos in range(0, width+50, 50):
        pg.draw.line(panel, 0xFFFFFF, (xpos, 0), (xpos, height), 1)
    for ypos in range(0, height+50, 50):
        pg.draw.line(panel, 0xFFFFFF, (0, ypos), (width, ypos), 1)

def draw_polygon(panel, vert_n):
    ptlist = []
    for theta in range(0, 360, int(360/vert_n)):
        rad = radians(theta)
        ptlist.append((cos(rad)*50 + 100, sin(rad)*50 + 100))

    pg.draw.polygon(panel, 0xFFFFFF, ptlist)

def draw_etc(panel):
    pg.draw.circle(panel, (100, 100, 100), (150, 100), 10, 5)
    pg.draw.ellipse(panel, (100, 200, 200), (10, 20, 30, 40))




if __name__ == '__main__':
    pg.init()
    WIN_SIZE = (500, 400)
    SURFACE = pg.display.set_mode(WIN_SIZE)
    pg.display.set_caption("Just Window")

    SYS_FONT = pg.font.SysFont(None, 36, bold=True, italic=True)
    TIMER = pg.time.Clock()
    COUNTER = 0
    RECT = Rect(10, 20, 30, 40)
    L_PTLIST = [(250, 200)]

    while True:
        SURFACE.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        draw_rect(SURFACE, RECT)
        draw_grid(SURFACE, WIN_SIZE)
        draw_polygon(SURFACE, 5)
        draw_etc(SURFACE)

        L_XPOS = random.randint(0, 500)
        L_YPOS = random.randint(0, 400)
        L_PTLIST.append((L_XPOS, L_YPOS))
        pg.draw.lines(SURFACE, (188, 131, 190), True, L_PTLIST, 5)

        COUNTER += 1
        COUNT_IMG = SYS_FONT.render(f'count is {COUNTER}', True, (100, 100, 225))
        SURFACE.blit(COUNT_IMG, (200, 200))
        TIMER.tick(1) # 1 loops per a second

        pg.display.update()
