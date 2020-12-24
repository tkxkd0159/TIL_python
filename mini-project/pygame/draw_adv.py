import sys
import pygame as pg
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION



if __name__ == "__main__":
    pg.init()
    pg.key.set_repeat(5, 5)
    WIN_SIZE = (300, 200)
    SURFACE = pg.display.set_mode(WIN_SIZE)
    TIMER = pg.time.Clock()

    FONT = pg.font.SysFont(None, 20, bold=True, italic=True)
    MSG = FONT.render("made by JS Lee", True, (0, 100, 128))
    MSG_RECT = MSG.get_rect()
    MSG_RECT.center = (150, 120)

    STRIP = pg.image.load("img/strip0.png")
    IMG = []
    MOUSE_POS = []
    MOUSE_LINEPOS = []
    MOUSE_DOWN = False

    for index in range(9):
        image = pg.Surface((24, 24))
        roi = Rect(index * 24, 0, 24, 24)
        image.blit(STRIP, (0, 0), roi)
        IMG.append(image)

    CNT = 0
    THETA = 0
    POS_X = 150
    POS_Y = 150
    MOTION_CNT = 0

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                MOUSE_POS.append(event.pos)
                MOUSE_DOWN = True
                MOUSE_LINEPOS.clear()
            elif event.type == MOUSEMOTION:
                if MOUSE_DOWN:
                    MOTION_CNT += 1
                    MOUSE_LINEPOS.append(event.pos)
                    if MOTION_CNT == 1:
                        MOUSE_POS.pop()
            elif event.type == MOUSEBUTTONUP:
                MOUSE_DOWN = False
                MOTION_CNT = 0



            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    POS_X -= 5
                elif event.key == K_RIGHT:
                    POS_X += 5
                elif event.key == K_UP:
                    POS_Y -= 5
                elif event.key == K_DOWN:
                    POS_Y += 5

        SURFACE.fill((0, 0, 0))

        for pos in MOUSE_POS:
            pg.draw.circle(SURFACE, (255, 255, 255), pos, 2)

        if len(MOUSE_LINEPOS) > 1:
            pg.draw.aalines(SURFACE, (255, 255, 255), False, MOUSE_LINEPOS, True)

        NEW_ICON1 = pg.transform.rotate(IMG[CNT % 2 + 0], THETA)
        ICON1_RECT = NEW_ICON1.get_rect()
        ICON1_RECT.center = (60, 60)

        NEW_ICON2 = pg.transform.rotate(IMG[CNT % 2 + 2], THETA)
        ICON2_RECT = NEW_ICON2.get_rect()
        ICON2_RECT.center = (110, 60)

        NEW_ICON3 = pg.transform.rotozoom(IMG[CNT % 2 + 4], THETA, (THETA % 365) / 180)
        ICON3_RECT = NEW_ICON3.get_rect()
        ICON3_RECT.center = (160, 60)

        NEW_ICON4 = pg.transform.rotozoom(IMG[CNT % 2 + 6], THETA, 2 - (THETA % 365) / 180)
        ICON4_RECT = NEW_ICON4.get_rect()
        ICON4_RECT.center = (210, 60)

        SURFACE.blit(NEW_ICON1, ICON1_RECT)
        SURFACE.blit(NEW_ICON2, ICON2_RECT)
        SURFACE.blit(NEW_ICON3, ICON3_RECT)
        SURFACE.blit(NEW_ICON4, ICON4_RECT)
        SURFACE.blit(MSG, MSG_RECT)
        CNT += 1
        THETA += 5

        SURFACE.blit(IMG[8], (POS_X, POS_Y))

        pg.display.update()
        TIMER.tick(30)
