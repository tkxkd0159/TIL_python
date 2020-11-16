import sys
import os
import random
import pygame as pg
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE, K_r

# pyinstaller draw.py --hidden-import pkg_resources.py2_warn --onefile --clean --noconsole

def main():

    game_over = False
    ship_y = 250
    velocity = 0
    score = 0
    slope = random.randint(1, 6)
    walls = 160
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 5, 100, 5, 400))  # width : 10

    parent_path = os.getcwd()
    ship_img = pg.image.load(os.path.join(parent_path, "img\\ship.png"))
    bang_img = pg.image.load(os.path.join(parent_path, "img\\bang.png"))


    while True:
        space_down = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space_down = True

        if not game_over:
            score += 10
            velocity += -3 if space_down else 3
            ship_y += velocity

            # Scroll map automatically
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = random.randint(1, 6) * (-1 if slope > 0 else 1)
                if edge.height >= 160:
                    edge.inflate_ip(0, -20)

            edge.move_ip(5, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-5, 0) for x in holes]

            # Check crash
            if holes[0].top > ship_y or holes[0].bottom < ship_y + 50:
                game_over = True

        SURFACE.fill((0, 255, 0))
        for hole in holes:
            pg.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_img, (0, ship_y))

        score_board = SYSFONT.render(f"score : {score}", True, (0, 0, 225))
        SURFACE.blit(score_board, (600, 20))

        if game_over:
            end_msg = SYSFONT.render(f"press R to restart", True, (255, 255, 255))
            cal_level = int((400 - holes[0].height) / 20)
            level = SYSFONT.render(f"level : {cal_level}", True, (255, 0, 0))
            SURFACE.blit(end_msg, (320, 200))
            SURFACE.blit(level, (370, 240))
            SURFACE.blit(bang_img, (0, ship_y - 40))

            pg.display.update()

            while True:
                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            game_over = False

                if not game_over:
                    ship_y = 250
                    velocity = 0
                    score = 0
                    slope = random.randint(1, 6)
                    holes = []
                    for xpos in range(walls):
                        holes.append(Rect(xpos * 5, 100, 5, 400))
                    break


        pg.display.update()
        FPS.tick(30)


if __name__ == "__main__":
    pg.init()
    pg.key.set_repeat(5, 5)
    SURFACE = pg.display.set_mode((800, 600))
    FPS = pg.time.Clock()
    SYSFONT = pg.font.SysFont("calibri", 36, bold=True)

    main()
