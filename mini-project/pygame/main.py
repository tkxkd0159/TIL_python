import sys
import pygame as pg
from pygame.locals import QUIT


if __name__ == '__main__':
    pg.init()
    SURFACE = pg.display.set_mode((400, 300))
    pg.display.set_caption("Just Window")

    SYS_FONT = pg.font.SysFont(None, 36)
    TIMER = pg.time.Clock()
    COUNTER = 0

    while True:
        SURFACE.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        COUNTER += 1
        COUNT_IMG = SYS_FONT.render(f'count is {COUNTER}', True, (100, 100, 225))
        SURFACE.blit(COUNT_IMG, (50, 50))
        TIMER.tick(10) # 10 loops per a second

        pg.display.update()
