import pygame
import sys
from random import randint
#  from pyvidplayer import Video
import random
import math

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
WIDTH, HEIGHT = 1470, 900
pi = 3.14
diff, musst, suit, cut_scene, im, subst, dif_k = '', -1, 'tasm2s', 0, 0, 0, 0
SCREEN = pygame.display.set_mode((1470, 920))
pygame.display.set_caption("Spider-Man")
infoObject = pygame.display.Info()
# display_w, display_h = pygame.display.Info().current_w, pygame.display.Info().current_h
display_w, display_h = WIDTH, HEIGHT
kx, ky = 1, 1
running = True
st = 0


def main_menu():
    global st
    global cut_scene
    global im
    global diff
    global musst
    global suit
    global subst
    expectation = randint(500, 600)
    # randint(1500, 2600)
    pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Music/Web Launch.wav")
    pygame.mixer.music.play()
    while running:
        if st == 0:
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                    "/Fonts/GULAG.otf", 120 * kx)
            text = font.render('Spider-Man', True, pygame.Color('WHITE'))
            tx, ty = display_w // 2 - len('Spider-Man  ') * 120 * kx // 4, display_h // 4 - 60 * ky - 90
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/Home_screen.png").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h + 20))
            SCREEN.blit(intro_image, (0, 0))
            SCREEN.blit(text, (tx, ty))
            pygame.display.update()
            pygame.time.wait(5000)
            # pygame.time.wait(500)
            st = 1
            text = font.render('START', True, pygame.Color('RED'))
            text.set_alpha(50)
            tx, ty = display_w // 2 - len('START') * 120 * kx // 4, display_h // 4 - 60 * ky - 20
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/newgamescreen.jpg").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            SCREEN.blit(text, (tx, ty))
            pygame.display.update()
        if st == 1:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/newgamescreen.jpg").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                    "/Fonts/GULAG.otf", 120 * kx)
            text = font.render('START', True, pygame.Color('RED'))
            tx, ty = display_w // 2 - len('START') * 120 * kx // 4, display_h // 4 - 120 * ky // 2 - 20
            for event1 in pygame.event.get():
                if event1.type == pygame.MOUSEMOTION:
                    if tx < event1.pos[0] < display_w // 2 + len('START') * 120 * kx // 4 \
                            and ty < event1.pos[1] < display_h // 4 + 120 * ky // 2 + 20:
                        text.set_alpha(255)
                    else:
                        text.set_alpha(50)
                    SCREEN.blit(text, (tx, ty))
                    pygame.display.update()
                else:
                    text.set_alpha(50)
                    SCREEN.blit(text, (tx, ty))
                    pygame.display.update()
                if event1.type == pygame.MOUSEBUTTONDOWN \
                        and tx < event1.pos[0] < display_w // 2 + len('START') * 120 * kx // 4 \
                        and ty < event1.pos[1] < display_h // 4 + 120 * ky // 2 + 20:
                    st = 2
                    im = 0
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        if st == 2:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/BS_menu.png").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            save_slots = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                           "/Pictures/BS Menu/save_slots.png").convert_alpha()
            save_slots = pygame.transform.scale(save_slots, (480, 810))
            SCREEN.blit(save_slots, (140, 50))
            pygame.draw.line(SCREEN, (255, 255, 255), (169 * kx, 168 * ky + 91 * im * ky),
                             (172 * kx, 168 * ky + 91 * im * ky), 1)
            pygame.draw.circle(SCREEN, (255, 255, 255), (184 * kx, 168 + 91 * im), 8, 2)
            pygame.draw.circle(SCREEN, (255, 255, 255), (184 * kx, 168 + 91 * im), 4, 2)
            s = pygame.Surface((400, 85))
            s.fill((21, 57, 92))
            s.set_alpha(160)
            SCREEN.blit(s, (196, 125 * ky + 91 * im * ky))
            pygame.draw.line(SCREEN, (255, 255, 255), (196 * kx, 125 * ky + 91 * im * ky),
                             (196 * kx, 145 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (195 * kx, 124 * ky + 91 * im * ky),
                             (216 * kx, 124 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (196 * kx, 189 * ky + 91 * im * ky),
                             (196 * kx, 209 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (195 * kx, 210 * ky + 91 * im * ky),
                             (216 * kx, 210 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (594 * kx, 125 * ky + 91 * im * ky),
                             (594 * kx, 145 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (575 * kx, 124 * ky + 91 * im * ky),
                             (595 * kx, 124 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (594 * kx, 189 * ky + 91 * im * ky),
                             (594 * kx, 209 * ky + 91 * im * ky), 3)
            pygame.draw.line(SCREEN, (255, 255, 255), (575 * kx, 210 * ky + 91 * im * ky),
                             (595 * kx, 210 * ky + 91 * im * ky), 3)
            f = open("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Saves.txt", mode="r")
            txt = f.readlines()
            for i in txt:
                if i != '':
                    pygame.draw.rect(SCREEN, (161, 3, 34), (203 * kx, 131 * ky + 91 * txt.index(i) * ky, 385, 73))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                            "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 40 * kx)
                    text = font.render(str(txt.index(i) + 1), True, (255, 255, 255))
                    tx, ty = 220, 145
                    SCREEN.blit(text, (tx * kx, ty * ky + 91 * txt.index(i) * ky))
            f.close()
            pygame.display.update()
            for event1 in pygame.event.get():
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_UP:
                        if im > 0:
                            im -= 1
                    if event1.key == pygame.K_DOWN:
                        if im < 5:
                            im += 1
                    if event1.key == pygame.K_x:
                        st = 3
                        im = 0
                    if event1.key == pygame.K_o:
                        st = 0
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        if st == 3:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/BS_menu.png").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            pygame.draw.rect(SCREEN, (53, 108, 161), (140 * kx, 48 * ky, 480, 341))
            pygame.draw.rect(SCREEN, (24, 80, 133), (140 * kx, 341 * ky, 480, 259))
            s = pygame.Surface((480, 263))
            s.fill((53, 108, 161))
            s.set_alpha(125)
            SCREEN.blit(s, (140, 600))
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 48 * ky),
                             (140 * kx, 150 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 160 * ky),
                             (140 * kx, 163 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 173 * ky),
                             (140 * kx, 710 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 720 * ky),
                             (140 * kx, 723 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 733 * ky),
                             (140 * kx, 861 * ky), 2)

            pygame.draw.line(SCREEN, (255, 255, 255), (620 * kx, 48 * ky),
                             (620 * kx, 150 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (620 * kx, 160 * ky),
                             (620 * kx, 163 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (620 * kx, 173 * ky),
                             (620 * kx, 710 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (620 * kx, 720 * ky),
                             (620 * kx, 723 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (620 * kx, 733 * ky),
                             (620 * kx, 861 * ky), 1)

            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 27 * kx)
            text = font.render("SELECT DIFFICULTY", True, (255, 255, 255))
            tx, ty = 160, 65
            SCREEN.blit(text, (tx * kx, ty * ky))
            pygame.draw.line(SCREEN, (255, 255, 255), (160 * kx, 102 * ky),
                             (185 * kx, 102 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (190 * kx, 102 * ky),
                             (194 * kx, 102 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (200 * kx, 102 * ky),
                             (600 * kx, 102 * ky), 1)

            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 117 * ky),
                             (165 * kx, 125 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 135 * ky),
                             (165 * kx, 305 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 315 * ky),
                             (165 * kx, 323 * ky), 2)
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 23 * kx)
            pygame.draw.line(SCREEN, (255, 255, 255), (171 * kx, 147 * ky + 40 * im * ky),
                             (174 * kx, 147 * ky + 40 * im * ky), 1)
            pygame.draw.circle(SCREEN, (255, 255, 255), (185, 147 + 40 * im), 8, 2)
            pygame.draw.circle(SCREEN, (255, 255, 255), (185 * kx, 147 + 40 * im), 4, 2)
            s = pygame.Surface((360, 32))
            s.fill((21, 57, 92))
            s.set_alpha(160)
            SCREEN.blit(s, (200, 130 * ky + 40 * im * ky))
            pygame.draw.line(SCREEN, (255, 255, 255), (200 * kx, 130 * ky + 40 * im * ky),
                             (210 * kx, 130 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (200 * kx, 130 * ky + 40 * im * ky),
                             (200 * kx, 140 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (200 * kx, 162 * ky + 40 * im * ky),
                             (210 * kx, 162 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (200 * kx, 152 * ky + 40 * im * ky),
                             (200 * kx, 162 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (550 * kx, 130 * ky + 40 * im * ky),
                             (560 * kx, 130 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (560 * kx, 130 * ky + 40 * im * ky),
                             (560 * kx, 140 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (550 * kx, 162 * ky + 40 * im * ky),
                             (560 * kx, 162 * ky + 40 * im * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (560 * kx, 152 * ky + 40 * im * ky),
                             (560 * kx, 162 * ky + 40 * im * ky), 2)
            text = font.render("FRIENDLY NEIGHBOURHOOD", True, (255, 255, 255))
            tx, ty = 210, 135
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("THE AMAZING", True, (255, 255, 255))
            tx, ty = 210, 175
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("SPECTACULAR", True, (255, 255, 255))
            tx, ty = 210, 215
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("ULTIMATE", True, (255, 255, 255))
            tx, ty = 210, 255
            SCREEN.blit(text, (tx * kx, ty * ky))
            for i in range(0, 3):
                s = pygame.Surface((250, 15))
                s.fill((35, 39, 66))
                s.set_alpha(155)
                SCREEN.blit(s, (350, 685 + 30 * i))
                pygame.draw.rect(SCREEN, (255, 255, 255), (349 * kx, 684 * ky + 30 * i, 252, 17), 2)
            if im == 0:
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                        "Marvel's Spider-Man 2D/Fonts/Old-Soviet.otf", 20 * kx)
                text = font.render("This setting is for expert players who", True, (255, 255, 255))
                tx, ty = 160, 400
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("enjoy a brutally         experience.", True, (255, 255, 255))
                tx, ty = 160, 462
                SCREEN.blit(text, (tx * kx, ty * ky))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                        "Marvel's Spider-Man 2D/Fonts/Avengeance-E1zj.otf", 30 * kx)
                text = font.render("Fun", True, (255, 255, 255))
                tx, ty = 360, 455
                SCREEN.blit(text, (tx * kx, ty * ky))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 686 * ky, 50, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 716 * ky, 70, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 746 * ky, 60, 13))
            elif im == 1:
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                        "Marvel's Spider-Man 2D/Fonts/Old-Soviet.otf", 20 * kx)
                text = font.render("This setting is for players who want", True, (255, 255, 255))
                tx, ty = 160, 380
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("to enjoy the story without", True, (255, 255, 255))
                tx, ty = 160, 442
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("challenging combat.", True, (255, 255, 255))
                tx, ty = 160, 504
                SCREEN.blit(text, (tx * kx, ty * ky))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 686 * ky, 100, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 716 * ky, 85, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 746 * ky, 95, 13))
            elif im == 2:
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                        "Marvel's Spider-Man 2D/Fonts/Old-Soviet.otf", 20 * kx)
                text = font.render("This setting is for players who like a", True, (255, 255, 255))
                tx, ty = 160, 380
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("balanced experience with some", True, (255, 255, 255))
                tx, ty = 160, 442
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("challenge", True, (255, 255, 255))
                tx, ty = 160, 504
                SCREEN.blit(text, (tx * kx, ty * ky))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 686 * ky, 126, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 716 * ky, 126, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 746 * ky, 126, 13))
            elif im == 3:
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                        "Marvel's Spider-Man 2D/Fonts/Old-Soviet.otf", 20 * kx)
                text = font.render("This setting is for players who enjoy", True, (255, 255, 255))
                tx, ty = 160, 380
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("challenging combat. Enemies will be", True, (255, 255, 255))
                tx, ty = 160, 442
                SCREEN.blit(text, (tx * kx, ty * ky))
                text = font.render("stronger and more aggressive.", True, (255, 255, 255))
                tx, ty = 160, 504
                SCREEN.blit(text, (tx * kx, ty * ky))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 686 * ky, 170, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 716 * ky, 180, 13))
                pygame.draw.rect(SCREEN, (255, 0, 43), (351 * kx, 746 * ky, 165, 13))
            spider_logo = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/spider_logo_tr.png").convert_alpha()
            spider_logo = pygame.transform.scale(spider_logo, (80 * kx, 80 * ky))
            SCREEN.blit(spider_logo, (340, 560))
            pygame.draw.line(SCREEN, (255, 255, 255), (155 * kx, 600 * ky),
                             (330 * kx, 600 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (430 * kx, 600 * ky),
                             (605 * kx, 600 * ky), 1)
            pygame.draw.circle(SCREEN, (255, 255, 255), (335, 600), 1, 2)
            pygame.draw.circle(SCREEN, (255, 255, 255), (425, 600), 1, 2)

            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 23 * kx)
            text = font.render("ENEMIES", True, (255, 255, 255))
            tx, ty = 195, 640
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("AGRESSIVE", True, (255, 255, 255))
            tx, ty = 195, 680
            text.set_alpha(155)
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("DAMAGE", True, (255, 255, 255))
            tx, ty = 195, 710
            text.set_alpha(155)
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("HEALTH", True, (255, 255, 255))
            tx, ty = 195, 740
            text.set_alpha(155)
            SCREEN.blit(text, (tx * kx, ty * ky))
            pygame.display.update()
            for event1 in pygame.event.get():
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_UP:
                        if im > 0:
                            im -= 1
                    if event1.key == pygame.K_DOWN:
                        if im < 3:
                            im += 1
                    if event1.key == pygame.K_x:
                        st = 4
                        im = 0
                        subst = 'OFF'
                        if im == 0:
                            diff = 'FN'
                            # friendly neighborhood
                        elif im == 1:
                            diff = 'F'
                            # friendly
                        elif im == 1:
                            diff = 'A'
                            # amazing
                        elif im == 1:
                            diff = 'S'
                            # spectacular
                    if event1.key == pygame.K_o:
                        st = 2
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        if st == 4:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/BS_menu.png").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            pygame.draw.rect(SCREEN, (53, 108, 161), (140 * kx, 48 * ky, 720, 500))
            s = pygame.Surface((720, 363))
            s.fill((53, 108, 161))
            s.set_alpha(125)
            SCREEN.blit(s, (140, 500))
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 48 * ky),
                             (140 * kx, 150 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 160 * ky),
                             (140 * kx, 163 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 173 * ky),
                             (140 * kx, 710 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 720 * ky),
                             (140 * kx, 723 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (140 * kx, 733 * ky),
                             (140 * kx, 861 * ky), 2)

            pygame.draw.line(SCREEN, (255, 255, 255), (860 * kx, 48 * ky),
                             (860 * kx, 150 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (860 * kx, 160 * ky),
                             (860 * kx, 163 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (860 * kx, 173 * ky),
                             (860 * kx, 710 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (860 * kx, 720 * ky),
                             (860 * kx, 723 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (860 * kx, 733 * ky),
                             (860 * kx, 861 * ky), 1)

            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 27 * kx)
            text = font.render("BEFORE YOU START", True, (255, 255, 255))
            tx, ty = 160, 65
            SCREEN.blit(text, (tx * kx, ty * ky))
            pygame.draw.line(SCREEN, (255, 255, 255), (160 * kx, 102 * ky),
                             (220 * kx, 102 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (225 * kx, 102 * ky),
                             (230 * kx, 102 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (230 * kx, 102 * ky),
                             (820 * kx, 102 * ky), 1)

            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 117 * ky),
                             (165 * kx, 127 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 137 * ky),
                             (165 * kx, 465 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (165 * kx, 475 * ky),
                             (165 * kx, 485 * ky), 2)
            pygame.draw.line(SCREEN, (255, 255, 255), (175 * kx, 158 * ky + 30 * im * ky),
                             (179 * kx, 158 * ky + 30 * im * ky), 1)
            spider_logo = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/spider_logo_tr.png").convert_alpha()
            spider_logo = pygame.transform.scale(spider_logo, (80 * kx, 80 * ky))
            SCREEN.blit(spider_logo, (470, 780))
            pygame.draw.line(SCREEN, (255, 255, 255), (275 * kx, 820 * ky),
                             (465 * kx, 820 * ky), 1)
            pygame.draw.line(SCREEN, (255, 255, 255), (555 * kx, 820 * ky),
                             (745 * kx, 820 * ky), 1)
            pygame.draw.circle(SCREEN, (255, 255, 255), (475, 821), 1, 3)
            pygame.draw.circle(SCREEN, (255, 255, 255), (545, 821), 1, 3)
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/Old-Soviet.otf", 25 * kx)
            text = font.render('More functions in next updates!', True, pygame.Color("White"))
            SCREEN.blit(text, (160 * kx, 505 * ky))
            pygame.draw.circle(SCREEN, (255, 255, 255), (193, 159 + 30 * im), 8, 2)
            pygame.draw.circle(SCREEN, (255, 255, 255), (193 * kx, 159 + 30 * im), 4, 2)
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/"
                                    "Marvel's Spider-Man 2D/Fonts/MonospaceBold.ttf", 24 * kx)
            text = font.render("START", True, (255, 255, 255))
            tx, ty = 220, 145
            if im == 0:
                text.set_alpha(255)
            else:
                text.set_alpha(155)
            SCREEN.blit(text, (tx * kx, ty * ky))
            text = font.render("SUBTITLES", True, (255, 255, 255))
            tx, ty = 220, 175
            if im == 1:
                text.set_alpha(255)
            else:
                text.set_alpha(155)
            SCREEN.blit(text, (tx * kx, ty * ky))
            if subst == 'ON':
                text = font.render("< ON >", True, (255, 255, 255))
                tx, ty = 550, 175
                SCREEN.blit(text, (tx * kx, ty * ky))
            else:
                text = font.render("< OFF >", True, (255, 255, 255))
                tx, ty = 550, 175
                SCREEN.blit(text, (tx * kx, ty * ky))
            pygame.display.update()
            for event1 in pygame.event.get():
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_UP:
                        if im > 0:
                            im -= 1
                    if event1.key == pygame.K_DOWN:
                        if im < 1:
                            im += 1
                    if event1.key == pygame.K_LEFT and im == 1:
                        if subst == 'ON':
                            subst = 'OFF'
                    if event1.key == pygame.K_RIGHT and im == 1:
                        if subst == 'OFF':
                            subst = 'ON'
                    if event1.key == pygame.K_x:
                        pygame.mixer.music.pause()
                        st = 5
                        vp = 0
                        d_arc = 0.0
                        time = 0
                    if event1.key == pygame.K_o:
                        st = 3
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        if st == 5:
            if d_arc < 2 * pi:
                d_arc += pi / 50
            else:
                d_arc = 0.0
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/"
                                            "Marvel's Spider-Man 2D/Pictures/BS Menu/black_screen.webp").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            spider_logo = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/BS Menu/spider_logo_tr.png").convert_alpha()
            spider_logo = pygame.transform.scale(spider_logo, (70 * kx, 70 * ky))
            SCREEN.blit(spider_logo, (display_w - 100, display_h - 100))
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 100, display_h - 100, 70, 70),
                            pi + d_arc, 5 * pi / 4 + d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 100, display_h - 100, 70, 70),
                            3 * pi / 2 + d_arc, 7 * pi / 4 + d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 100, display_h - 100, 70, 70),
                            0 + d_arc, pi / 4 + d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 100, display_h - 100, 70, 70),
                            pi / 2 + d_arc, 3 * pi / 4 + d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 105, display_h - 105, 80, 80),
                            0 - d_arc, pi / 2 - d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 105, display_h - 105, 80, 80),
                            2 * pi / 3 - d_arc, 7 * pi / 6 - d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 105, display_h - 105, 80, 80),
                            4 * pi / 3 - d_arc, 11 * pi / 6 - d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 110, display_h - 110, 90, 90),
                            0 + d_arc, 5 * pi / 6 + d_arc)
            pygame.draw.arc(SCREEN, pygame.Color('White'),
                            (display_w - 110, display_h - 110, 90, 90),
                            pi + d_arc, 11 * pi / 6 + d_arc)
            pygame.display.update()
            pygame.time.wait(7)
            time += 7
            if time >= expectation:
                if vp == 0:
                    main_game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                quit()


def menu():
    global im
    global diff
    global musst
    global suit
    global st
    mst, choose_sst, st = 1, '', 0
    expectation = randint(1000, 2000)
    # randint(1500, 2500)
    pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Music/Pause Menu.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    # 144  9 7 7 9 8 10 12 12 12 11 17 30
    red_icons_text = ['', ' MAP', 'SUITS', 'GADGETS', 'SKILLS', 'MISSIONS', 'COLLECTIONS      ', 'BENCHMARKS',
                      'CHARACTERS',
                      'MOVES LIST           ', '']
    equipments_icon = ['SUIT', 'SUIT POWER', 'SUIT MODS']
    suits = ['adss_icon.png', 'adss2.0_icon.png', 'bgs_icon.png', 'bts_icon.png', 'cs_icon.png', 'hs_icon.png', 'iss_icon.png',
             'nms_icon.png', 'pbps_icon.png', 'scss_icon.png', 'sm99s_icon.png',
             'sps_icon.png', 'tasm2s_icon.png', 'tasms_icon.png', 'us_icon.png',
             'ws_icon.png']
    qx, qy, mdx, mdy, ix, iy = 0, 0, 0, 0, 0, 0
    red_icons_weight = [round(6.2 / 100 * display_w, 0), round(4.87 / 100 * display_w, 0),
                        round(4.86 / 100 * display_w, 0), round(6.3 / 100 * display_w, 0),
                        round(5.5 / 100 * display_w, 0), round(6.95 / 100 * display_w, 0),
                        round(8.2 / 100 * display_w, 0), round(8.3 / 100 * display_w, 0),
                        round(8.4 / 100 * display_w, 0), round(7.6 / 100 * display_w, 0),
                        round(11.8 / 100 * display_w, 0)]
    red_icons_height = round(9.75 / 100 * display_h, 0) * ky
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif ev.key == pygame.K_TAB:
                    pygame.mixer.music.unload()
                    main_game()
            if ev.type == pygame.MOUSEBUTTONDOWN and mst == 1:
                mdx, mdy = ev.pos[0], ev.pos[1]
                if ev.button == 1 and 62 < mdx < 220 and 142 < mdy < 239:
                    mst = 1.1
            if ev.type == pygame.MOUSEBUTTONDOWN and mst == 1.1:
                mdx, mdy = ev.pos[0], ev.pos[1]
                for i in suits:
                    ix, iy = 295 + 132 * (suits.index(i) % 4), 208 + (suits.index(i) // 4) * 85
                    if ev.button == 1 and ix + 1 < mdx < ix + 109 and iy + 1 < mdy < iy + 62:
                        choose_sst = i
                if ev.button == 1 and 1349 < mdx < 1420 and 226 < mdy < 256:
                    suit = choose_sst.split('_icon.png')[0]
        if mst == 1:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/Base Menu/IMG_4305.JPG").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 17 * kx)
            for i in red_icons_weight:
                if red_icons_weight.index(i) == mst + 1:
                    pygame.draw.rect(SCREEN, (161, 3, 34), (qx, 0, i * kx, red_icons_height))
                    pygame.draw.rect(SCREEN, (255, 255, 255), (qx, 0, i * kx, 6))
                else:
                    pygame.draw.rect(SCREEN, (255, 0, 59), (qx, 0, i * kx, red_icons_height))
                text = font.render(red_icons_text[red_icons_weight.index(i)], True, (28, 6, 46))
                tx, ty = (qx + i * kx // (len(red_icons_text[red_icons_weight.index(i)]) + 2)) * kx, \
                         (red_icons_height // 2 - 8 * ky) * ky
                SCREEN.blit(text, (tx, ty))
                qx += i
                pygame.draw.rect(SCREEN, (28, 6, 46), (qx, 0, 2, red_icons_height))
                qx += 2

            for i in equipments_icon:
                text = font.render(i, True, pygame.Color('White'))
                tx, ty = ((red_icons_weight[0] // 2) + 15) * kx, \
                         (red_icons_height + 15 * ky + 0.17 * display_h * equipments_icon.index(i)) * ky
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 23 * ky, 0.02 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 27 * ky, 0.11 * display_w * kx, 3))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 35 * ky, 0.11 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 135 * ky, 0.11 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 35 * ky, 1 * kx, 100 * ky))
                pygame.draw.rect(SCREEN, pygame.Color('White'),
                                 (tx + 0.11 * display_w * kx, ty + 35 * ky, 1 * kx, 100 * ky))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx - 5, ty + 27 * ky, 1, 30))

            tx, ty = ((red_icons_weight[0] // 2) + 16) * kx, (red_icons_height + 51) * ky
            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss_icon.png").convert_alpha()
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss2.0_icon.png").convert_alpha()
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bgs_icon.png").convert_alpha()
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bts_icon.png").convert_alpha()
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/cs_icon.png").convert_alpha()
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/hs_icon.png").convert_alpha()
            elif suit == 'iss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/iss_icon.png").convert_alpha()
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/nms_icon.png").convert_alpha()
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/pbps_icon.png").convert_alpha()
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/scss_icon.png").convert_alpha()
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sm99s_icon.png").convert_alpha()
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sps_icon.png").convert_alpha()
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasm2s_icon.png").convert_alpha()
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasms_icon.png").convert_alpha()
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/us_icon.png").convert_alpha()
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/ws_icon.png").convert_alpha()
            suit_icon = pygame.transform.scale(suit_icon, (0.11 * display_w * kx - 3, 98))
            SCREEN.blit(suit_icon, (tx + 1, ty + 1))

            pygame.draw.rect(SCREEN, (29, 31, 36), (qx, 0, display_w - qx, display_h))
            pygame.draw.rect(SCREEN, (28, 6, 46), (qx - 8, 0, 3, red_icons_height))
            pygame.draw.rect(SCREEN, (255, 255, 255), (qx, red_icons_height, display_w - qx, 50))
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (qx, red_icons_height, 1, display_h - red_icons_height), 1)
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 27 * kx)
            text = font.render('EQUIPPED', True, (28, 6, 46))
            tx, ty = qx + 8, red_icons_height + 10
            SCREEN.blit(text, (tx, ty))
            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss_icon.png").convert_alpha()
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss2.0_icon.png").convert_alpha()
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bgs_icon.png").convert_alpha()
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bts_icon.png").convert_alpha()
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/cs_icon.png").convert_alpha()
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/hs_icon.png").convert_alpha()
            elif suit == 'iss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/iss_icon.png").convert_alpha()
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/nms_icon.png").convert_alpha()
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/pbps_icon.png").convert_alpha()
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/scss_icon.png").convert_alpha()
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sm99s_icon.png").convert_alpha()
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sps_icon.png").convert_alpha()
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasm2s_icon.png").convert_alpha()
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasms_icon.png").convert_alpha()
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/us_icon.png").convert_alpha()
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/ws_icon.png").convert_alpha()
            suit_icon = pygame.transform.scale(suit_icon, (110, 63))
            SCREEN.blit(suit_icon, (qx + 10, red_icons_height + 66))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceRegular.ttf", 18 * kx)
            if suit == 'adss':
                text = font.render('Advanced Suit', True, (255, 255, 255))
            elif suit == 'cs':
                text = font.render('Classic Suit', True, (255, 255, 255))
            elif suit == 'bts':
                text = font.render('Big Time', True, (255, 255, 255))
            elif suit == 'iss':
                text = font.render('Iron Spider', True, (255, 255, 255))
            elif suit == 'ws':
                text = font.render('Webbed Suit', True, (255, 255, 255))
            elif suit == 'us':
                text = font.render('Upgraded Suit', True, (255, 255, 255))
            elif suit == 'nms':
                text = font.render('Night Monkey', True, (255, 255, 255))
            elif suit == 'pbps':
                text = font.render('Peter B Parker', True, (255, 255, 255))
            elif suit == 'scss':
                text = font.render('Scarlet Spider', True, (255, 255, 255))
            elif suit == 'sm99s':
                text = font.render('Spider-Man 2099', True, (255, 255, 255))
            elif suit == 'sps':
                text = font.render('Spider-Punk', True, (255, 255, 255))
            elif suit == 'tasms':
                text = font.render('Amazing Suit', True, (255, 255, 255))
            elif suit == 'tasm2s':
                text = font.render('Amazing 2 Suit', True, (255, 255, 255))
            elif suit == 'hs':
                text = font.render('Hybrid Suit', True, (255, 255, 255))

            if suit == 'bgs':
                text = font.render('Black and Gold', True, (255, 255, 255))
                tx, ty = qx + 125, red_icons_height + 71
                SCREEN.blit(text, (tx, ty))
                text = font.render('Suit', True, (255, 255, 255))
                tx, ty = qx + 175, red_icons_height + 90
                SCREEN.blit(text, (tx, ty))
                pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                   [display_w, ty + 23])
            elif suit == 'adss2.0':
                text = font.render('Advanced Suit', True, (255, 255, 255))
                tx, ty = qx + 125, red_icons_height + 71
                SCREEN.blit(text, (tx, ty))
                text = font.render('2.0', True, (255, 255, 255))
                tx, ty = qx + 175, red_icons_height + 90
                SCREEN.blit(text, (tx, ty))
                pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                   [display_w, ty + 23])
            else:
                tx, ty = qx + 125, red_icons_height + 71
                SCREEN.blit(text, (tx, ty))
                pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                   [display_w, ty + 23])

            pygame.draw.ellipse(SCREEN, (255, 255, 255), (display_w // 3.5, 590, display_w // 2.3, 200), 3)
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (display_w // 3.5 + 65, 615, display_w // 2.3 - 130, 140), 1)
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (display_w // 3.5 + 228, 650, display_w // 2.3 - 460, 70), 1)
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + display_w // 4.6 - 5, 591],
                               [display_w // 3.5 + 228 + (display_w // 2.3 - 460) // 2, 647])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + 230 + (display_w // 2.3 - 460) // 2, 721],
                               [display_w // 3.5 + display_w // 4.6 + 4, 787])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + display_w // 9.2 - 22, 610],
                               [display_w // 3.5 + 228 + (display_w // 2.3 - 460) // 4 - 13, 657])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + 390, 707], [display_w // 3.5 + 530, 764])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + 1, 683], [display_w // 3.5 + 228, 683])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + 407, 683],
                               [display_w // 3.5 + display_w // 2.3, 683])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + display_w // 9.2 - 30, 769],
                               [display_w // 3.5 + 228 + (display_w // 2.3 - 460) // 4 - 13, 711])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [display_w // 3.5 + 500, 610], [display_w // 3.5 + 384, 660])

            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_adss.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_adss2.0.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_bgs.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_bts.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_cs.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_hs.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'iss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_iss.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_nms.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_pbps.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_scss.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_sm99s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_sps.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_tasm2s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (505, 395))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 50, 360))
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_tasms.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_us.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_ws.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (545, 370))
                SCREEN.blit(suit_icon, (display_w // 3.5 + 40, 410))
            qx, qy = 0, 0

        elif mst == 1.1:
            intro_image = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                            "/Pictures/Base Menu/IMG_4305.JPG").convert_alpha()
            intro_image = pygame.transform.scale(intro_image, (display_w, display_h))
            SCREEN.blit(intro_image, (0, 0))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 17 * kx)
            for i in red_icons_weight:
                if red_icons_weight.index(i) == mst + 0.9:
                    pygame.draw.rect(SCREEN, (161, 3, 34), (qx, 0, i * kx, red_icons_height))
                    pygame.draw.rect(SCREEN, (255, 255, 255), (qx, 0, i * kx, 6))
                else:
                    pygame.draw.rect(SCREEN, (255, 0, 59), (qx, 0, i * kx, red_icons_height))
                text = font.render(red_icons_text[red_icons_weight.index(i)], True, (28, 6, 46))
                tx, ty = (qx + i * kx // (len(red_icons_text[red_icons_weight.index(i)]) + 2)) * kx, \
                         (red_icons_height // 2 - 8 * ky) * ky
                SCREEN.blit(text, (tx, ty))
                qx += i
                pygame.draw.rect(SCREEN, (28, 6, 46), (qx, 0, 2, red_icons_height))
                qx += 2

            for i in equipments_icon:
                text = font.render(i, True, pygame.Color('White'))
                tx, ty = ((red_icons_weight[0] // 2) + 15) * kx, \
                         (red_icons_height + 15 * ky + 0.17 * display_h * equipments_icon.index(i)) * ky
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 23 * ky, 0.02 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 27 * ky, 0.11 * display_w * kx, 3))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 35 * ky, 0.11 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 135 * ky, 0.11 * display_w * kx, 1))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx, ty + 35 * ky, 1 * kx, 100 * ky))
                pygame.draw.rect(SCREEN, pygame.Color('White'),
                                 (tx + 0.11 * display_w * kx, ty + 35 * ky, 1 * kx, 100 * ky))
                pygame.draw.rect(SCREEN, pygame.Color('White'), (tx - 5, ty + 27 * ky, 1, 30))

            tx, ty = ((red_icons_weight[0] // 2) + 16) * kx, (red_icons_height + 51) * ky
            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss_icon.png").convert_alpha()
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss2.0_icon.png").convert_alpha()
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bgs_icon.png").convert_alpha()
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bts_icon.png").convert_alpha()
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/cs_icon.png").convert_alpha()
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/hs_icon.png").convert_alpha()
            elif suit == 'is':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/is_icon.png").convert_alpha()
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/nms_icon.png").convert_alpha()
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/pbps_icon.png").convert_alpha()
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/scss_icon.png").convert_alpha()
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sm99s_icon.png").convert_alpha()
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sps_icon.png").convert_alpha()
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasm2s_icon.png").convert_alpha()
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasms_icon.png").convert_alpha()
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/us_icon.png").convert_alpha()
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/ws_icon.png").convert_alpha()
            suit_icon = pygame.transform.scale(suit_icon, (0.11 * display_w * kx - 3, 98))
            SCREEN.blit(suit_icon, (tx + 1, ty + 1))
            pygame.draw.aalines(SCREEN, (255, 255, 255), False, [[tx + 0.11 * display_w * kx, red_icons_height + 97],
                                                                 [270, red_icons_height + 97]])
            pygame.draw.rect(SCREEN, (255, 255, 255), (243, red_icons_height + 95, 6, 6))
            pygame.draw.lines(SCREEN, (255, 255, 255), False, [[290, red_icons_height + 97],
                                                               [370, red_icons_height + 97]], 2)
            pygame.draw.lines(SCREEN, (255, 255, 255), False, [[380, red_icons_height + 97],
                                                               [810, red_icons_height + 97]])
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 22 * kx)
            text = font.render('SUIT', True, (255, 255, 255))
            SCREEN.blit(text, (290, red_icons_height + 65))
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mdx, mdy = ev.pos[0], ev.pos[1]
                    if ev.button == 1 and tx + 1 < mdx < tx + 0.11 * display_w * kx - 3 and ty + 1 < mdy < ty + 98:
                        mst = 1

            pygame.draw.rect(SCREEN, (29, 31, 36), (qx, 0, display_w - qx, display_h))
            pygame.draw.rect(SCREEN, (28, 6, 46), (qx - 8, 0, 3, red_icons_height))
            pygame.draw.rect(SCREEN, (255, 255, 255), (qx, red_icons_height, display_w - qx, 50))
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (qx, red_icons_height, 1, display_h - red_icons_height), 1)
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 27 * kx)
            text = font.render('EQUIPPED', True, (28, 6, 46))
            tx, ty = qx + 8, red_icons_height + 10
            SCREEN.blit(text, (tx, ty))
            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss_icon.png").convert_alpha()
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/adss2.0_icon.png").convert_alpha()
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bgs_icon.png").convert_alpha()
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/bts_icon.png").convert_alpha()
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/cs_icon.png").convert_alpha()
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/hs_icon.png").convert_alpha()
            elif suit == 'is':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/is_icon.png").convert_alpha()
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/nms_icon.png").convert_alpha()
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/pbps_icon.png").convert_alpha()
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/scss_icon.png").convert_alpha()
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sm99s_icon.png").convert_alpha()
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/sps_icon.png").convert_alpha()
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasm2s_icon.png").convert_alpha()
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/tasms_icon.png").convert_alpha()
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/us_icon.png").convert_alpha()
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/ws_icon.png").convert_alpha()
            suit_icon = pygame.transform.scale(suit_icon, (110, 63))
            SCREEN.blit(suit_icon, (qx + 10, red_icons_height + 66))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceRegular.ttf", 18 * kx)
            if choose_sst == '':
                if suit == 'adss':
                    text = font.render('Advanced Suit', True, (255, 255, 255))
                elif suit == 'cs':
                    text = font.render('Classic Suit', True, (255, 255, 255))
                elif suit == 'bts':
                    text = font.render('Big Time', True, (255, 255, 255))
                elif suit == 'iss':
                    text = font.render('Iron Spider', True, (255, 255, 255))
                elif suit == 'ws':
                    text = font.render('Webbed Suit', True, (255, 255, 255))
                elif suit == 'us':
                    text = font.render('Upgraded Suit', True, (255, 255, 255))
                elif suit == 'nms':
                    text = font.render('Night Monkey', True, (255, 255, 255))
                elif suit == 'pbps':
                    text = font.render('Peter B Parker', True, (255, 255, 255))
                elif suit == 'scss':
                    text = font.render('Scarlet Spider', True, (255, 255, 255))
                elif suit == 'sm99s':
                    text = font.render('Spider-Man 2099', True, (255, 255, 255))
                elif suit == 'sps':
                    text = font.render('Spider-Punk', True, (255, 255, 255))
                elif suit == 'tasms':
                    text = font.render('Amazing Suit', True, (255, 255, 255))
                elif suit == 'tasm2s':
                    text = font.render('Amazing 2 Suit', True, (255, 255, 255))
                elif suit == 'hs':
                    text = font.render('Hybrid Suit', True, (255, 255, 255))
                if suit == 'bgs':
                    text = font.render('Black and Gold', True, (255, 255, 255))
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    text = font.render('Suit', True, (255, 255, 255))
                    tx, ty = qx + 175, red_icons_height + 90
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23])
                elif suit == 'adss2.0':
                    text = font.render('Advanced Suit', True, (255, 255, 255))
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    text = font.render('2.0', True, (255, 255, 255))
                    tx, ty = qx + 175, red_icons_height + 90
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23])
                else:
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23])

            pygame.draw.rect(SCREEN, (255, 255, 255), (270, 145, 560, 655), 1)
            pygame.draw.aalines(SCREEN, (255, 255, 255), False, [[817, 136], [838, 136], [838, 155]])
            pygame.draw.lines(SCREEN, (255, 255, 255), False, [[838, 159], [838, 179]], 3)
            pygame.draw.aalines(SCREEN, (255, 255, 255), False, [[817, 809], [838, 809], [838, 790]])
            pygame.draw.lines(SCREEN, (255, 255, 255), False, [[838, 786], [838, 766]], 3)

            for i in suits:
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/" + i).convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (110, 63))
                ix, iy = 295 + 132 * (suits.index(i) % 4), 208 + (suits.index(i) // 4) * 85
                SCREEN.blit(suit_icon, (ix, iy))

            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif ev.key == pygame.K_TAB:
                        pygame.mixer.music.unload()
                        main_game()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mdx, mdy = ev.pos[0], ev.pos[1]
                    for i in suits:
                        ix, iy = 295 + 132 * (suits.index(i) % 4), 208 + (suits.index(i) // 4) * 85
                        if ev.button == 1 and ix + 1 < mdx < ix + 109 and iy + 1 < mdy < iy + 62:
                            choose_sst = i

            if choose_sst != '':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suit's Icons/" + choose_sst).convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (110, 63))
                SCREEN.blit(suit_icon, (qx + 10, red_icons_height + 66))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceRegular.ttf", 18 * kx)
                if choose_sst == 'cs_icon.png':
                    text = font.render('Classic Suit', True, (255, 255, 255))
                elif choose_sst == 'adss_icon.png':
                    text = font.render('Advansed Suit', True, (255, 255, 255))
                elif choose_sst == 'bts_icon.png':
                    text = font.render('Big Time Suit', True, (255, 255, 255))
                elif choose_sst == 'pbps_icon.png':
                    text = font.render('Peter B Parker', True, (255, 255, 255))
                elif choose_sst == 'sm99s_icon.png':
                    text = font.render('Spider-Man 2099', True, (255, 255, 255))
                elif choose_sst == 'sps_icon.png':
                    text = font.render('Spider-Punk', True, (255, 255, 255))
                elif choose_sst == 'scss_icon.png':
                    text = font.render('Scarlet Spider', True, (255, 255, 255))
                elif choose_sst == 'iss_icon.png':
                    text = font.render('Iron Spider', True, (255, 255, 255))
                elif choose_sst == 'ws_icon.png':
                    text = font.render('Webbed Suit', True, (255, 255, 255))
                elif choose_sst == 'us_icon.png':
                    text = font.render('Upgraded Suit', True, (255, 255, 255))
                elif choose_sst == 'nms_icon.png':
                    text = font.render('Night Monkey', True, (255, 255, 255))
                elif choose_sst == 'tasms_icon.png':
                    text = font.render('Amazing Suit', True, (255, 255, 255))
                elif choose_sst == 'tasm2s_icon.png':
                    text = font.render('Amazing 2 Suit', True, (255, 255, 255))
                elif choose_sst == 'hs_icon.png':
                    text = font.render('Hybrid Suit', True, (255, 255, 255))

                if choose_sst == 'bgs_icon.png':
                    text = font.render('Black and Gold', True, (255, 255, 255))
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    text = font.render('Suit', True, (255, 255, 255))
                    tx, ty = qx + 175, red_icons_height + 90
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23])
                elif choose_sst == 'adss2.0_icon.png':
                    text = font.render('Advanced Suit', True, (255, 255, 255))
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    text = font.render('2.0', True, (255, 255, 255))
                    tx, ty = qx + 175, red_icons_height + 90
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23])
                else:
                    tx, ty = qx + 125, red_icons_height + 71
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.aaline(SCREEN, (255, 255, 255), [qx + 125, ty + 23],
                                       [display_w, ty + 23] )
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 22 * kx)
            if suit not in choose_sst:
                text = font.render('USE', True, (255, 255, 255))
                tx, ty = qx + 175, red_icons_height + 140
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, (255, 255, 255), (tx - 10, ty - 5, 63, 32), 2)
                pygame.draw.aaline(SCREEN, (255, 255, 255), [tx - 175, ty + 13],
                                   [tx - 11, ty + 13])
                pygame.draw.aaline(SCREEN, (255, 255, 255), [tx + 53, ty + 13],
                                   [display_w, ty + 13])
            else:
                text = font.render('USED', True, (255, 255, 255))
                tx, ty = qx + 175, red_icons_height + 140
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, (255, 255, 255), (tx - 10, ty - 5, 73, 32), 2)
                pygame.draw.aaline(SCREEN, (255, 255, 255), [tx - 175, ty + 13],
                                   [tx - 11, ty + 13])
                pygame.draw.aaline(SCREEN, (255, 255, 255), [tx + 64, ty + 13],
                                   [display_w, ty + 13])

            pygame.draw.ellipse(SCREEN, (255, 255, 255), (865, 730, 290, 85), 2)
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (903, 740, 220, 55), 1)
            pygame.draw.ellipse(SCREEN, (255, 255, 255), (963, 751, 90, 30), 1)
            pygame.draw.aaline(SCREEN, (255, 255, 255), [1012, 731], [1010, 750])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [919, 741], [981, 753])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [866, 765], [962, 765])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [895, 796], [976, 776])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [1008, 780], [1006, 810])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [1035, 778], [1120, 800])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [1053, 765], [1150, 765])
            pygame.draw.aaline(SCREEN, (255, 255, 255), [1035, 754], [1105, 740])
            if suit == 'adss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_adss_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (250, 610))
                SCREEN.blit(suit_icon, (880, 210))
            elif suit == 'adss2.0':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_adss2.0_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (270, 620))
                SCREEN.blit(suit_icon, (880, 200))
            elif suit == 'bgs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_bgs_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'bts':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_bts_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (250, 610))
                SCREEN.blit(suit_icon, (880, 210))
            elif suit == 'cs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_cs_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'hs':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_hs_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'iss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_iss_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'nms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_nms_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'pbps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_pbps_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (270, 610))
                SCREEN.blit(suit_icon, (870, 210))
            elif suit == 'scss':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_scss_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (250, 610))
                SCREEN.blit(suit_icon, (880, 195))
            elif suit == 'sm99s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_sm99s_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (280, 610))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'sps':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_sps_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (250, 610))
                SCREEN.blit(suit_icon, (880, 210))
            elif suit == 'tasm2s':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_tasm2s_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (240, 600))
                SCREEN.blit(suit_icon, (880, 210))
            elif suit == 'tasms':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_tasms_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'us':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_us_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))
            elif suit == 'ws':
                suit_icon = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                              "/Pictures/Base Menu/Suits for Base Menu/menu_ws_s.png").convert_alpha()
                suit_icon = pygame.transform.scale(suit_icon, (310, 620))
                SCREEN.blit(suit_icon, (860, 210))

            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mdx, mdy = ev.pos[0], ev.pos[1]
                    for i in suits:
                        ix, iy = 295 + 132 * (suits.index(i) % 4), 208 + (suits.index(i) // 4) * 85
                        if ev.button == 1 and ix + 1 < mdx < ix + 109 and iy + 1 < mdy < iy + 62:
                            choose_sst = i
                    if ev.button == 1 and 1349 < mdx < 1420 and 226 < mdy < 256:
                        suit = choose_sst.split('_icon.png')[0]
                if ev.type == pygame.QUIT:
                    quit()
            qx, qy = 0, 0
        pygame.display.update()
        pygame.time.wait(40)


def main_game():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    WIDTH, HEIGHT = 1470, 900
    pi = 3.14
    diff, musst, suit, cut_scene = '', -1, 'cs', 0
    SCREEN = pygame.display.set_mode((1470, 920))
    pygame.display.set_caption("Spider-Man")
    infoObject = pygame.display.Info()
    display_w, display_h = WIDTH, HEIGHT
    kx, ky = 1, 1
    st = 0
    sp_ticks = 0
    bg = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                           "Textures/fhomewthspandpavmnt.jpg").convert()
    bg = pygame.transform.scale(bg, (1414, 2000))
    road = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                             "Textures/дорога.jpeg").convert()
    road = pygame.transform.scale(road, (2011, 354))
    sky = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                            "Textures/skyy.png").convert()
    sky = pygame.transform.scale(sky, (2011, 1000))
    ground = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                               "Textures/groundd.jpg").convert()
    ground = pygame.transform.scale(ground, (1000, 100))
    sdvigx = 0
    sdvigy = -330
    podst = 0
    revst = 0
    crawl_st = 0
    tiles = math.ceil(display_w / bg.get_width()) + 1
    i = 0
    running = True

    SMx, SMy = display_w // 2 - 150 + 15, display_h // 2 - 200 + 7
    Thx, Thy = display_w // 2 + 150 + 15, display_h // 2 - 200 + 7
    type_of_landing = -1
    SMRt = 90
    cc = SMx
    wbx, wby = SMx + 90, SMy + 160
    lh = 0
    web_ticks = 0
    amplitude = 10
    frequency = 0.05
    angle = 45
    xx = 1090
    inertia = 0
    go_back_in_a_sec = 0
    musticks = 0
    thug_st = 0
    th_st = 0
    sp_ticks = 0
    thug_ticks = 0
    dlt_sdvigx = 0
    dlt_sdvigy = 0
    th_sdvigx = 10 * 10
    th_sdvigy = 0
    thug_type_of_hit = 0
    thug_type_of_react = 0
    th_revst = 0
    th_delay = 0
    hit = 0
    fight_ready = 0
    fight_ready_pose = 0
    l_hit, r_hit = 0, 0
    type_of_evasion = 0
    health = 100
    harm = 20
    th_health = 50
    p_of_hit = 20
    evasion = 0
    crawl_st, dcrawl_st = 0, 0
    spider_type_of_react = 0
    type_of_hit = 0

    health = 100
    pygame.mixer.pre_init(44100, -16, 1, 512)
    mixst = 0
    thwip = pygame.mixer.Sound(
        "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/Thwip_sound.wav")
    thwip1 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                "Thwip_sound1.wav")
    thwip2 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                "Thwip_sound2.wav")
    thwip3 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                "Thwip_sound3.wav")

    swing = pygame.mixer.Sound(
        "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/Swing_sound.wav")

    run = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/run1.wav")

    jump = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/Jump.wav")

    grounds = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                 "Ground_sound.wav")

    sp_death = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                  "Spider_death.wav")

    th_death = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                                  "th_hitted.wav")

    hit_mix = random.choice([0, 1, 2, 3])
    hitt = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/hit.wav")
    hit1 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                              "hit1.wav")
    hit2 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                              "hit2.wav")
    hit3 = pygame.mixer.Sound("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/"
                              "hit3.wav")

    city_mus = random.choice([0, 1, 2, 3])
    if city_mus == 0:
        pygame.mixer.music.load(
            "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound.mp3")
        vol = 0.7
    elif city_mus == 1:
        pygame.mixer.music.load(
            "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound1.mp3")
        vol = 0.7
    elif city_mus == 2:
        pygame.mixer.music.load(
            "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound2.mp3")
        vol = 0.5
    elif city_mus == 3:
        pygame.mixer.music.load(
            "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound3.mp3")
        vol = 0.7
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1)
    musst = 0  # Звуки города
    while running:
        ticks = pygame.time.get_ticks()

        if musst == 2 and 2000 <= ticks - musticks <= 2500:
            city_mus = random.choice([0, 1, 2, 3])
            if city_mus == 0:
                pygame.mixer.music.load(
                    "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound.mp3")
                vol = 0.7
            elif city_mus == 1:
                pygame.mixer.music.load(
                    "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound1.mp3")
                vol = 0.7
            elif city_mus == 2:
                pygame.mixer.music.load(
                    "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound2.mp3")
                vol = 0.5
            elif city_mus == 3:
                pygame.mixer.music.load(
                    "/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Sounds/city_sound3.mp3")
                vol = 0.7
            pygame.mixer.music.set_volume(vol)
            pygame.mixer.music.play(-1)
            musst = 0  # Звуки города

        if st == 0 and revst == 0 and (sdvigy <= -330 or sdvigy >= 1600) and (0 <= ticks - sp_ticks <= 1500) \
                and ((not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE]
                      and not pygame.key.get_pressed()[pygame.K_a]) or
                     (pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_d])):
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if mixst == 1:
                mixst = 0
                run.stop()
            if inertia != 0:
                inertia = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 315))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 125))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 300))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 3))


        elif (st == 0 and revst == 0 and (sdvigy <= -330 or sdvigy >= 1600)
              and (1500 <= ticks - sp_ticks <= 3000)
              and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE]
              and not pygame.key.get_pressed()[pygame.K_a]):
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 22.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 315))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 125))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 300))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 3))

        if st == 0 and revst == 0 and (ticks - sp_ticks > 3000) \
                and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
                and not pygame.key.get_pressed()[pygame.K_a]:
            sp_ticks = ticks

        # Бег
        if (st == 0 and revst == 0 and (sdvigy <= -330 or
                                        (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
                and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
                and (0 <= ticks - sp_ticks <= 80 or sp_ticks == 0)):
            if mixst == 0:
                mixst = 1
                run.play(-1)
            if inertia == 0:
                inertia = 1
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 7.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (115, 300))
                SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (107, 285))
                SCREEN.blit(Spider_Man, (SMx - 5, SMy + 15))
            if sp_ticks == 0:
                sp_ticks = ticks - 80


        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 80 <= ticks - sp_ticks <= 160):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 10.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (170, 300))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (162, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 160 <= ticks - sp_ticks <= 240):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 11.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (210, 300))
                SCREEN.blit(Spider_Man, (SMx - 60, SMy + 123))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (202, 285))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 240 <= ticks - sp_ticks <= 320):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 14.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (203, 300))
                SCREEN.blit(Spider_Man, (SMx - 60, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (195, 285))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 320 <= ticks - sp_ticks <= 400):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 15.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (139, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 400 <= ticks - sp_ticks <= 480):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 18.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (114, 300))
                SCREEN.blit(Spider_Man, (SMx + 10, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (106, 285))
                SCREEN.blit(Spider_Man, (SMx + 10, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))





        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 480 <= ticks - sp_ticks <= 560):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 19.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (160, 300))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (152, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 560 <= ticks - sp_ticks <= 640):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 28.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (215, 300))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 123))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (207, 285))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 640 <= ticks - sp_ticks <= 720):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 29.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (204, 300))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (196, 285))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 0 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]
              and 720 <= ticks - sp_ticks <= 800):
            sdvigx -= 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 32.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (144, 300))
                SCREEN.blit(Spider_Man, (SMx - 30, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (136, 285))
                SCREEN.blit(Spider_Man, (SMx - 30, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))


        elif st == 0 and revst == 0 and (sdvigy <= -330 or sdvigy >= 1600) and pygame.key.get_pressed()[pygame.K_d] \
                and (ticks - sp_ticks > 800):
            sp_ticks = ticks

        if revst == 0 and pygame.key.get_pressed()[pygame.K_a] and not 0 <= sdvigy <= 1700:
            revst = 1
            if st == 0 and sdvigy >= 1600:
                sp_ticks = 0
            else:
                sp_ticks = ticks
        elif revst == 1 and pygame.key.get_pressed()[pygame.K_d] and not 0 <= sdvigy <= 1700:
            revst = 0
            if st == 0 and sdvigy >= 1600:
                sp_ticks = 0
            else:
                sp_ticks = ticks

        if st == 0 and revst == 1 and (sdvigy <= -330 or sdvigy >= 1600) and (0 <= ticks - sp_ticks <= 1500) \
                and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
                and not pygame.key.get_pressed()[pygame.K_a]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if mixst == 1:
                mixst = 0
                run.stop()
            if inertia != 0:
                inertia = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 21.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 315))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 125))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 300))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 3))


        elif (st == 0 and revst == 1 and (sdvigy <= -330 or sdvigy >= 1600)
              and (1500 <= ticks - sp_ticks <= 3000)
              and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE]
              and not pygame.key.get_pressed()[pygame.K_a]):
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 24.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 315))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 125))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (75, 300))
                SCREEN.blit(Spider_Man, (SMx + 27, SMy + 3))

        if st == 0 and revst == 1 and (ticks - sp_ticks > 3000) \
                and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
                and not pygame.key.get_pressed()[pygame.K_a]:
            sp_ticks = ticks

        if (st == 0 and revst == 1 and (sdvigy <= -330 or
                                        (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 550)))
                and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
                and (0 <= ticks - sp_ticks <= 80 or sp_ticks == 0)):
            sdvigx += 9
            if mixst == 0:
                mixst = 1
                run.play(-1)
            if inertia == 0:
                inertia = 1
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 8.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (115, 300))
                SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (107, 285))
                SCREEN.blit(Spider_Man, (SMx - 5, SMy + 15))
            if sp_ticks == 0:
                sp_ticks = ticks - 80


        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 80 <= ticks - sp_ticks <= 160):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 9.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (170, 300))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (162, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 160 <= ticks - sp_ticks <= 240):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 12.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (210, 300))
                SCREEN.blit(Spider_Man, (SMx - 60, SMy + 123))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (202, 285))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 240 <= ticks - sp_ticks <= 320):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 13.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (203, 300))
                SCREEN.blit(Spider_Man, (SMx - 60, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (195, 285))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 320 <= ticks - sp_ticks <= 400):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 16.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
                SCREEN.blit(Spider_Man, (SMx - 40, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (139, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and (400 <= ticks - sp_ticks <= 480)):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 17.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (114, 300))
                SCREEN.blit(Spider_Man, (SMx + 10, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (106, 285))
                SCREEN.blit(Spider_Man, (SMx + 10, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 480 <= ticks - sp_ticks <= 560):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 20.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (160, 300))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (152, 285))
                SCREEN.blit(Spider_Man, (SMx - 20, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 560 <= ticks - sp_ticks <= 640):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 27.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (215, 300))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 123))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (207, 285))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 640 <= ticks - sp_ticks <= 720):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 30.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (204, 300))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 130))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (196, 285))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))



        elif (st == 0 and revst == 1 and (sdvigy <= -330 or
                                          (sdvigy >= 1600 and (-1440 <= sdvigx <= -800 or -545 <= sdvigx <= 570)))
              and pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]
              and 720 <= ticks - sp_ticks <= 800):
            sdvigx += 9
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 31.png').convert_alpha()
            if sdvigy <= -330:
                Spider_Man = pygame.transform.scale(Spider_Man, (144, 300))
                SCREEN.blit(Spider_Man, (SMx - 30, SMy + 140))
            elif sdvigy >= 1600:
                Spider_Man = pygame.transform.scale(Spider_Man, (136, 285))
                SCREEN.blit(Spider_Man, (SMx - 30, SMy + 18))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))


        elif st == 0 and revst == 1 and (sdvigy <= -330 or sdvigy >= 1600) and pygame.key.get_pressed()[pygame.K_a] \
                and (ticks - sp_ticks > 800):
            sp_ticks = ticks

        if (st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_w] and
                (-710 <= sdvigx <= -630 or 700 <= sdvigx <= 810)
                and pygame.key.get_pressed()[pygame.K_SPACE]
                and st != 3 and st != 1):
            st = 3

        # Запрыгивание на стену
        if st == 3 and (0 <= ticks - sp_ticks <= 70):
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 33.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 3 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 36.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 215))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 225))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 3 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 37.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (185, 265))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 3 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 70
            Spider_Man = pygame.image.load('Тема 40.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (170, 290))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 3 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 60
            Spider_Man = pygame.image.load('Тема 41.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 325))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 3 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 100
            Spider_Man = pygame.image.load('Тема 346.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (165, 320))
            SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if sdvigx != -680:
                sdvigx = -680
            st = 4

        else:
            if st == 3:
                sp_ticks = ticks

        # Ползанье по стене вверх
        if st == 4 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 309.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 320))
            SCREEN.blit(Spider_Man, (SMx + 22, SMy + 100))
        elif st == 4 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 310.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (135, 300))
            SCREEN.blit(Spider_Man, (SMx + 19, SMy + 125))
        elif st == 4 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 313.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (125, 270))
            SCREEN.blit(Spider_Man, (SMx + 28, SMy + 135))
        elif st == 4 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 314.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (125, 265))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 137))
        elif st == 4 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 317.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (121, 265))
            SCREEN.blit(Spider_Man, (SMx + 32, SMy + 120))
        elif st == 4 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 318.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (125, 265))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 106))
        elif st == 4 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 321.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 95))
        elif st == 4 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 324.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
        elif st == 4 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 326.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
            SCREEN.blit(Spider_Man, (SMx + 23, SMy + 115))
        elif st == 4 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 327.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 280))
            SCREEN.blit(Spider_Man, (SMx + 24, SMy + 130))
        elif st == 4 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 329.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
            SCREEN.blit(Spider_Man, (SMx + 18, SMy + 125))
        elif st == 4 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 330.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (135, 290))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 133))
        elif st == 4 and crawl_st == 12:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 333.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 285))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 135))
        elif st == 4 and crawl_st == 13:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 334.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 310))
            SCREEN.blit(Spider_Man, (SMx + 15, SMy + 112))
        elif st == 4 and crawl_st == 14:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 336.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (135, 300))
            SCREEN.blit(Spider_Man, (SMx + 15, SMy + 101))
        elif st == 4 and crawl_st == 15:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 337.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
            SCREEN.blit(Spider_Man, (SMx + 15, SMy + 90))
        elif st == 4 and crawl_st == 16:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 340.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 310))
            SCREEN.blit(Spider_Man, (SMx + 14, SMy + 83))
        elif st == 4 and crawl_st == 17:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 341.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
            SCREEN.blit(Spider_Man, (SMx + 28, SMy + 83))

        # Ползанье по стене вниз
        if st == -4 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 308.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 300))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 100))
        elif st == -4 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 311.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (135, 280))
            SCREEN.blit(Spider_Man, (SMx + 19, SMy + 105))
        elif st == -4 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 312.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (125, 270))
            SCREEN.blit(Spider_Man, (SMx + 28, SMy + 110))
        elif st == -4 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 315.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 277))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
        elif st == -4 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 316.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx + 28, SMy + 110))
        elif st == -4 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 319.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx + 27, SMy + 120))
        elif st == -4 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 320.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 115))
        elif st == -4 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 322.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (85, 260))
            SCREEN.blit(Spider_Man, (SMx + 55, SMy + 115))
        elif st == -4 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 323.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (90, 250))
            SCREEN.blit(Spider_Man, (SMx + 50, SMy + 120))
        elif st == -4 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 325.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 280))
            SCREEN.blit(Spider_Man, (SMx + 29, SMy + 120))
        elif st == -4 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 328.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (90, 250))
            SCREEN.blit(Spider_Man, (SMx + 50, SMy + 120))
        elif st == -4 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 331.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
        elif st == -4 and crawl_st == 12:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 332.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
        elif st == -4 and crawl_st == 13:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 335.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 275))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
        elif st == -4 and crawl_st == 14:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 345.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (95, 270))
            SCREEN.blit(Spider_Man, (SMx + 45, SMy + 120))
        elif st == -4 and crawl_st == 15:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 338.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (135, 280))
            SCREEN.blit(Spider_Man, (SMx + 25, SMy + 110))
        elif st == -4 and crawl_st == 16:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 339.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 300))
            SCREEN.blit(Spider_Man, (SMx + 14, SMy + 105))
        elif st == -4 and crawl_st == 17:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 342.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 315))
            SCREEN.blit(Spider_Man, (SMx + 28, SMy + 95))

        # Запрыгивание на крышу
        if st == 5 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 348.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (152, 340))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy - 20))
        elif st == 5 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 349.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (160, 370))
            SCREEN.blit(Spider_Man, (SMx - 13, SMy - 20))
        elif st == 5 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 352.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
            SCREEN.blit(Spider_Man, (SMx + 9, SMy - 20))
        elif st == 5 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 353.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (137, 310))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
        elif st == 5 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 356.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 333))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
        elif st == 5 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 357.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 333))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy - 3))
        elif st == 5 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 360.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 35))
        elif st == 5 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 361.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 0))
        elif st == 5 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 364.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (180, 385))
            SCREEN.blit(Spider_Man, (SMx + 10, SMy + 10))
        elif st == 5 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 365.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 320))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 52))
        elif st == 5 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 368.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 320))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 72))
        elif st == 5 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 369.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (133, 177))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 126))
            st = 0

        # Спрыгивание со стены
        if st == -5 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 372.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (152, 320))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 100))
        elif st == -5 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 373.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
            SCREEN.blit(Spider_Man, (SMx + 2, SMy + 100))
        elif st == -5 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 376.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (170, 350))
            SCREEN.blit(Spider_Man, (SMx - 17, SMy + 97))
        elif st == -5 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 377.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (230, 445))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy + 70))
        elif st == -5 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 380.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (255, 470))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 70))
        elif st == -5 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 406.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (235, 215))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 70))
        elif st == -5 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 383.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (210, 435))
            SCREEN.blit(Spider_Man, (SMx - 17, SMy - 27))
        elif st == -5 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 384.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (190, 410))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy + 0))
        elif st == -5 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 405.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (205, 245))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 60))
        elif st == -5 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 386.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (200, 430))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 22))
        elif st == -5 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 389.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (240, 510))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 0))
        elif st == -5 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 400.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (250, 200))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 160))
        elif st == -5 and crawl_st == 12:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 391.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (250, 495))
            SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
        elif st == -5 and crawl_st == 13:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 392.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (210, 460))
            SCREEN.blit(Spider_Man, (SMx + 10, SMy + 65))
        elif st == -5 and crawl_st == 14:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 402.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (200, 205))
            SCREEN.blit(Spider_Man, (SMx + 10, SMy + 235))
        elif st == -5 and crawl_st == 15:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 394.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (180, 390))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 125))
        elif st == -5 and crawl_st == 16:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 397.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (170, 380))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 115))
        elif st == -5 and crawl_st == 17:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 398.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (160, 340))
            SCREEN.blit(Spider_Man, (SMx + 0, SMy + 155))

        # Триггер
        if (st == 0 and pygame.key.get_pressed()[pygame.K_SPACE] and st != 1 and not pygame.key.get_pressed()[
            pygame.K_w]
                and st != 1 and sdvigy == -330):
            st = 1
            if mixst == 1:
                mixst = 0
                run.stop()
            sp_ticks = ticks

        if st == 1 and revst == 0 and (0 <= ticks - sp_ticks <= 70) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 33.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 36.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 215))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 225))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 37.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (185, 265))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 85
            if inertia != 0:
                sdvigx -= 13
            Spider_Man = pygame.image.load('Тема 40.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (182, 305))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 65
            if inertia != 0:
                sdvigx -= 13
            Spider_Man = pygame.image.load('Тема 41.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (155, 360))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 55
            if inertia != 0:
                sdvigx -= 13
            Spider_Man = pygame.image.load('Тема 44.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (155, 290))
            SCREEN.blit(Spider_Man, (SMx - 35, SMy + 150))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (510 <= ticks - sp_ticks <= 700) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if inertia != 0:
                sdvigx -= 1
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 45.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (170, 220))
            SCREEN.blit(Spider_Man, (SMx - 40, SMy + 150))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))






        elif st == 1 and revst == 0 and (700 <= ticks - sp_ticks <= 830) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy -= 115
            if inertia != 0:
                sdvigx -= 13
            Spider_Man = pygame.image.load('Тема 48.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (198, 300))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))





        elif st == 1 and revst == 0 and (sdvigy > -330 or (830 <= ticks - sp_ticks <= 900)) and not \
                pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy -= 70
            if inertia != 0:
                sdvigx -= 13
            if mixst == 0:
                jump.play()
                mixst = 1
            Spider_Man = pygame.image.load('Тема 49.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (230, 280))
            SCREEN.blit(Spider_Man, (SMx - 30, SMy + 160))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (900 <= ticks - sp_ticks <= 970) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            if sdvigy != -330:
                sdvigy = -330
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            mixst = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 52.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (205, 230))
            SCREEN.blit(Spider_Man, (SMx - 40, SMy + 210))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (970 <= ticks - sp_ticks <= 1040) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            if sdvigy != -330:
                sdvigy = -330
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            mixst = 0
            Spider_Man = pygame.image.load('Тема 53.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (173, 200))
            SCREEN.blit(Spider_Man, (SMx - 32, SMy + 240))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (1040 <= ticks - sp_ticks <= 1110) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 56.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 230))
            SCREEN.blit(Spider_Man, (SMx - 30, SMy + 210))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (1110 <= ticks - sp_ticks <= 1180) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 57.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 270))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 170))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 0 and (1180 <= ticks - sp_ticks <= 1350) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 60.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (129, 300))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))


        elif st == 1 and revst == 0 and (ticks - sp_ticks > 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            sp_ticks = ticks
            st = 0

        if st == 1 and revst == 1 and (0 <= ticks - sp_ticks <= 70) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 34.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 35.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 215))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 225))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 38.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (185, 265))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 85
            if inertia != 0:
                sdvigx += 13
            Spider_Man = pygame.image.load('Тема 39.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (182, 305))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 65
            if inertia != 0:
                sdvigx += 13
            Spider_Man = pygame.image.load('Тема 42.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (155, 360))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy += 55
            if inertia != 0:
                sdvigx += 13
            Spider_Man = pygame.image.load('Тема 43.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (155, 290))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 150))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (510 <= ticks - sp_ticks <= 700) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if inertia != 0:
                sdvigx += 1
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 46.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (170, 220))
            SCREEN.blit(Spider_Man, (SMx - 10, SMy + 150))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))






        elif st == 1 and revst == 1 and (700 <= ticks - sp_ticks <= 830) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy -= 115
            if inertia != 0:
                sdvigx += 13
            Spider_Man = pygame.image.load('Тема 47.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (198, 300))
            SCREEN.blit(Spider_Man, (SMx - 40, SMy + 140))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))





        elif st == 1 and revst == 1 and (sdvigy > -330 or (830 <= ticks - sp_ticks <= 900)) and not \
                pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            sdvigy -= 70
            if inertia != 0:
                sdvigx += 13
            if mixst == 0:
                jump.play()
                mixst = 1
            Spider_Man = pygame.image.load('Тема 50.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (230, 280))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 160))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (900 <= ticks - sp_ticks <= 970) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            if sdvigy != -330:
                sdvigy = -330
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            mixst = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 51.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (205, 230))
            SCREEN.blit(Spider_Man, (SMx - 40, SMy + 210))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (970 <= ticks - sp_ticks <= 1040) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            if sdvigy != -330:
                sdvigy = -330
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            mixst = 0
            Spider_Man = pygame.image.load('Тема 54.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (173, 200))
            SCREEN.blit(Spider_Man, (SMx - 32, SMy + 240))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (1040 <= ticks - sp_ticks <= 1110) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 55.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (150, 230))
            SCREEN.blit(Spider_Man, (SMx - 30, SMy + 210))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (1110 <= ticks - sp_ticks <= 1180) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 58.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (140, 270))
            SCREEN.blit(Spider_Man, (SMx - 20, SMy + 170))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))




        elif st == 1 and revst == 1 and (1180 <= ticks - sp_ticks <= 1350) and not pygame.key.get_pressed()[
            pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            if sdvigy != -330:
                sdvigy = -330
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            Spider_Man = pygame.image.load('Тема 59.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (129, 300))
            SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))


        elif st == 1 and revst == 1 and (ticks - sp_ticks > 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            sp_ticks = ticks
            st = 0

        if st == 0 and revst == 0 and sdvigy >= 1600 and -580 <= sdvigx <= -545 and pygame.key.get_pressed()[
            pygame.K_d]:
            st = 6
            if mixst == 1:
                mixst = 0
                run.stop()
            sp_ticks = ticks

        # Сальто вперед
        if st == 6 and revst == 0 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 407.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 14))
        elif st == 6 and revst == 0 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 408.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 100, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 409.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 410.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 416.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 417.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 419.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 0 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 422.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 10))
        elif st == 6 and revst == 0 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 423.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy + 0))
        elif st == 6 and revst == 0 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 425.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 5))
            st = 7
            acs = 2
            crawl_st = 0
            sp_ticks = ticks

        # Падение
        if st == 7 and revst == 0 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 428.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 43, SMy + 25))
        elif st == 7 and revst == 0 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 429.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
        elif st == 7 and revst == 0 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 430.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
            sp_ticks = ticks

        # Приземление + Кувырок
        if st == 8 and revst == 0 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 433.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
        elif st == 8 and revst == 0 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 434.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
        elif st == 8 and revst == 0 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 435.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
        elif st == 8 and revst == 0 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 436.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
        elif st == 8 and revst == 0 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 437.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 190))
        elif st == 8 and revst == 0 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 438.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 215))
        elif st == 8 and revst == 0 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 439.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 70, SMy + 240))
        elif st == 8 and revst == 0 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 440.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 240))
        elif st == 8 and revst == 0 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 441.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 220))
        elif st == 8 and revst == 0 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 442.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 60, SMy + 225))
        elif st == 8 and revst == 0 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 443.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 230))
        elif st == 8 and revst == 0 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 444.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 210))
        elif st == 8 and revst == 0 and crawl_st == 12:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 445.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 310))
            SCREEN.blit(Spider_Man, (SMx - 60, SMy + 210))
        elif st == 8 and revst == 0 and crawl_st == 13:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 446.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 305))
            SCREEN.blit(Spider_Man, (SMx - 55, SMy + 170))
        elif st == 8 and revst == 0 and crawl_st == 14:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 447.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (310, 310))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 147))
            st = 0

        if (st == 0 and revst == 1 and sdvigy >= 1600 and (-850 <= sdvigx <= -830 or 560 <= sdvigx <= 580)
                and pygame.key.get_pressed()[pygame.K_a]):
            st = 6
            musst = 0
            run.stop()
            sp_ticks = ticks

        # Сальто вперед
        if st == 6 and revst == 1 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 411.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 5))
        elif st == 6 and revst == 1 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 412.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 100, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 413.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 414.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 415.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 418.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 420.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
        elif st == 6 and revst == 1 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 421.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 10))
        elif st == 6 and revst == 1 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 424.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy + 0))
        elif st == 6 and revst == 1 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 424.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy - 5))
            st = 7
            acs = 2
            crawl_st = 0
            sp_ticks = ticks

        # Падение
        if st == 7 and revst == 1 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 427.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 43, SMy + 25))
        elif st == 7 and revst == 1 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 431.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
        elif st == 7 and revst == 1 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 432.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
            sp_ticks = ticks

        # Приземление + Кувырок
        if st == 8 and revst == 1 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 448.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
        elif st == 8 and revst == 1 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 449.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
        elif st == 8 and revst == 1 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 450.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
        elif st == 8 and revst == 1 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 451.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
        elif st == 8 and revst == 1 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 452.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
            SCREEN.blit(Spider_Man, (SMx - 73, SMy + 190))
        elif st == 8 and revst == 1 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 453.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 215))
        elif st == 8 and revst == 1 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 454.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 70, SMy + 240))
        elif st == 8 and revst == 1 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 455.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 240))
        elif st == 8 and revst == 1 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 456.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 220))
        elif st == 8 and revst == 1 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 457.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 60, SMy + 225))
        elif st == 8 and revst == 1 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 458.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 230))
        elif st == 8 and revst == 1 and crawl_st == 11:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 459.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
            SCREEN.blit(Spider_Man, (SMx - 50, SMy + 210))
        elif st == 8 and revst == 1 and crawl_st == 12:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 460.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (300, 310))
            SCREEN.blit(Spider_Man, (SMx - 60, SMy + 210))
        elif st == 8 and revst == 1 and crawl_st == 13:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 461.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 305))
            SCREEN.blit(Spider_Man, (SMx - 55, SMy + 170))
        elif st == 8 and revst == 1 and crawl_st == 14:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 462.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (310, 310))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 147))
            st = 0

        # Раскачка на паутине
        if st == 9 and crawl_st == 0 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if sdvigy < 1300:
                if cc > -100000:
                    xx = SMx + 90
                    if ticks - web_ticks >= 10 and cc > 0:
                        cc -= 25
                        web_ticks = 0
                    for x in range(SMx + 60, cc, -1):
                        if lh == 0:
                            xx += 1
                        elif lh == 1:
                            if x % 4 == 0:
                                xx += 1
                        y = amplitude * math.sin(frequency * x) - 240
                        pygame.draw.circle(SCREEN, pygame.Color('White'),
                                           (xx, int(y + x * math.tan(math.radians(angle)))), 1)
            else:
                xx = 1090
                pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 5, wby),
                                 (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 463.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            Spider_Man = pygame.transform.rotate(Spider_Man, 40)
            SCREEN.blit(Spider_Man, (SMx - 140, SMy - 40))
        elif st == 9 and crawl_st == 3 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 1050:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 5, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 463.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            Spider_Man = pygame.transform.rotate(Spider_Man, 40)
            SCREEN.blit(Spider_Man, (SMx - 140, SMy - 40))
        elif st == 9 and crawl_st == 1 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 960:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 40, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 477.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (340, 365))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 50))
        elif st == 9 and crawl_st == 2 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 690:
                xx -= 9
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 48, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 478.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (340, 365))
            SCREEN.blit(Spider_Man, (SMx - 125, SMy + 55))
        # elif st == 9 and crawl_st == 3 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        #     SCREEN.fill(pygame.Color('Black'))
        #     i = 0
        #     while i < tiles:
        #         SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
        #         SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
        #         i += 1
        #     if abs(sdvigx) > bg.get_width():
        #         sdvigx = 0
        #     if dcrawl_st == 0:
        #         Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
        #         Spider_Man = pygame.transform.rotate(Spider_Man, -10)
        #         SCREEN.blit(Spider_Man, (SMx - 75, SMy + 65))
        #     elif dcrawl_st == 1:
        #         Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
        #         SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
        #     elif dcrawl_st == 2:
        #         Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
        #         Spider_Man = pygame.transform.rotate(Spider_Man, 10)
        #         SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
        # elif st == 9 and crawl_st == 4 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        #     SCREEN.fill(pygame.Color('Black'))
        #     i = 0
        #     while i < tiles:
        #         SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
        #         SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
        #         i += 1
        #     if abs(sdvigx) > bg.get_width():
        #         sdvigx = 0
        #     if dcrawl_st == 0:
        #         Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
        #         Spider_Man = pygame.transform.rotate(Spider_Man, -10)
        #         SCREEN.blit(Spider_Man, (SMx - 140, SMy + 30))
        #     elif dcrawl_st == 1:
        #         Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
        #         SCREEN.blit(Spider_Man, (SMx - 90, SMy + 65))
        #     elif dcrawl_st == 2:
        #         Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
        #         Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
        #         Spider_Man = pygame.transform.rotate(Spider_Man, 10)
        #         SCREEN.blit(Spider_Man, (SMx - 100, SMy + 35))
        elif st == 9 and crawl_st == 5 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 620:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 37, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            if dcrawl_st == 0:
                Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
                Spider_Man = pygame.transform.rotate(Spider_Man, -10)
                SCREEN.blit(Spider_Man, (SMx - 135, SMy + 30))
            elif dcrawl_st == 1:
                Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
                SCREEN.blit(Spider_Man, (SMx - 82, SMy + 65))
            elif dcrawl_st == 2:
                Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
                Spider_Man = pygame.transform.rotate(Spider_Man, 10)
                SCREEN.blit(Spider_Man, (SMx - 86, SMy + 33))
        elif st == 9 and crawl_st == 6 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 550:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 38, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 482.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
            SCREEN.blit(Spider_Man, (SMx - 60, SMy + 50))
        elif st == 9 and crawl_st == 7 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 480:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 40, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            if dcrawl_st == 0:
                Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, -10)
                SCREEN.blit(Spider_Man, (SMx - 85, SMy - 15))
            elif dcrawl_st == 1:
                Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                SCREEN.blit(Spider_Man, (SMx - 45, SMy + 10))
            elif dcrawl_st == 2:
                Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, 10)
                SCREEN.blit(Spider_Man, (SMx - 58, SMy - 22))
        elif st == 9 and crawl_st == 8 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 380:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 50, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            if dcrawl_st == 0:
                Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, -10)
                SCREEN.blit(Spider_Man, (SMx - 100, SMy - 25))
            elif dcrawl_st == 1:
                Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                SCREEN.blit(Spider_Man, (SMx - 60, SMy + 3))
            elif dcrawl_st == 2:
                Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, 10)
                SCREEN.blit(Spider_Man, (SMx - 75, SMy - 25))
        elif st == 9 and crawl_st == 9 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 340:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 43, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            if dcrawl_st == 0:
                Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, -10)
                SCREEN.blit(Spider_Man, (SMx - 95, SMy - 45))
            elif dcrawl_st == 1:
                Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                SCREEN.blit(Spider_Man, (SMx - 55, SMy - 15))
            elif dcrawl_st == 2:
                Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, 10)
                SCREEN.blit(Spider_Man, (SMx - 75, SMy - 45))
        elif st == 9 and crawl_st == 10 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            if xx > 310:
                xx -= 3
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 45, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            if dcrawl_st == 0:
                Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, -10)
                SCREEN.blit(Spider_Man, (SMx - 85, SMy - 40))
            elif dcrawl_st == 1:
                Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                SCREEN.blit(Spider_Man, (SMx - 50, SMy - 10))
            elif dcrawl_st == 2:
                Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
                Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
                Spider_Man = pygame.transform.rotate(Spider_Man, 10)
                SCREEN.blit(Spider_Man, (SMx - 70, SMy - 40))

        # Выталкивание
        if st == 10 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            xx = 310
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 45, wby + 55),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 488.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (360, 360))
            Spider_Man = pygame.transform.rotate(Spider_Man, -20)
            SCREEN.blit(Spider_Man, (SMx - 100, SMy - 85))
        elif st == 10 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            xx = 240
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 75, wby + 55),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 489.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (360, 340))
            Spider_Man = pygame.transform.rotate(Spider_Man, -50)
            SCREEN.blit(Spider_Man, (SMx - 115, SMy - 95))
        elif st == 10 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 490.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (380, 340))
            Spider_Man = pygame.transform.rotate(Spider_Man, -50)
            SCREEN.blit(Spider_Man, (SMx - 130, SMy - 85))
        elif st == 10 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 429.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
            Spider_Man = pygame.transform.rotate(Spider_Man, SMRt)
            SCREEN.blit(Spider_Man, (SMx - 40, SMy + 10))

        # Приземление при низком полете №1
        if st == 12 and type_of_landing == 0 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            xx = 240
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 75, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 464.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 70))
        elif st == 12 and type_of_landing == 0 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 465.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 90, SMy + 100))
        elif st == 12 and type_of_landing == 0 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 466.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 130))
        elif st == 12 and type_of_landing == 0 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 467.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 150))
        elif st == 12 and type_of_landing == 0 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 468.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 160))
        elif st == 12 and type_of_landing == 0 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 469.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
            SCREEN.blit(Spider_Man, (SMx - 80, SMy + 170))

        # Приземление при низком полете №2
        if st == 12 and type_of_landing == 1 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            xx = 240
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 492.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 100, SMy + 90))
        elif st == 12 and type_of_landing == 1 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 493.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 100, SMy + 90))
        elif st == 12 and type_of_landing == 1 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 494.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 100, SMy + 50))
        elif st == 12 and type_of_landing == 1 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 495.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 50))
        elif st == 12 and type_of_landing == 1 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 496.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 120, SMy + 50))
        elif st == 12 and type_of_landing == 1 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 497.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 55))
        elif st == 12 and type_of_landing == 1 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 498.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 130, SMy + 115))
        elif st == 12 and type_of_landing == 1 and crawl_st == 7:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 499.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 130, SMy + 130))
        elif st == 12 and type_of_landing == 1 and crawl_st == 8:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 500.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 120, SMy + 165))
        elif st == 12 and type_of_landing == 1 and crawl_st == 9:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 501.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
            SCREEN.blit(Spider_Man, (SMx - 95, SMy + 192))
        elif st == 12 and type_of_landing == 1 and crawl_st == 10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 502.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (340, 350))
            SCREEN.blit(Spider_Man, (SMx - 55, SMy + 223))

        # Приземление при низком полете №3
        if st == 12 and type_of_landing == 2 and crawl_st == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            xx = 240
            pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 35, wby),
                             (xx, -2000 + display_h - 100 + sdvigy), 1)
            Spider_Man = pygame.image.load('Тема 503.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (410, 410))
            SCREEN.blit(Spider_Man, (SMx - 120, SMy + 45))
        elif st == 12 and type_of_landing == 2 and crawl_st == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 504.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (410, 410))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 105))
        elif st == 12 and type_of_landing == 2 and crawl_st == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 505.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
        elif st == 12 and type_of_landing == 2 and crawl_st == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 506.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 138))
        elif st == 12 and type_of_landing == 2 and crawl_st == 4:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 507.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
        elif st == 12 and type_of_landing == 2 and crawl_st == 5:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 508.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 150))
        elif st == 12 and type_of_landing == 2 and crawl_st == 6:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 509.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
            SCREEN.blit(Spider_Man, (SMx - 135, SMy + 170))

        # Триггеры
        if ((st == 0 or st == 1 or st == 7 or st == -5) and -330 < sdvigy <= 1600
                and pygame.key.get_pressed()[pygame.K_LSHIFT]):
            SMRt = 90
            st = 9  # Раскачка на паутине
            sp_ticks = ticks
            acs = 0
            inertia = 0
            crawl_st = 0

        if st == 9 and (1380 <= ticks - sp_ticks <= 2300) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
            st = 10  # Выталкивание
            sp_ticks = ticks
            crawl_st = 0
            inertia = 1

        if st == 9 and (ticks - sp_ticks > 2300) and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            st = 7  # Слабое качание на паутине (пока - просто падение)
            sp_ticks = ticks
            crawl_st = 0
            inertia = 1

        if st == 9 and (1380 > ticks - sp_ticks) and (not pygame.key.get_pressed()[pygame.K_LSHIFT] or sdvigy > 1600):
            st = 7  # Падение при отпускании паутины
            sp_ticks = ticks
            crawl_st = 0
            inertia = 1

        if st == 9 and sdvigy <= -310 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            st = 12  # Приземление при низкой высоте полета
            if type_of_landing == -1:
                type_of_landing = random.randint(0, 2)
            sdvigy = -330
            sp_ticks = ticks
            crawl_st = 0

        if st == 4 and st != -4 and pygame.key.get_pressed()[pygame.K_s]:
            st = -4
            sp_ticks = ticks

        if st == -4 and st != 4 and pygame.key.get_pressed()[pygame.K_w]:
            st = 4
            sp_ticks = ticks

        if st == 4 and pygame.key.get_pressed()[pygame.K_w] and 1550 <= sdvigy <= 1650:
            st = 5
            sp_ticks = ticks

        if st == 4 and pygame.key.get_pressed()[pygame.K_SPACE] and sdvigy >= 50:
            st = -5
            crawl_st = 0
            sp_ticks = ticks
            acs = 2 * (abs(-330 - sdvigy)) // 48
            go_down_in_a_sec = acs
            go_back_in_a_sec = go_down_in_a_sec // 2

        # Ползанье вверх
        if st == 4 and (0 <= ticks - sp_ticks <= 70) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 0
            sdvigy += 15
        elif st == 4 and (70 <= ticks - sp_ticks <= 140) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 1
            sdvigy += 15
        elif st == 4 and (140 <= ticks - sp_ticks <= 210) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 2
            sdvigy += 15
        elif st == 4 and (210 <= ticks - sp_ticks <= 280) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 3
            sdvigy += 15
        elif st == 4 and (280 <= ticks - sp_ticks <= 350) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 4
            sdvigy += 15
        elif st == 4 and (350 <= ticks - sp_ticks <= 420) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 5
            sdvigy += 15
        elif st == 4 and (420 <= ticks - sp_ticks <= 490) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 6
            sdvigy += 15
        elif st == 4 and (490 <= ticks - sp_ticks <= 560) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 7
            sdvigy += 15
        elif st == 4 and (560 <= ticks - sp_ticks <= 630) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 8
            sdvigy += 15
        elif st == 4 and (630 <= ticks - sp_ticks <= 700) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 9
            sdvigy += 15
        elif st == 4 and (700 <= ticks - sp_ticks <= 770) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 10
            sdvigy += 15
        elif st == 4 and (770 <= ticks - sp_ticks <= 840) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 11
            sdvigy += 15
        elif st == 4 and (840 <= ticks - sp_ticks <= 910) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 12
            sdvigy += 15
        elif st == 4 and (910 <= ticks - sp_ticks <= 980) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 13
            sdvigy += 15
        elif st == 4 and (980 <= ticks - sp_ticks <= 1050) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 14
            sdvigy += 15
        elif st == 4 and (1050 <= ticks - sp_ticks <= 1120) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 15
            sdvigy += 15
        elif st == 4 and (1120 <= ticks - sp_ticks <= 1190) and pygame.key.get_pressed()[pygame.K_w] and sdvigy <= 1550:
            crawl_st = 16
            sdvigy += 15
        elif st == 4:
            sp_ticks = ticks
            if 0 < crawl_st < 4 or 14 < crawl_st < 19:
                crawl_st = 0
            elif 4 < crawl_st < 15:
                crawl_st = 6
            # 309 321
            # 0   6

        # Ползанье вниз
        if st == -4 and (0 <= ticks - sp_ticks <= 70) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 0
            sdvigy -= 15
        elif st == -4 and (70 <= ticks - sp_ticks <= 140) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 1
            sdvigy -= 15
        elif st == -4 and (140 <= ticks - sp_ticks <= 210) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 2
            sdvigy -= 15
        elif st == -4 and (210 <= ticks - sp_ticks <= 280) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 3
            sdvigy -= 15
        elif st == -4 and (280 <= ticks - sp_ticks <= 350) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 4
            sdvigy -= 15
        elif st == -4 and (350 <= ticks - sp_ticks <= 420) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 5
            sdvigy -= 15
        elif st == -4 and (420 <= ticks - sp_ticks <= 490) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 6
            sdvigy -= 15
        elif st == -4 and (490 <= ticks - sp_ticks <= 560) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 7
            sdvigy -= 15
        elif st == -4 and (560 <= ticks - sp_ticks <= 630) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 8
            sdvigy -= 15
        elif st == -4 and (630 <= ticks - sp_ticks <= 700) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 9
            sdvigy -= 15
        elif st == -4 and (700 <= ticks - sp_ticks <= 770) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 10
            sdvigy -= 15
        elif st == -4 and (770 <= ticks - sp_ticks <= 840) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 11
            sdvigy -= 15
        elif st == -4 and (840 <= ticks - sp_ticks <= 910) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 12
            sdvigy -= 15
        elif st == -4 and (910 <= ticks - sp_ticks <= 980) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 13
            sdvigy -= 15
        elif st == -4 and (980 <= ticks - sp_ticks <= 1050) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 14
            sdvigy -= 15
        elif st == -4 and (1050 <= ticks - sp_ticks <= 1120) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 15
            sdvigy -= 15
        elif st == -4 and (1120 <= ticks - sp_ticks <= 1190) and pygame.key.get_pressed()[pygame.K_s] and sdvigy >= 0:
            crawl_st = 16
            sdvigy -= 15
        elif st == -4:
            sp_ticks = ticks
            if 0 < crawl_st < 4 or 14 < crawl_st < 19:
                crawl_st = 0
            elif 4 < crawl_st < 15:
                crawl_st = 6
            # 308 320
            # 0   6

        # Запрыгивание на крышу
        if st == 5 and (0 <= ticks - sp_ticks <= 70) and pygame.key.get_pressed()[pygame.K_w]:
            crawl_st = 0
            sdvigy += 35
        elif st == 5 and (70 <= ticks - sp_ticks <= 140) and pygame.key.get_pressed()[pygame.K_w]:
            crawl_st = 1
            sdvigy += 35
        elif st == 5 and (140 <= ticks - sp_ticks <= 210):
            crawl_st = 2
            sdvigy += 25
        elif st == 5 and (210 <= ticks - sp_ticks <= 280):
            crawl_st = 3
            sdvigy += 15
        elif st == 5 and (280 <= ticks - sp_ticks <= 350):
            crawl_st = 4
            sdvigy += 5
        elif st == 5 and (350 <= ticks - sp_ticks <= 420):
            crawl_st = 5
            sdvigx -= 15
        elif st == 5 and (420 <= ticks - sp_ticks <= 490):
            crawl_st = 6
            sdvigy -= 15
            sdvigx -= 15
        elif st == 5 and (490 <= ticks - sp_ticks <= 560):
            crawl_st = 7
            sdvigy = 1758
            sdvigx -= 10
        elif st == 5 and (560 <= ticks - sp_ticks <= 630):
            crawl_st = 8
            sdvigx -= 10
        elif st == 5 and (630 <= ticks - sp_ticks <= 700):
            crawl_st = 9
            sdvigx -= 5
        elif st == 5 and (980 <= ticks - sp_ticks <= 1050):
            crawl_st = 10
        elif st == 5 and (1050 <= ticks - sp_ticks <= 1120):
            crawl_st = 11

        # Спрыгивание со стены
        if st == -5 and (0 <= ticks - sp_ticks <= 70):
            crawl_st = 0
        elif st == -5 and (70 <= ticks - sp_ticks <= 140):
            crawl_st = 1
            sdvigx += go_back_in_a_sec
        elif st == -5 and (140 <= ticks - sp_ticks <= 210):
            crawl_st = 2
            sdvigx += go_back_in_a_sec
        elif st == -5 and (210 <= ticks - sp_ticks <= 280):
            crawl_st = 3
            sdvigx += go_back_in_a_sec
        elif st == -5 and (280 <= ticks - sp_ticks <= 350):
            crawl_st = 4
            sdvigx += go_back_in_a_sec
        elif st == -5 and (350 <= ticks - sp_ticks <= 420):
            crawl_st = 5
            go_down_in_a_sec += 1
            sdvigx += go_back_in_a_sec
            sdvigy -= go_down_in_a_sec
        elif st == -5 and (420 <= ticks - sp_ticks <= 490):
            crawl_st = 6
            sdvigx += go_back_in_a_sec
            sdvigy -= go_down_in_a_sec
        elif st == -5 and (490 <= ticks - sp_ticks <= 560):
            crawl_st = 7
            sdvigx += go_back_in_a_sec
            sdvigy -= go_down_in_a_sec
        elif st == -5 and (560 <= ticks - sp_ticks <= 630):
            crawl_st = 8
            if sdvigy > -330:
                sdvigx += go_back_in_a_sec
                sdvigy -= go_down_in_a_sec
        elif st == -5 and (630 <= ticks - sp_ticks <= 700):
            crawl_st = 9
            if sdvigy > -330:
                sdvigx += go_back_in_a_sec
                sdvigy -= go_down_in_a_sec
        elif st == -5 and (700 <= ticks - sp_ticks <= 770):
            crawl_st = 10
            if sdvigy > -330:
                sdvigx += go_back_in_a_sec
                sdvigy -= go_down_in_a_sec
        elif st == -5 and (770 <= ticks - sp_ticks <= 840):
            crawl_st = 11
            if sdvigy > -330:
                sdvigx += go_back_in_a_sec
                sdvigy -= go_down_in_a_sec
        elif st == -5 and (840 <= ticks - sp_ticks <= 910):
            crawl_st = 12
            if sdvigy > -330:
                sdvigx += go_back_in_a_sec
                sdvigy -= go_down_in_a_sec
        elif st == -5 and (910 <= ticks - sp_ticks <= 980):
            crawl_st = 13
            sdvigy = -330
            if mixst == 0:
                jump.play()
                mixst = 1
        elif st == -5 and (980 <= ticks - sp_ticks <= 1050):
            crawl_st = 14
            sdvigy = -330
            mixst = 0
        elif st == -5 and (1050 <= ticks - sp_ticks <= 1120):
            crawl_st = 15
        elif st == -5 and (1120 <= ticks - sp_ticks <= 1190):
            crawl_st = 16
        elif st == -5 and (1190 <= ticks - sp_ticks <= 1400):
            crawl_st = 17
        elif st == -5 and (ticks - sp_ticks > 1400):
            st = 0

        # Падение
        if st == 7 and sdvigy <= 0:
            st = 8
            sp_ticks = ticks
            crawl_st = 0

        # Сальто вперед
        if st == 6 and (0 <= ticks - sp_ticks <= 70) and sdvigy >= 1550:
            crawl_st = 0
        elif st == 6 and (70 <= ticks - sp_ticks <= 140) and sdvigy >= 1550:
            crawl_st = 1
            sdvigy += 15
            if revst == 0:
                sdvigx -= 15
            elif revst == 1:
                sdvigx += 15
        elif st == 6 and (140 <= ticks - sp_ticks <= 210) and sdvigy >= 1550:
            crawl_st = 2
            sdvigy += 10
            if revst == 0:
                sdvigx -= 10
            elif revst == 1:
                sdvigx += 10
        elif st == 6 and (210 <= ticks - sp_ticks <= 280) and sdvigy >= 1550:
            crawl_st = 3
            sdvigy += 5
            if revst == 0:
                sdvigx -= 10
            elif revst == 1:
                sdvigx += 10
        elif st == 6 and (280 <= ticks - sp_ticks <= 350) and sdvigy >= 1550:
            crawl_st = 4
            if revst == 0:
                sdvigx -= 9
            elif revst == 1:
                sdvigx += 9
        elif st == 6 and (350 <= ticks - sp_ticks <= 420) and sdvigy >= 1550:
            crawl_st = 5
            sdvigy -= 5
            if revst == 0:
                sdvigx -= 8
            elif revst == 1:
                sdvigx += 8
        elif st == 6 and (420 <= ticks - sp_ticks <= 490) and sdvigy >= 1550:
            crawl_st = 6
            sdvigy -= 6
            if revst == 0:
                sdvigx -= 7
            elif revst == 1:
                sdvigx += 7
        elif st == 6 and (490 <= ticks - sp_ticks <= 560) and sdvigy >= 1550:
            crawl_st = 7
            sdvigy -= 8
            if revst == 0:
                sdvigx -= 6
            elif revst == 1:
                sdvigx += 6
        elif st == 6 and (560 <= ticks - sp_ticks <= 630) and sdvigy >= 1550:
            crawl_st = 8
            sdvigy -= 10
            if revst == 0:
                sdvigx -= 5
            elif revst == 1:
                sdvigx += 5
        elif st == 6 and (630 <= ticks - sp_ticks <= 700) and sdvigy >= 1550:
            crawl_st = 9
            sdvigy -= 12
            if revst == 0:
                sdvigx -= 3
            elif revst == 1:
                sdvigx += 3

        # Падение
        if st == 7 and (0 <= ticks - sp_ticks <= 320):
            crawl_st = 0
            if revst == 0:
                if inertia == 1:
                    sdvigx -= 4
                else:
                    sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
        elif st == 7 and (320 <= ticks - sp_ticks <= 640):
            crawl_st = 1
            if revst == 0:
                if inertia == 1:
                    sdvigx -= 4
                else:
                    sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
        elif st == 7 and (640 <= ticks - sp_ticks <= 960):
            crawl_st = 2
            if revst == 0:
                if inertia == 1:
                    sdvigx -= 4
                else:
                    sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
            acs += 4

        # Приземление + кувырок
        if st == 8 and (0 <= ticks - sp_ticks <= 70):
            crawl_st = 0
            if revst == 0:
                sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
            acs += 3
        elif st == 8 and (70 <= ticks - sp_ticks <= 140):
            crawl_st = 1
            if revst == 0:
                sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
            acs += 3
            if mixst == 0:
                grounds.play()
                mixst = 1
        elif st == 8 and (140 <= ticks - sp_ticks <= 200):
            mixst = 0
            crawl_st = 2
            if revst == 0:
                sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
            acs += 3
        elif st == 8 and (200 <= ticks - sp_ticks <= 260):
            crawl_st = 3
            if revst == 0:
                sdvigx -= 1
            elif revst == 1:
                sdvigx += 1
            if sdvigy - 5 - acs > -330:
                sdvigy -= (5 + acs)
            else:
                sdvigy = -330
            acs += 3
        elif st == 8 and (260 <= ticks - sp_ticks <= 300) and sdvigy == -330:
            crawl_st = 4
        elif st == 8 and (300 <= ticks - sp_ticks <= 370):
            crawl_st = 5
            if revst == 0:
                sdvigx -= 10
            elif revst == 1:
                sdvigx += 10
        elif st == 8 and (370 <= ticks - sp_ticks <= 440):
            crawl_st = 6
            if revst == 0:
                sdvigx -= 9
            elif revst == 1:
                sdvigx += 9
        elif st == 8 and (440 <= ticks - sp_ticks <= 510):
            crawl_st = 7
            if revst == 0:
                sdvigx -= 8
            elif revst == 1:
                sdvigx += 8
        elif st == 8 and (510 <= ticks - sp_ticks <= 580):
            crawl_st = 8
            if revst == 0:
                sdvigx -= 7
            elif revst == 1:
                sdvigx += 7
        elif st == 8 and (580 <= ticks - sp_ticks <= 650):
            crawl_st = 9
            if revst == 0:
                sdvigx -= 6
            elif revst == 1:
                sdvigx += 6
        elif st == 8 and (650 <= ticks - sp_ticks <= 720):
            crawl_st = 10
            if revst == 0:
                sdvigx -= 5
            elif revst == 1:
                sdvigx += 5
        elif st == 8 and (720 <= ticks - sp_ticks <= 790):
            crawl_st = 11
            if revst == 0:
                sdvigx -= 4
            elif revst == 1:
                sdvigx += 4
        elif st == 8 and (790 <= ticks - sp_ticks <= 860):
            crawl_st = 12
            if revst == 0:
                sdvigx -= 3
            elif revst == 1:
                sdvigx += 3
        elif st == 8 and (860 <= ticks - sp_ticks <= 930):
            crawl_st = 13
            if musst == 1:
                musst = 2
                musticks = ticks
                pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                        "/Music/fin_Free-Roam.wav")
                pygame.mixer.music.play(0)
                vol = 0.5
                pygame.mixer.music.set_volume(vol)
        elif st == 8 and (930 <= ticks - sp_ticks <= 1000):
            crawl_st = 14
        elif st == 8 and (ticks - sp_ticks > 1000):
            st = 0
            inertia = 0

        # Раскачка на паутине
        if st == 9 and (0 <= ticks - sp_ticks <= 75) and sdvigy >= -1010:
            if revst != 0:
                revst = 0
            crawl_st = 0
            sdvigy -= 5
            sdvigx -= 5
            if mixst == 0:
                mixst = 1
                thwip_mus = random.choice([0, 1, 2, 3])
                if thwip_mus == 0:
                    thwip.play()
                elif thwip_mus == 1:
                    thwip1.play()
                elif thwip_mus == 2:
                    thwip2.play()
                elif thwip_mus == 3:
                    thwip3.play()
        elif st == 9 and (75 <= ticks - sp_ticks <= 150) and sdvigy >= -1010:
            if xx > 1090:
                xx = 1090
            crawl_st = 3
            sdvigy -= 5
            sdvigx -= 5
            mixst = 0
        elif st == 9 and (150 <= ticks - sp_ticks <= 300) and sdvigy >= -1010:
            if xx > 1050:
                xx = 1050
            crawl_st = 1
            sdvigy -= 8
            sdvigx -= 9
        elif st == 9 and (300 <= ticks - sp_ticks <= 450) and sdvigy >= -1010:
            if xx > 960:
                xx = 960
            crawl_st = 2
            sdvigy -= 11
            sdvigx -= 13
            dcrawl_st = 0
        elif st == 9 and (450 <= ticks - sp_ticks <= 600) and sdvigy >= -1010:
            if xx > 960:
                xx = 960
            crawl_st = 2
            sdvigy -= 14
            sdvigx -= 16
        elif st == 9 and (600 <= ticks - sp_ticks <= 750) and sdvigy >= -1010:
            if xx > 960:
                xx = 960
            crawl_st = 2
            dcrawl_st = 1
            # if 600 <= ticks - sp_ticks <= 650:
            #     dcrawl_st = 0
            # elif 650 < ticks - sp_ticks <= 700:
            #     dcrawl_st = 1
            # elif 700 < ticks - sp_ticks < 750:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 750:
            #     dcrawl_st = 0
            sdvigy -= 16
            sdvigx -= 19
        elif st == 9 and (750 <= ticks - sp_ticks <= 850) and sdvigy >= -1010:
            if xx > 690:
                xx = 690
            crawl_st = 5
            dcrawl_st = 1
            # if 750 <= ticks - sp_ticks <= 800:
            #     dcrawl_st = 0
            # elif 800 < ticks - sp_ticks <= 850:
            #     dcrawl_st = 1
            # elif 850 < ticks - sp_ticks < 900:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 900:
            #     dcrawl_st = 0
            if 750 <= ticks - sp_ticks <= 790:
                sdvigy -= 17
            elif 810 <= ticks - sp_ticks <= 850:
                sdvigy += 16
            sdvigx -= 20
        elif st == 9 and (850 <= ticks - sp_ticks <= 930) and sdvigy >= -1010:
            if xx > 620:
                xx = 620
            crawl_st = 6
            sdvigy += 16
            sdvigx -= 19
        elif st == 9 and (930 <= ticks - sp_ticks <= 1080) and sdvigy >= -1010:
            if xx > 550:
                xx = 550
            crawl_st = 7
            dcrawl_st = 1
            # if 1050 <= ticks - sp_ticks <= 1100:
            #     dcrawl_st = 0
            # elif 1100 < ticks - sp_ticks <= 1150:
            #     dcrawl_st = 1
            # elif 1150 < ticks - sp_ticks < 1200:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 1200:
            #     dcrawl_st = 0
            sdvigy += 13
            sdvigx -= 16
            if musst != 1:
                musst = 1
                pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                        "/Music/Free-Roam.wav")
                pygame.mixer.music.play(-1)
                vol = 0.5
                pygame.mixer.music.set_volume(vol)
        elif st == 9 and (1080 <= ticks - sp_ticks <= 1230) and sdvigy >= -1010:
            if xx > 480:
                xx = 480
            crawl_st = 8
            dcrawl_st = 1
            # if 1200 <= ticks - sp_ticks <= 1250:
            #     dcrawl_st = 0
            # elif 1250 < ticks - sp_ticks <= 1300:
            #     dcrawl_st = 1
            # elif 1300 < ticks - sp_ticks < 1350:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 1350:
            #     dcrawl_st = 0
            sdvigy += 10
            sdvigx -= 13
        elif st == 9 and (1230 <= ticks - sp_ticks <= 1380) and sdvigy >= -1010:
            if xx > 380:
                xx = 380
            crawl_st = 9
            dcrawl_st = 1
            # if 1350 <= ticks - sp_ticks <= 1400:
            #     dcrawl_st = 0
            # elif 1400 < ticks - sp_ticks <= 1450:
            #     dcrawl_st = 1
            # elif 1450 < ticks - sp_ticks < 2000:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 2000:
            #     dcrawl_st = 0
            sdvigy += 8
            sdvigx -= 10
        elif st == 9 and (1380 <= ticks - sp_ticks <= 2000) and sdvigy >= -1010:
            if xx > 340:
                xx = 340
            crawl_st = 10
            dcrawl_st = 1
            # if 1500 <= ticks - sp_ticks <= 1550:
            #     dcrawl_st = 0
            # elif 1550 < ticks - sp_ticks <= 1600:
            #     dcrawl_st = 1
            # elif 1600 < ticks - sp_ticks < 2000:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 2000:
            #     dcrawl_st = 0
            sdvigy += 7
            sdvigx -= 9
        elif st == 9 and (2000 <= ticks - sp_ticks <= 2300) and sdvigy >= -1010:
            if xx > 340:
                xx = 340
            crawl_st = 10
            dcrawl_st = 1
            # if 1500 <= ticks - sp_ticks <= 1550:
            #     dcrawl_st = 0
            # elif 1550 < ticks - sp_ticks <= 1600:
            #     dcrawl_st = 1
            # elif 1600 < ticks - sp_ticks < 2000:
            #     dcrawl_st = 2
            # elif ticks - sp_ticks == 2000:
            #     dcrawl_st = 0
            sdvigy += 4
            sdvigx -= 5
        elif st == 9 and sp_ticks > 2300 and sdvigy >= -1010:
            st = 7
            acs = 2
            crawl_st = 0
            sp_ticks = ticks

        # Выталкивание
        if st == 10 and (0 <= ticks - sp_ticks <= 120):
            crawl_st = 0
            sdvigy += 12
            sdvigx -= 10
            if mixst == 0:
                mixst = 1
                swing.play()
        elif st == 10 and (120 <= ticks - sp_ticks <= 200):
            crawl_st = 1
            sdvigy += 8
            sdvigx -= 10
        elif st == 10 and (200 <= ticks - sp_ticks <= 550):
            crawl_st = 2
            sdvigy += 7
            sdvigx -= 9
        elif st == 10 and (550 <= ticks - sp_ticks <= 1300):
            mixst = 0
            crawl_st = 3
            sdvigy += 7
            sdvigx -= 9
            SMRt -= 1
        elif st == 10 and (ticks - sp_ticks > 1300):
            sp_ticks = ticks
            st = 7

        # Приземление при низком полете №1
        if st == 12 and type_of_landing == 0 and (0 <= ticks - sp_ticks <= 100):
            crawl_st = 0
            sdvigx -= 8
        elif st == 12 and type_of_landing == 0 and (100 <= ticks - sp_ticks <= 250):
            crawl_st = 1
            sdvigx -= 7
        elif st == 12 and type_of_landing == 0 and (250 <= ticks - sp_ticks <= 400):
            crawl_st = 2
            sdvigx -= 6
        elif st == 12 and type_of_landing == 0 and (400 <= ticks - sp_ticks <= 500):
            crawl_st = 3
            sdvigx -= 5
        elif st == 12 and type_of_landing == 0 and (500 <= ticks - sp_ticks <= 600):
            crawl_st = 4
        elif st == 12 and type_of_landing == 0 and (600 <= ticks - sp_ticks <= 1100):
            crawl_st = 5
            if musst == 1:
                musst = 2
                pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                        "/Music/fin_Free-Roam.wav")
                pygame.mixer.music.play(0)
                vol = 0.5
                pygame.mixer.music.set_volume(vol)
                musticks = ticks
        elif st == 12 and type_of_landing == 0 and (ticks - sp_ticks > 1100):
            st = 0
            type_of_landing = -1
            inertia = 0

        # Приземление при низком полете №2
        if st == 12 and type_of_landing == 1 and (0 <= ticks - sp_ticks <= 100):
            crawl_st = 0
            sdvigx -= 13
        elif st == 12 and type_of_landing == 1 and (100 <= ticks - sp_ticks <= 200):
            crawl_st = 1
            sdvigx -= 11
        elif st == 12 and type_of_landing == 1 and (200 <= ticks - sp_ticks <= 300):
            crawl_st = 2
            sdvigx -= 9
        elif st == 12 and type_of_landing == 1 and (300 <= ticks - sp_ticks <= 400):
            crawl_st = 3
            sdvigx -= 7
        elif st == 12 and type_of_landing == 1 and (400 <= ticks - sp_ticks <= 500):
            crawl_st = 4
            sdvigx -= 6
        elif st == 12 and type_of_landing == 1 and (500 <= ticks - sp_ticks <= 600):
            crawl_st = 5
            sdvigx -= 5
        elif st == 12 and type_of_landing == 1 and (600 <= ticks - sp_ticks <= 700):
            crawl_st = 6
            sdvigx -= 4
        elif st == 12 and type_of_landing == 1 and (700 <= ticks - sp_ticks <= 800):
            crawl_st = 7
            sdvigx -= 3
            if musst == 1:
                musst = 2
                musticks = ticks
                pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                        "/Music/fin_Free-Roam.wav")
                pygame.mixer.music.play(0)
                vol = 0.5
                pygame.mixer.music.set_volume(vol)
        elif st == 12 and type_of_landing == 1 and (800 <= ticks - sp_ticks <= 900):
            crawl_st = 8
        elif st == 12 and type_of_landing == 1 and (900 <= ticks - sp_ticks <= 1000):
            crawl_st = 9
        elif st == 12 and type_of_landing == 1 and (1000 <= ticks - sp_ticks <= 1500):
            crawl_st = 10
        elif st == 12 and type_of_landing == 1 and (ticks - sp_ticks > 1500):
            st = 0
            type_of_landing = -1
            inertia = 0

        # Приземление при низком полете №3
        if st == 12 and type_of_landing == 2 and (0 <= ticks - sp_ticks <= 100):
            crawl_st = 0
            sdvigx -= 12
        elif st == 12 and type_of_landing == 2 and (100 <= ticks - sp_ticks <= 200):
            crawl_st = 1
            sdvigx -= 9
        elif st == 12 and type_of_landing == 2 and (200 <= ticks - sp_ticks <= 300):
            crawl_st = 2
            sdvigx -= 7
        elif st == 12 and type_of_landing == 2 and (300 <= ticks - sp_ticks <= 400):
            crawl_st = 3
            sdvigx -= 5
        elif st == 12 and type_of_landing == 2 and (400 <= ticks - sp_ticks <= 500):
            crawl_st = 4
        elif st == 12 and type_of_landing == 2 and (500 <= ticks - sp_ticks <= 600):
            crawl_st = 5
            if musst == 1:
                musst = 2
                musticks = ticks
                pygame.mixer.music.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                        "/Music/fin_Free-Roam.wav")
                pygame.mixer.music.play(0)
                vol = 0.5
                pygame.mixer.music.set_volume(vol)
        elif st == 12 and type_of_landing == 2 and (600 <= ticks - sp_ticks <= 1100):
            crawl_st = 6
        elif st == 12 and type_of_landing == 2 and (ticks - sp_ticks > 1100):
            st = 0
            type_of_landing = -1
            inertia = 0

        # Триггеры

        # Реакция на удар
        if (sdvigy <= -330 and ((thug_st == 2 and th_st == 3 and thug_type_of_hit == 0)
                                or thug_st == 2 and th_st == 3 and thug_type_of_hit == 1) and health - harm <= 0
            and spider_type_of_react != 0) and st != 12 and st != -10:
            st = 13
            sp_ticks = ticks
            crawl_st = 0
            health -= harm
            spider_type_of_react = 0  # смерть от удара в лицо
            thug_st = -11
            sp_death.play()
        elif (sdvigy <= -330 and ((thug_st == 2 and th_st == 3 and thug_type_of_hit == 0)
                                  or thug_st == 2 and th_st == 3 and thug_type_of_hit == 1) and health - harm >= 0
              and st != 12):
            st = 12
            sp_ticks = ticks
            crawl_st = 0
            health -= harm
            hit_mix = random.choice([0, 1, 2, 3])
            if hit_mix == 0:
                hitt.play()
            elif hit_mix == 1:
                hit1.play()
            elif hit_mix == 2:
                hit2.play()
            elif hit_mix == 3:
                hit3.play()
            spider_type_of_react = 2  # реакция на удар в лицо

        if st == -10:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D"
                                    "/Fonts/GULAG.otf", 25 * kx)
            text = font.render('!HELP!', True,
                               (255, 0, 0))
            SCREEN.blit(text, (420, 250))
            pygame.draw.line(SCREEN, (255, 0, 0), [400, 280], [1080, 280], 2)
            pygame.draw.line(SCREEN, (255, 0, 0), [400, 380], [1080, 380], 2)
            font = pygame.font.Font('MonospaceBold.ttf', 55 * kx)
            text = font.render("YOU'RE FAILED, BUDDY", True, (255, 0, 0))
            SCREEN.blit(text, (410, 300))
            pygame.display.update()
            pygame.time.wait(5000)
            st, sdvigy, hp, musst = 0, -330, 100, 0

        # Переход в боевую стойку
        if st == 0 and pygame.mouse.get_pressed() == (True, False, False) and st != 2 and fight_ready_pose == 0:
            st, fight_ready, sp_ticks = 2, 0, ticks

        # Выход из боевой стойки
        if st == 2 and pygame.mouse.get_pressed() == (False, False, False) and st != 0 and fight_ready_pose == 1 \
                and (ticks - sp_ticks >= 5000):
            st, sp_ticks, fight_ready_pose = 0, ticks, 0

        # Боевая стойка
        if fight_ready_pose == 0:
            if st == 2 and sdvigy <= -330 and (0 <= ticks - sp_ticks <= 50 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 61.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (143, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 62.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (143, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))

            elif st == 2 and sdvigy <= -330 and (50 <= ticks - sp_ticks <= 100 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 63.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (126, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 64.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (126, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))

            elif st == 2 and sdvigy <= -330 and (100 <= ticks - sp_ticks <= 150 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 66.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (144, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 65.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (144, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))

            elif st == 2 and sdvigy <= -330 and (150 <= ticks - sp_ticks <= 200 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 67.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (160, 285))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 155))
                else:
                    Spider_Man = pygame.image.load('Тема 68.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (160, 285))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 155))

            elif st == 2 and sdvigy <= -330 and (200 <= ticks - sp_ticks <= 250 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 70.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (163, 290))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 150))
                else:
                    Spider_Man = pygame.image.load('Тема 69.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (163, 290))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 150))

            elif st == 2 and sdvigy <= -330 and (250 <= ticks - sp_ticks <= 300 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 71.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 72.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))

            elif st == 2 and sdvigy <= -330 and (300 <= ticks - sp_ticks <= 350 or sp_ticks == 0):
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 74.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 73.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                sp_ticks = ticks
                fight_ready = 1
                fight_ready_pose = 1

        elif fight_ready_pose == 1 and hit != 1 and evasion == 0:
            if st == 2 and sdvigy <= -330:
                SCREEN.fill(pygame.Color('Black'))
                i = 0
                while i < tiles:
                    SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                    SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                    SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                    SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                    i += 1
                if abs(sdvigx) > bg.get_width():
                    sdvigx = 0
                pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                        "/MonospaceBold.ttf", 25 * kx)
                text = font.render(str(health), True, pygame.Color("red"))
                tx, ty = 60, 52
                SCREEN.blit(text, (tx, ty))
                if revst == 0:
                    Spider_Man = pygame.image.load('Тема 74.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                else:
                    Spider_Man = pygame.image.load('Тема 73.png').convert_alpha()
                    Spider_Man = pygame.transform.scale(Spider_Man, (152, 300))
                    SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
                # sp_ticks = ticks
                fight_ready = 1

        # Удары
        if fight_ready_pose == 1 and (pygame.mouse.get_pressed() == (True, False, False) or hit == 1) and st == 2:
            if hit == 0:
                sp_ticks = ticks
                type_of_hit = random.choice([0, 1, 2, 4, 5, 6])
                hit = 1

            # 1 Удар ногой с подкруткой
            if type_of_hit == 0:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 75.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (236, 245))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 195))
                    else:
                        Spider_Man = pygame.image.load('Тема 76.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (236, 245))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 195))


                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 78.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (175, 245))
                        SCREEN.blit(Spider_Man, (SMx - 15, SMy + 195))
                    else:
                        Spider_Man = pygame.image.load('Тема 77.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (175, 245))
                        SCREEN.blit(Spider_Man, (SMx - 15, SMy + 195))


                elif 140 <= ticks - sp_ticks <= 210:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 79.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (232, 255))
                        SCREEN.blit(Spider_Man, (SMx - 65, SMy + 185))
                    else:
                        Spider_Man = pygame.image.load('Тема 80.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (232, 255))
                        SCREEN.blit(Spider_Man, (SMx - 65, SMy + 185))

                elif 210 <= ticks - sp_ticks <= 280:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 82.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (173, 245))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 195))
                    else:
                        Spider_Man = pygame.image.load('Тема 81.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (173, 245))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 195))


                elif 280 <= ticks - sp_ticks <= 370:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 83.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 235))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 205))
                    else:
                        Spider_Man = pygame.image.load('Тема 84.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 235))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 205))


                elif 370 <= ticks - sp_ticks <= 470:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 86.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 270))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 170))
                    else:
                        Spider_Man = pygame.image.load('Тема 85.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 270))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 170))

                elif 470 <= ticks - sp_ticks <= 570:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 87.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (138, 275))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 165))
                    else:
                        Spider_Man = pygame.image.load('Тема 88.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (138, 275))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 165))


                elif 570 <= ticks - sp_ticks <= 640:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 90.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (110, 215))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 225))
                    else:
                        Spider_Man = pygame.image.load('Тема 89.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (110, 215))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 225))

                elif 640 <= ticks - sp_ticks <= 720:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 91.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (179, 205))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 235))
                    else:
                        Spider_Man = pygame.image.load('Тема 92.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (179, 205))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 235))


                elif 720 <= ticks - sp_ticks <= 790:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 94.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 240))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 200))
                    else:
                        Spider_Man = pygame.image.load('Тема 93.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 240))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 200))
                elif ticks - sp_ticks > 790:
                    type_of_hit = -1
                    sp_ticks = ticks
                    hit = 0

            # 2 Удар ногой прямо
            elif type_of_hit == 1:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 109.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (222, 360))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 113))
                    else:
                        Spider_Man = pygame.image.load('Тема 108.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (220, 295))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 152))


                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 110.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (212, 375))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 108))
                    else:
                        Spider_Man = pygame.image.load('Тема 111.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 377))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 100))


                elif 140 <= ticks - sp_ticks <= 290:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 107.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 285))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 155))
                    else:
                        Spider_Man = pygame.image.load('Тема 112.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (235, 387))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 90))


                elif 290 <= ticks - sp_ticks <= 490:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 113.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (246, 375))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 114.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (250, 375))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 101))


                elif 490 <= ticks - sp_ticks <= 660:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 116.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (193, 360))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 112))
                    else:
                        Spider_Man = pygame.image.load('Тема 115.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 367))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 100))


                elif 660 <= ticks - sp_ticks <= 750:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 117.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (155, 325))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 128))
                    else:
                        Spider_Man = pygame.image.load('Тема 118.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 330))
                        SCREEN.blit(Spider_Man, (SMx - 0, SMy + 112))

                # elif 750 <= ticks - sp_ticks <= 950:
                #     SCREEN.fill(pygame.Color('Black'))
                #     i = 0
                #     while i < tiles:
                #         SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                #         SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                #         i += 1
                #     Spider_Man = pygame.image.load('Тема 120.png').convert_alpha()
                #     Spider_Man = pygame.transform.scale(Spider_Man, (221, 385))
                #     SCREEN.blit(Spider_Man, (SMx - 40, SMy + 105))
                elif ticks - sp_ticks > 750:
                    type_of_hit = -1
                    sp_ticks = ticks
                    hit = 0

            # 3 Удар ногой в прыжке
            elif type_of_hit == 2:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0

                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 8
                        Spider_Man = pygame.image.load('Тема 122.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (178, 340))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 123))
                    else:
                        sdvigx += 8
                        Spider_Man = pygame.image.load('Тема 121.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (178, 340))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 123))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0

                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 6
                        Spider_Man = pygame.image.load('Тема 123.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (210, 395))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 75))
                    else:
                        sdvigx += 6
                        Spider_Man = pygame.image.load('Тема 124.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (210, 395))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 75))


                elif 140 <= ticks - sp_ticks <= 290:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 126.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (205, 400))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 45))
                    else:
                        sdvigx += 5
                        Spider_Man = pygame.image.load('Тема 125.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (205, 400))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 45))

                elif 290 <= ticks - sp_ticks <= 490:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0

                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 127.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (298, 420))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 5))
                    else:
                        sdvigx += 5
                        Spider_Man = pygame.image.load('Тема 128.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (298, 420))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 5))



                elif 490 <= ticks - sp_ticks <= 660:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 130.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (310, 420))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy - 10))
                    else:
                        sdvigx += 5
                        Spider_Man = pygame.image.load('Тема 129.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (310, 420))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy - 10))



                elif 660 <= ticks - sp_ticks <= 750:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 2
                        Spider_Man = pygame.image.load('Тема 131.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (278, 380))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 70))
                    else:
                        sdvigx += 2
                        Spider_Man = pygame.image.load('Тема 132.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (278, 380))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 70))

                elif 750 <= ticks - sp_ticks <= 880:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 134.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 390))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 110))
                    else:
                        Spider_Man = pygame.image.load('Тема 133.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 390))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 110))

                elif 880 <= ticks - sp_ticks <= 950:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 135.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (199, 410))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 136.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (199, 410))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))

                elif 950 <= ticks - sp_ticks <= 1020:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 138.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 400))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 137.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 400))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))

                elif 1020 <= ticks - sp_ticks <= 1090:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 139.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 377))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 140.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 377))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    fight_ready_pose = 1
                elif ticks - sp_ticks > 1090:
                    type_of_hit = -1
                    sp_ticks = ticks
                    hit = 0

            # 4 Удар ногой стоя
            elif type_of_hit == 3:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 168.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (220, 330))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 143))
                    else:
                        Spider_Man = pygame.image.load('Тема 167.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 330))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 143))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 169.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (210, 345))
                        SCREEN.blit(Spider_Man, (SMx - 62, SMy + 115))
                    else:
                        Spider_Man = pygame.image.load('Тема 170.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 345))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))

                elif 140 <= ticks - sp_ticks <= 290:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 172.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (205, 370))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 171.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (220, 370))
                        SCREEN.blit(Spider_Man, (SMx - 85, SMy + 98))

                elif 290 <= ticks - sp_ticks <= 350:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 173.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 370))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 174.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 370))
                        SCREEN.blit(Spider_Man, (SMx - 85, SMy + 97))

                elif 350 <= ticks - sp_ticks <= 550:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 176.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (236, 362))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 175.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (255, 362))
                        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 100))

                elif 550 <= ticks - sp_ticks <= 640:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 177.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (217, 360))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 178.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (217, 360))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 120))

                elif 640 <= ticks - sp_ticks <= 730:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 180.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (219, 370))
                        SCREEN.blit(Spider_Man, (SMx - 55, SMy + 112))
                    else:
                        Spider_Man = pygame.image.load('Тема 179.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (219, 370))
                        SCREEN.blit(Spider_Man, (SMx - 55, SMy + 112))
                elif ticks - sp_ticks > 730:
                    sp_ticks = ticks
                    type_of_hit = -1
                    hit = 0

            # 5 Удар ногой с работой бедра
            elif type_of_hit == 4:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 279.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 340))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 127))
                    else:
                        Spider_Man = pygame.image.load('Тема 278.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 340))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 127))



                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 280.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (177, 345))
                        SCREEN.blit(Spider_Man, (SMx - 8, SMy + 115))
                    else:
                        Spider_Man = pygame.image.load('Тема 281.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (177, 345))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 115))



                elif 140 <= ticks - sp_ticks <= 240:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 284.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (172, 360))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 110))
                    else:
                        Spider_Man = pygame.image.load('Тема 282.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (172, 360))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 110))



                elif 240 <= ticks - sp_ticks <= 440:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 285.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (270, 370))
                        SCREEN.blit(Spider_Man, (SMx + 2, SMy + 107))
                    else:
                        Spider_Man = pygame.image.load('Тема 286.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (250, 375))
                        SCREEN.blit(Spider_Man, (SMx - 85, SMy + 102))



                elif 440 <= ticks - sp_ticks <= 560:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 288.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (215, 375))
                        SCREEN.blit(Spider_Man, (SMx - 15, SMy + 115))
                    else:
                        Spider_Man = pygame.image.load('Тема 283.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 260))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 178))



                elif 560 <= ticks - sp_ticks <= 650:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 289.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 370))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 120))
                    else:
                        Spider_Man = pygame.image.load('Тема 287.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (150, 260))
                        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 180))


                elif 650 <= ticks - sp_ticks <= 730:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 291.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (155, 335))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 135))
                    else:
                        Spider_Man = pygame.image.load('Тема 290.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (155, 345))
                        SCREEN.blit(Spider_Man, (SMx + 30, SMy + 128))
                elif ticks - sp_ticks > 730:
                    sp_ticks = ticks
                    type_of_hit = -1
                    hit = 0

            # 6 Удар рукой в прыжке
            elif type_of_hit == 5:
                if 0 <= ticks - sp_ticks <= 100:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 8
                        Spider_Man = pygame.image.load('Тема 249.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (156, 340))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))
                    else:
                        sdvigx += 8
                        Spider_Man = pygame.image.load('Тема 248.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (156, 340))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))

                elif 100 <= ticks - sp_ticks <= 200:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 10
                        Spider_Man = pygame.image.load('Тема 253.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 360))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 110))
                    else:
                        sdvigx += 10
                        Spider_Man = pygame.image.load('Тема 252.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (184, 360))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 110))

                elif 200 <= ticks - sp_ticks <= 400:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 254.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 159))
                    else:
                        Spider_Man = pygame.image.load('Тема 255.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 159))

                elif 400 <= ticks - sp_ticks <= 500:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 6
                        Spider_Man = pygame.image.load('Тема 257.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (193, 420))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 10))
                    else:
                        sdvigx += 6
                        Spider_Man = pygame.image.load('Тема 256.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (193, 420))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 10))

                elif 500 <= ticks - sp_ticks <= 650:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 8
                        Spider_Man = pygame.image.load('Тема 258.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 365))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy - 10))
                    else:
                        sdvigx += 8
                        Spider_Man = pygame.image.load('Тема 259.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 365))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy - 10))

                elif 650 <= ticks - sp_ticks <= 800:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 9
                        Spider_Man = pygame.image.load('Тема 261.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 410))
                        SCREEN.blit(Spider_Man, (SMx - 15, SMy - 20))
                    else:
                        sdvigx += 9
                        Spider_Man = pygame.image.load('Тема 260.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 410))
                        SCREEN.blit(Spider_Man, (SMx - 15, SMy - 20))

                elif 800 <= ticks - sp_ticks <= 950:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 10
                        Spider_Man = pygame.image.load('Тема 262.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (220, 430))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy - 40))
                    else:
                        sdvigx += 10
                        Spider_Man = pygame.image.load('Тема 263.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (220, 430))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy - 40))

                elif 950 <= ticks - sp_ticks <= 1100:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        if not (th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (th_revst == 1
                                                                                    and SMx - (Thx - th_sdvigx) <= 100):
                            sdvigx -= 8
                        Spider_Man = pygame.image.load('Тема 265.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 430))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 0))
                    else:
                        sdvigx += 8
                        Spider_Man = pygame.image.load('Тема 264.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 430))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 0))

                elif 1100 <= ticks - sp_ticks <= 1450:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 266.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (215, 395))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 267.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (215, 395))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 100))
                elif ticks - sp_ticks > 1450:
                    sp_ticks = ticks
                    type_of_hit = -1
                    hit = 0

            # 7 Удар рукой
            elif type_of_hit == 6:
                if 0 <= ticks - sp_ticks <= 90:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 292.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (165, 360))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 293.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 360))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 105))

                elif 90 <= ticks - sp_ticks <= 180:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 295.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (188, 360))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 294.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (188, 360))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 105))

                elif 180 <= ticks - sp_ticks <= 270:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 296.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (196, 355))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 108))
                    else:
                        Spider_Man = pygame.image.load('Тема 297.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (196, 355))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 108))

                elif 270 <= ticks - sp_ticks <= 360:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 299.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (187, 340))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 123))
                    else:
                        Spider_Man = pygame.image.load('Тема 298.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (187, 340))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 123))

                elif 360 <= ticks - sp_ticks <= 450:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 300.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 353))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 109))
                    else:
                        Spider_Man = pygame.image.load('Тема 301.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 353))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 109))

                elif 450 <= ticks - sp_ticks <= 650:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 307.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 358))
                        SCREEN.blit(Spider_Man, (SMx - 23, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 302.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 358))
                        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 105))

                elif 650 <= ticks - sp_ticks <= 740:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 303.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 359))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 304.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (200, 359))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 105))
                elif 740 <= ticks - sp_ticks <= 830:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 306.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 357))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 105))
                    else:
                        Spider_Man = pygame.image.load('Тема 305.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 357))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 105))
                    fight_ready_pose = 1
                elif ticks - sp_ticks > 830:
                    sp_ticks = ticks
                    type_of_hit = -1
                    hit = 0

        # print(pygame.key.get_pressed()[pygame.K_LCTRL], st)
        # Уклонения
        if (pygame.key.get_pressed()[pygame.K_LCTRL] or evasion == 1) and st in [0, 2]:
            if evasion == 0:
                sp_ticks = ticks
                if st == 100:
                    type_of_evasion = random.choice([0, 1, 2, 3, 4])
                else:
                    type_of_evasion = random.choice([1, 2, 3, 4])
            evasion = 1
            # if type_of_evasion == 0 and evasion != 0:
            #     evasion = 0

            # 1 Уклонение вбок
            if type_of_evasion == 0:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 96.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (84, 295))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 145))
                    else:
                        Spider_Man = pygame.image.load('Тема 95.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (84, 295))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 145))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 97.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (110, 295))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 145))
                    else:
                        Spider_Man = pygame.image.load('Тема 98.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (110, 295))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 145))

                elif 140 <= ticks - sp_ticks <= 210:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 99.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (123, 285))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 155))
                    else:
                        Spider_Man = pygame.image.load('Тема 100.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (123, 285))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 155))

                elif 210 <= ticks - sp_ticks <= 280:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 101.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (153, 270))
                        SCREEN.blit(Spider_Man, (SMx - 8, SMy + 170))
                    else:
                        Spider_Man = pygame.image.load('Тема 102.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (153, 270))
                        SCREEN.blit(Spider_Man, (SMx - 8, SMy + 170))

                elif 280 <= ticks - sp_ticks <= 370:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 104.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (127, 270))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 170))
                    else:
                        Spider_Man = pygame.image.load('Тема 103.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (127, 270))
                        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 170))

                elif 370 <= ticks - sp_ticks <= 470:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 105.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (105, 275))
                        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 165))
                    else:
                        Spider_Man = pygame.image.load('Тема 106.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (105, 275))
                        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 165))

                elif 470 <= ticks - sp_ticks <= 570:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 96.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (80, 290))
                        SCREEN.blit(Spider_Man, (SMx + 22, SMy + 150))
                    else:
                        Spider_Man = pygame.image.load('Тема 95.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (80, 290))
                        SCREEN.blit(Spider_Man, (SMx + 22, SMy + 150))
                    fight_ready_pose = 1

                elif ticks - sp_ticks > 570:
                    fight_ready = 0
                    sp_ticks = ticks
                    evasion = 0

            # 2 Сальто назад с рукой
            elif type_of_evasion == 1:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 142.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (206, 365))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 111))

                    else:
                        Spider_Man = pygame.image.load('Тема 141.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (206, 365))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 111))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 143.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (224, 325))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 155))
                    else:
                        Spider_Man = pygame.image.load('Тема 144.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (224, 325))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 155))

                elif 140 <= ticks - sp_ticks <= 210:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 146.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (255, 325))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 155))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 145.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (255, 325))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 155))

                elif 210 <= ticks - sp_ticks <= 280:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 147.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 340))
                        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 150))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 148.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (240, 340))
                        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 150))

                elif 280 <= ticks - sp_ticks <= 350:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 150.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (300, 340))
                        SCREEN.blit(Spider_Man, (SMx - 105, SMy + 155))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 149.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (300, 340))
                        SCREEN.blit(Spider_Man, (SMx - 105, SMy + 155))

                elif 350 <= ticks - sp_ticks <= 420:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 35
                        Spider_Man = pygame.image.load('Тема 151.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 340))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 159))
                    else:
                        sdvigx -= 35
                        Spider_Man = pygame.image.load('Тема 152.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 340))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 159))

                elif 420 <= ticks - sp_ticks <= 490:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 35
                        Spider_Man = pygame.image.load('Тема 154.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (205, 330))
                        SCREEN.blit(Spider_Man, (SMx - 22, SMy + 153))
                    else:
                        sdvigx -= 35
                        Spider_Man = pygame.image.load('Тема 153.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (205, 330))
                        SCREEN.blit(Spider_Man, (SMx - 22, SMy + 153))

                elif 490 <= ticks - sp_ticks <= 600:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 155.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 350))
                        SCREEN.blit(Spider_Man, (SMx - 37, SMy + 118))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 156.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 350))
                        SCREEN.blit(Spider_Man, (SMx - 37, SMy + 118))

                elif 600 <= ticks - sp_ticks <= 670:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 158.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (173, 360))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 130))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 157.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (173, 360))
                        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 130))

                elif 670 <= ticks - sp_ticks <= 740:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 159.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (223, 317))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 177))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 160.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (223, 317))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 177))

                elif 740 <= ticks - sp_ticks <= 810:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 162.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (212, 330))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 182))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 161.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (212, 330))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 182))

                elif 810 <= ticks - sp_ticks <= 880:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 163.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (203, 335))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
                    else:
                        Spider_Man = pygame.image.load('Тема 164.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (203, 335))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))

                elif 880 <= ticks - sp_ticks <= 950:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if abs(sdvigx) > bg.get_width():
                        sdvigx = 0
                    pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
                    pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
                    font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                            "/MonospaceBold.ttf", 25 * kx)
                    text = font.render(str(health), True, pygame.Color("red"))
                    tx, ty = 60, 52
                    SCREEN.blit(text, (tx, ty))
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 166.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 330))
                        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 167))
                    else:
                        Spider_Man = pygame.image.load('Тема 165.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 330))
                        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 167))

                elif ticks - sp_ticks > 950:
                    sp_ticks = ticks
                    evasion = 0


            # 3 Уклонение с перекрутом в стиле Тоби
            elif type_of_evasion == 2:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 185.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (203, 350))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 120))
                    else:
                        Spider_Man = pygame.image.load('Тема 187.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (203, 350))
                        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 120))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 189.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (254, 340))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 123))
                    else:
                        Spider_Man = pygame.image.load('Тема 188.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (254, 340))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 123))

                elif 140 <= ticks - sp_ticks <= 210:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 190.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 270))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 172))
                    else:
                        sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 191.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 270))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 172))

                elif 210 <= ticks - sp_ticks <= 280:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 193.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 340))
                        SCREEN.blit(Spider_Man, (SMx - 95, SMy + 135))
                    else:
                        sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 192.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 340))
                        SCREEN.blit(Spider_Man, (SMx - 95, SMy + 135))

                elif 280 <= ticks - sp_ticks <= 350:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 194.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (228, 360))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 117))
                    else:
                        sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 195.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (228, 360))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 117))

                elif 350 <= ticks - sp_ticks <= 420:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 197.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (310, 370))
                        SCREEN.blit(Spider_Man, (SMx - 120, SMy + 110))
                    else:
                        sdvigx -= 5
                        Spider_Man = pygame.image.load('Тема 196.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (310, 370))
                        SCREEN.blit(Spider_Man, (SMx - 120, SMy + 110))

                elif 420 <= ticks - sp_ticks <= 490:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 198.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (260, 380))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 110))
                    else:
                        sdvigx -= 12
                        Spider_Man = pygame.image.load('Тема 199.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (260, 380))
                        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 110))

                elif 490 <= ticks - sp_ticks <= 600:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 201.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (234, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 70))
                    else:
                        sdvigx -= 12
                        Spider_Man = pygame.image.load('Тема 200.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (234, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 70))

                elif 600 <= ticks - sp_ticks <= 670:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 202.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 380))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 50))
                    else:
                        sdvigx -= 12
                        Spider_Man = pygame.image.load('Тема 203.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 380))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 50))


                elif 670 <= ticks - sp_ticks <= 740:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 205.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (221, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 50))
                    else:
                        sdvigx -= 12
                        Spider_Man = pygame.image.load('Тема 204.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (221, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 50))

                elif 740 <= ticks - sp_ticks <= 810:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 206.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 380))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 110))
                    else:
                        sdvigx -= 10
                        Spider_Man = pygame.image.load('Тема 207.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (182, 380))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 110))

                elif 810 <= ticks - sp_ticks <= 880:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 209.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (260, 385))
                        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 126))
                    else:
                        Spider_Man = pygame.image.load('Тема 208.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (260, 385))
                        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 126))

                elif 880 <= ticks - sp_ticks <= 950:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 210.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 395))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 118))
                    else:
                        Spider_Man = pygame.image.load('Тема 211.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 395))
                        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 118))

                elif 950 <= ticks - sp_ticks <= 1020:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 213.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (218, 380))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 126))
                    else:
                        Spider_Man = pygame.image.load('Тема 212.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (218, 380))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 126))

                elif 1020 <= ticks - sp_ticks <= 1090:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 214.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (195, 370))
                        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 140))
                    else:
                        Spider_Man = pygame.image.load('Тема 215.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (195, 370))
                        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 140))

                elif ticks - sp_ticks > 1090:
                    sp_ticks = ticks
                    evasion = 0


            # 4 Уклонение в стиле брейк-данс
            elif type_of_evasion == 3:
                if 0 <= ticks - sp_ticks <= 70:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 217.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 138))
                    else:
                        Spider_Man = pygame.image.load('Тема 216.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
                        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 138))

                elif 70 <= ticks - sp_ticks <= 140:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 218.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))
                    else:
                        Spider_Man = pygame.image.load('Тема 219.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (225, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 100))

                elif 140 <= ticks - sp_ticks <= 240:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 221.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (210, 380))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 122))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 220.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (210, 380))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 122))

                elif 240 <= ticks - sp_ticks <= 310:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 222.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (215, 380))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 118))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 223.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (215, 380))
                        SCREEN.blit(Spider_Man, (SMx - 25, SMy + 118))

                elif 310 <= ticks - sp_ticks <= 380:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 225.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 350))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 125))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 224.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 350))
                        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 125))

                elif 380 <= ticks - sp_ticks <= 470:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 227.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 350))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 120))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 226.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 350))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 120))

                elif 470 <= ticks - sp_ticks <= 620:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 228.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 360))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 113))
                    else:
                        sdvigx -= 25
                        Spider_Man = pygame.image.load('Тема 229.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 360))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 113))

                elif 620 <= ticks - sp_ticks <= 770:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 231.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 365))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 110))
                    else:
                        sdvigx -= 25
                        Spider_Man = pygame.image.load('Тема 230.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (170, 365))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 110))

                elif 770 <= ticks - sp_ticks <= 920:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 25
                        Spider_Man = pygame.image.load('Тема 232.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (178, 385))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 87))
                    else:
                        sdvigx -= 25
                        Spider_Man = pygame.image.load('Тема 233.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (178, 385))
                        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 87))

                elif 920 <= ticks - sp_ticks <= 1070:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 235.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 385))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 90))
                    else:
                        Spider_Man = pygame.image.load('Тема 234.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (180, 385))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 90))

                elif 1070 <= ticks - sp_ticks <= 1160:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 236.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (176, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 92))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 237.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (176, 380))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 92))
                elif 1160 <= ticks - sp_ticks <= 1250:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 20
                        Spider_Man = pygame.image.load('Тема 239.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 400))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 71))
                    else:
                        sdvigx -= 20
                        Spider_Man = pygame.image.load('Тема 238.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (230, 400))
                        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 71))
                elif 1250 <= ticks - sp_ticks <= 1340:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 240.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 395))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 105))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 241.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (245, 395))
                        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 105))
                elif 1340 <= ticks - sp_ticks <= 1420:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        sdvigx += 15
                        Spider_Man = pygame.image.load('Тема 243.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (195, 370))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 120))
                    else:
                        sdvigx -= 15
                        Spider_Man = pygame.image.load('Тема 242.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (195, 370))
                        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 120))
                elif 1420 <= ticks - sp_ticks <= 1510:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 244.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 360))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 140))
                    else:
                        Spider_Man = pygame.image.load('Тема 245.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (190, 360))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 140))
                elif 1510 <= ticks - sp_ticks <= 1620:
                    SCREEN.fill(pygame.Color('Black'))
                    i = 0
                    while i < tiles:
                        SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                        SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                        SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                        SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                        i += 1
                    if revst == 0:
                        Spider_Man = pygame.image.load('Тема 247.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (162, 350))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 120))
                    else:
                        Spider_Man = pygame.image.load('Тема 246.png').convert_alpha()
                        Spider_Man = pygame.transform.scale(Spider_Man, (162, 350))
                        SCREEN.blit(Spider_Man, (SMx, SMy + 120))
                elif ticks - sp_ticks > 1620:
                    sp_ticks = ticks
                    evasion = 0

        # Реакция на удары
        # Смерть от удара в лицо
        if st == 13 and crawl_st == 0 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))
            Spider_Man = pygame.image.load('Тема 525.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 100))
        elif st == 13 and crawl_st == 1 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))
            Spider_Man = pygame.image.load('Тема 526.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 98))
        elif st == 13 and crawl_st == 2 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 527.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 98))
        elif st == 13 and crawl_st == 3 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 528.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
        elif st == 13 and crawl_st == 4 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 529.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
        elif st == 13 and crawl_st == 5 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 530.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
        elif st == 13 and crawl_st == 6 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 531.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
        elif st == 13 and crawl_st == 7 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 532.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 100))
        elif st == 13 and crawl_st == 8 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 533.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
        elif st == 13 and crawl_st == 9 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 534.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 155))
        elif st == 13 and crawl_st == 10 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 535.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 165))
        elif st == 13 and crawl_st == 11 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 536.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 195))
        elif st == 13 and crawl_st == 13 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 537.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 185))
        elif st == 13 and crawl_st == 13 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 538.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 185))
        elif st == 13 and crawl_st == 14 and spider_type_of_react == 0:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))
            Spider_Man = pygame.image.load('Тема 539.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))

        # Смерть от удара в лицо
        if st == 13 and spider_type_of_react == 0 and (0 <= ticks - sp_ticks <= 80):
            crawl_st = 0
        elif st == 13 and spider_type_of_react == 0 and (80 <= ticks - sp_ticks <= 160):
            crawl_st = 1
        elif st == 13 and spider_type_of_react == 0 and (160 <= ticks - sp_ticks <= 240):
            crawl_st = 2
        elif st == 13 and spider_type_of_react == 0 and (240 <= ticks - sp_ticks <= 320):
            crawl_st = 3
        elif st == 13 and spider_type_of_react == 0 and (320 <= ticks - sp_ticks <= 400):
            crawl_st = 4
        elif st == 13 and spider_type_of_react == 0 and (400 <= ticks - sp_ticks <= 480):
            crawl_st = 5
        elif st == 13 and spider_type_of_react == 0 and (480 <= ticks - sp_ticks <= 560):
            crawl_st = 6
        elif st == 13 and spider_type_of_react == 0 and (560 <= ticks - sp_ticks <= 640):
            crawl_st = 7
        elif st == 13 and spider_type_of_react == 0 and (640 <= ticks - sp_ticks <= 720):
            crawl_st = 8
        elif st == 13 and spider_type_of_react == 0 and (720 <= ticks - sp_ticks <= 800):
            crawl_st = 9
        elif st == 13 and spider_type_of_react == 0 and (800 <= ticks - sp_ticks <= 880):
            crawl_st = 10
        elif st == 13 and spider_type_of_react == 0 and (880 <= ticks - sp_ticks <= 960):
            crawl_st = 11
        elif st == 13 and spider_type_of_react == 0 and (960 <= ticks - sp_ticks <= 1040):
            crawl_st = 12
        elif st == 13 and spider_type_of_react == 0 and (1040 <= ticks - sp_ticks <= 1120):
            crawl_st = 13
        elif st == 13 and spider_type_of_react == 0 and (1120 <= ticks - sp_ticks <= 1200):
            crawl_st = 14
        elif st == 13 and spider_type_of_react == 0 and (ticks - sp_ticks > 1200):
            crawl_st = 0
            sp_ticks = ticks
            st = -10

        # Смерть от удара в спину
        if st == 13 and crawl_st == 0 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 570.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
        elif st == 13 and crawl_st == 1 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 571.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
        elif st == 13 and crawl_st == 2 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 572.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
        elif st == 13 and crawl_st == 3 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 573.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 150))
        elif st == 13 and crawl_st == 4 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 574.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
        elif st == 13 and crawl_st == 5 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 575.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
        elif st == 13 and crawl_st == 6 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 576.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
        elif st == 13 and crawl_st == 7 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 577.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
        elif st == 13 and crawl_st == 8 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 578.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
        elif st == 13 and crawl_st == 9 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 579.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
        elif st == 13 and crawl_st == 10 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 580.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
        elif st == 13 and crawl_st == 11 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 581.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))
        elif st == 13 and crawl_st == 13 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 582.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))
        elif st == 13 and crawl_st == 13 and spider_type_of_react == 1:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 583.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
            SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))

        # Смерть от удара в спину
        if st == 13 and spider_type_of_react == 1 and (0 <= ticks - sp_ticks <= 80):
            crawl_st = 0
            sdvigx -= 10
        elif st == 13 and spider_type_of_react == 1 and (80 <= ticks - sp_ticks <= 160):
            crawl_st = 1
            sdvigx -= 6
        elif st == 13 and spider_type_of_react == 1 and (160 <= ticks - sp_ticks <= 240):
            crawl_st = 2
            sdvigx -= 4
        elif st == 13 and spider_type_of_react == 1 and (240 <= ticks - sp_ticks <= 320):
            crawl_st = 3
            sdvigx -= 3
        elif st == 13 and spider_type_of_react == 1 and (320 <= ticks - sp_ticks <= 400):
            crawl_st = 4
            sdvigx -= 2
        elif st == 13 and spider_type_of_react == 1 and (400 <= ticks - sp_ticks <= 480):
            crawl_st = 5
            sdvigx -= 1
        elif st == 13 and spider_type_of_react == 1 and (480 <= ticks - sp_ticks <= 560):
            crawl_st = 6
            sdvigx -= 1
        elif st == 13 and spider_type_of_react == 1 and (560 <= ticks - sp_ticks <= 640):
            crawl_st = 7
            sdvigx -= 1
        elif st == 13 and spider_type_of_react == 1 and (640 <= ticks - sp_ticks <= 720):
            crawl_st = 8
        elif st == 13 and spider_type_of_react == 1 and (720 <= ticks - sp_ticks <= 800):
            crawl_st = 9
        elif st == 13 and spider_type_of_react == 1 and (800 <= ticks - sp_ticks <= 880):
            crawl_st = 10
        elif st == 13 and spider_type_of_react == 1 and (880 <= ticks - sp_ticks <= 960):
            crawl_st = 11
        elif st == 13 and spider_type_of_react == 1 and (960 <= ticks - sp_ticks <= 1040):
            crawl_st = 12
        elif st == 13 and spider_type_of_react == 1 and (1040 <= ticks - sp_ticks <= 1120):
            crawl_st = 13
        elif st == 13 and spider_type_of_react == 1 and (ticks - sp_ticks > 1120):
            crawl_st = 0
            sp_ticks = ticks

        # Реакция на удар в лицо
        if st == 13 and crawl_st == 0 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 548.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
        elif st == 13 and crawl_st == 1 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 549.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
        elif st == 13 and crawl_st == 2 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 550.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
        elif st == 13 and crawl_st == 3 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 551.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
        elif st == 13 and crawl_st == 4 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 552.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 143))
        elif st == 13 and crawl_st == 5 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 553.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))
        elif st == 13 and crawl_st == 6 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 554.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))
        elif st == 13 and crawl_st == 7 and spider_type_of_react == 2:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 555.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))

        # Реакция на удар в лицо
        if st == 13 and spider_type_of_react == 2 and (0 <= ticks - sp_ticks <= 80):
            crawl_st = 0
        elif st == 13 and spider_type_of_react == 2 and (80 <= ticks - sp_ticks <= 160):
            crawl_st = 1
        elif st == 13 and spider_type_of_react == 2 and (160 <= ticks - sp_ticks <= 240):
            crawl_st = 2
        elif st == 13 and spider_type_of_react == 2 and (240 <= ticks - sp_ticks <= 320):
            crawl_st = 3
        elif st == 13 and spider_type_of_react == 2 and (320 <= ticks - sp_ticks <= 400):
            crawl_st = 4
        elif st == 13 and spider_type_of_react == 2 and (400 <= ticks - sp_ticks <= 480):
            crawl_st = 5
        elif st == 13 and spider_type_of_react == 2 and (480 <= ticks - sp_ticks <= 560):
            crawl_st = 6
        elif st == 13 and spider_type_of_react == 2 and (560 <= ticks - sp_ticks <= 640):
            crawl_st = 7
        elif st == 13 and spider_type_of_react == 2 and (ticks - sp_ticks > 640):
            st = 2
            fight_ready_pose = 1
            type_of_hit = -1
            crawl_st = 0
            sp_ticks = ticks

        # Реакция на удар в спину
        if st == 13 and crawl_st == 0 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 592.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 1 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 593.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 2 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 594.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 3 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 595.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 4 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 596.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 5 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 597.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 6 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 598.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
        elif st == 13 and crawl_st == 7 and spider_type_of_react == 3:
            SCREEN.fill(pygame.Color('Black'))
            i = 0
            while i < tiles:
                SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
                SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
                SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
                SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
                i += 1
            if abs(sdvigx) > bg.get_width():
                sdvigx = 0
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 50, 400, 30), 3)
            pygame.draw.rect(SCREEN, (50, 191, 73), (55, 55, 390, 20))
            font = pygame.font.Font("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/Fonts"
                                    "/MonospaceBold.ttf", 25 * kx)
            text = font.render(str(health), True, pygame.Color("red"))
            tx, ty = 60, 52
            SCREEN.blit(text, (tx, ty))

            Spider_Man = pygame.image.load('Тема 599.png').convert_alpha()
            Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
            SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))

        # Реакция на удар в спину
        if st == 13 and spider_type_of_react == 3 and (0 <= ticks - sp_ticks <= 80):
            crawl_st = 0
        elif st == 13 and spider_type_of_react == 3 and (80 <= ticks - sp_ticks <= 160):
            crawl_st = 1
        elif st == 13 and spider_type_of_react == 3 and (160 <= ticks - sp_ticks <= 240):
            crawl_st = 2
        elif st == 13 and spider_type_of_react == 3 and (240 <= ticks - sp_ticks <= 320):
            crawl_st = 3
        elif st == 13 and spider_type_of_react == 3 and (320 <= ticks - sp_ticks <= 400):
            crawl_st = 4
        elif st == 13 and spider_type_of_react == 3 and (400 <= ticks - sp_ticks <= 480):
            crawl_st = 5
        elif st == 13 and spider_type_of_react == 3 and (480 <= ticks - sp_ticks <= 560):
            crawl_st = 6
        elif st == 13 and spider_type_of_react == 3 and (560 <= ticks - sp_ticks <= 640):
            crawl_st = 7
        elif st == 13 and spider_type_of_react == 3 and (ticks - sp_ticks > 640):
            st = 2
            fight_ready_pose = 1
            crawl_st = 0
            sp_ticks = ticks

        if ticks >= 2000000:
            # Fisk thug
            th_sdvigx -= sdvigx - dlt_sdvigx
            th_sdvigy -= sdvigy - dlt_sdvigy

            # Стандартная стойка
            if thug_st == 0 or thug_st == -11:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 37.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 46.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                if thug_st == -11:
                    thug_st = -12

            # print(st, crawl_st, ticks - sp_ticks)

            # Триггеры

            # Реакция на удар
            if (sdvigy <= -330 and st == 2 and ((type_of_hit == 0 and 370 <= ticks - sp_ticks <= 470)
                                                or (type_of_hit == 1 and 290 <= ticks - sp_ticks <= 490)
                                                or (type_of_hit == 2 and 290 <= ticks - sp_ticks <= 490)
                                                or (type_of_hit == 3 and 350 <= ticks - sp_ticks <= 550)
                                                or (type_of_hit == 4 and 240 <= ticks - sp_ticks <= 440)
                                                or (type_of_hit == 5 and 1100 <= ticks - sp_ticks <= 1450)
                                                or (type_of_hit == 6 and 450 <= ticks - sp_ticks <= 650))
                    and th_health - p_of_hit <= 0 and (
                            thug_type_of_react != 0 or thug_type_of_react != 1) and thug_st != -2
                    and thug_st == 0 and ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0)
                                          or (th_revst == 1 and SMx - (Thx - th_sdvigx) <= 100))):
                thug_st = 5
                thug_ticks = ticks
                th_st = 0
                th_health -= p_of_hit
                thug_type_of_react = 0  # вырубание бандита от удара в лицо
                th_death.play()
            elif (sdvigy <= -330 and st == 2 and ((type_of_hit == 0 and 370 <= ticks - sp_ticks <= 470)
                                                  or (type_of_hit == 1 and 290 <= ticks - sp_ticks <= 490)
                                                  or (type_of_hit == 2 and 290 <= ticks - sp_ticks <= 490)
                                                  or (type_of_hit == 3 and 350 <= ticks - sp_ticks <= 550)
                                                  or (type_of_hit == 4 and 240 <= ticks - sp_ticks <= 440)
                                                  or (type_of_hit == 5 and 1100 <= ticks - sp_ticks <= 1450)
                                                  or (type_of_hit == 6 and 450 <= ticks - sp_ticks <= 650))
                  and th_health - p_of_hit > 0 and (
                          thug_type_of_react != 0 or thug_type_of_react != 1) and thug_st != -2
                  and ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0)
                       or (th_revst == 1 and SMx - (Thx - th_sdvigx) <= 100))):
                thug_st = -2
                thug_ticks = ticks
                th_st = 0
                th_health -= p_of_hit
                # thug_type_of_react = random.choice([0, 1])  # реакция бандита на удар в лицо
                thug_type_of_react = 1
                hit_mix = random.choice([0, 1, 2, 3])
                if hit_mix == 0:
                    hitt.play()
                elif hit_mix == 1:
                    hit1.play()
                elif hit_mix == 2:
                    hit2.play()
                elif hit_mix == 3:
                    hit3.play()

            if ((thug_st == 1 and sdvigy <= -330 and
                 ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (
                         th_revst == 1 and SMx - (Thx - th_sdvigx) <= 100))) or
                    health <= 0):
                thug_st = 0  # Остановка
                thug_ticks = ticks
                th_delay = ticks
                th_st = 0

            if (thug_st == 0 and sdvigy <= -330 and
                    ((th_revst == 0 and SMx - (Thx - th_sdvigx) <= 0) or (
                            th_revst == 1 and SMx - (Thx - th_sdvigx) >= 100)) and
                    health > 0):
                thug_st = 1  # Бег
                thug_ticks = ticks
                th_st = 0

            if (thug_st == 0 and sdvigy <= -330
                    and ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) or (
                            th_revst == 1 and SMx - (Thx - th_sdvigx)) <= 100)
                    and health > 0):
                if ticks - th_delay > 500:
                    thug_st = 2  # Удар
                    thug_ticks = ticks
                    th_st = 0
                    thug_type_of_hit = random.choice([0, 1])

            # Бег
            if thug_st == 1 and th_st == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 1.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 9.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 2.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 10.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 2:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 3.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 11.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 3:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 4.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 12.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 4:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 5.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 13.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 5:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 6.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 14.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 6:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 7.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 15.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
            elif thug_st == 1 and th_st == 7:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 8.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 16.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))

            # Удар 1
            if thug_st == 2 and th_st == 0 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 55.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 66.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 1 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 56.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 67.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 2 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 57.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 68.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 3 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 58.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 69.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 4 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 59.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 70.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 5 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 60.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 71.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 6 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 61.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 72.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 7 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 62.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 73.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 8 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 63.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 74.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 9 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 64.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 75.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 10 and thug_type_of_hit == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 65.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 76.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))

            # Удар 2
            if thug_st == 2 and th_st == 0 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 77.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 85.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 1 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 78.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 86.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 2 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 79.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 87.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 3 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 80.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 88.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 4 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 81.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 89.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 5 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 82.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 90.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 6 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 83.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 91.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 2 and th_st == 7 and thug_type_of_hit == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 84.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 92.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))

            # Реакция на удар 1
            if thug_st == -2 and th_st == 0 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 17.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 27.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 1 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 18.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 28.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 2 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 19.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 29.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 3 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 20.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 30.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 4 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 21.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 31.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 5 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 22.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 32.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 6 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 23.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 33.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == -2 and th_st == 7 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 34.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 24.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
            elif thug_st == -2 and th_st == 6 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 25.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 35.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
            elif thug_st == -2 and th_st == 7 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 26.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 122 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 36.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 122 + th_sdvigy))

            # Реакция на удар 2
            if thug_st == -2 and th_st == 0 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 37.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 46.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 1 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 38.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 47.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 2 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 39.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 48.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 3 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 40.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 49.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 4 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 41.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 50.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 5 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 42.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 51.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 6 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 43.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 52.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 7 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 44.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 53.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == -2 and th_st == 8 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 45.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 54.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))

            # Стандартная реакция на сильный удар
            if thug_st == 3 and th_st == 0 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 93.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 108.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 1 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 94.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 109.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 2 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 95.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 110.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 3 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 96.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 111.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 4 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 97.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 112.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 5 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 98.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 113.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 6 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 99.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 114.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 7 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 100.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 115.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 8 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 101.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 116.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 8 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 102.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 117.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 9 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 103.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 118.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 10 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 104.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 119.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 335))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 11 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 105.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (375, 375))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 120.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (375, 375))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 12 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 106.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 140 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 121.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 140 + th_sdvigy))
            elif thug_st == 3 and th_st == 13 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 107.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 122.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))

            # Стандартная реакция на сильный удар 1
            if thug_st == 3 and th_st == 0 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 123.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 133.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
            elif thug_st == 3 and th_st == 1 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 124.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 134.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
            elif thug_st == 3 and th_st == 2 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 125.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 135.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 3 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 126.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 136.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 4 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 127.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 137.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 5 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 128.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 138.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 6 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 129.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 139.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 7 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 130.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 140.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
            elif thug_st == 3 and th_st == 8 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 131.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 141.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
            elif thug_st == 3 and th_st == 9 and thug_type_of_react == 1:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 132.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 145 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 142.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 145 + th_sdvigy))

            # Подъем после удара
            if thug_st == 4 and th_st == 0 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 143.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 152.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 1 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 144.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 153.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 2 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 145.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 154.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 3 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 146.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 155.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 4 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 147.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 156.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 5 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 148.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 157.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
            elif thug_st == 4 and th_st == 6 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 149.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 158.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 4 and th_st == 7 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 150.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 159.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))
            elif thug_st == 4 and th_st == 8 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 151.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 160.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))

            # Вырубание
            if thug_st == 5 and th_st == 0 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 161.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 115 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 175.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 115 + th_sdvigy))
            elif thug_st == 5 and th_st == 1 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 162.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 176.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
            elif thug_st == 5 and th_st == 2 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 163.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 177.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
            elif thug_st == 5 and th_st == 3 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 164.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 178.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
            elif thug_st == 5 and th_st == 4 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 165.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 179.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
            elif thug_st == 5 and th_st == 5 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 166.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 180.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
            elif thug_st == 5 and th_st == 6 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 167.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 45 - th_sdvigx, Thy + 160 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 181.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
                    SCREEN.blit(Fisk_thug, (Thx + 45 - th_sdvigx, Thy + 160 + th_sdvigy))
            elif thug_st == 5 and th_st == 7 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 168.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 182.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 5 and th_st == 8 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 169.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 10 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 183.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 10 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 5 and th_st == 8 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 170.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 184.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 5 and th_st == 9 and thug_type_of_react == 0:

                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 171.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 185.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 5 and th_st == 10 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 172.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 186.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif thug_st == 5 and th_st == 11 and thug_type_of_react == 0:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 173.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 187.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
            elif (thug_st == 5 and th_st == 12 and thug_type_of_react == 0) or thug_st == -10:
                if th_revst == 0:
                    Fisk_thug = pygame.image.load('Тима 174.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
                else:
                    Fisk_thug = pygame.image.load('Тима 188.png').convert_alpha()
                    Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
                    SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))

            # Бег
            if thug_st == 1 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (480 <= ticks - thug_ticks <= 560):
                th_st = 7
                if th_revst == 0:
                    th_sdvigx += 6
                else:
                    th_sdvigx -= 6
            elif thug_st == 1 and (ticks - thug_ticks > 560):
                th_st = 0
                thug_ticks = ticks

            # Удар 1
            if thug_st == 2 and thug_type_of_hit == 0 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx += 1
                else:
                    th_sdvigx -= 1
            elif thug_st == 2 and thug_type_of_hit == 0 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx += 1
                else:
                    th_sdvigx -= 1
            elif thug_st == 2 and thug_type_of_hit == 0 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
            elif thug_st == 2 and thug_type_of_hit == 0 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
            elif thug_st == 2 and thug_type_of_hit == 0 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == 2 and thug_type_of_hit == 0 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
            elif thug_st == 2 and thug_type_of_hit == 0 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
            elif thug_st == 2 and thug_type_of_hit == 0 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
            elif thug_st == 2 and thug_type_of_hit == 0 and (640 <= ticks - thug_ticks <= 720):
                th_st = 8
            elif thug_st == 2 and thug_type_of_hit == 0 and (720 <= ticks - thug_ticks <= 800):
                th_st = 9
            elif thug_st == 2 and thug_type_of_hit == 0 and (800 <= ticks - thug_ticks <= 880):
                th_st = 10
            elif thug_st == 2 and thug_type_of_hit == 0 and (ticks - thug_ticks > 880):
                thug_st = 0
                th_st = 0
                thug_ticks = ticks
                th_delay = ticks

            # Удар 2
            if thug_st == 2 and thug_type_of_hit == 1 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx += 1
                else:
                    th_sdvigx -= 1
            elif thug_st == 2 and thug_type_of_hit == 1 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
            elif thug_st == 2 and thug_type_of_hit == 1 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
            elif thug_st == 2 and thug_type_of_hit == 1 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
            elif thug_st == 2 and thug_type_of_hit == 1 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == 2 and thug_type_of_hit == 1 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
            elif thug_st == 2 and thug_type_of_hit == 1 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
            elif thug_st == 2 and thug_type_of_hit == 1 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
            elif thug_st == 2 and thug_type_of_hit == 1 and (ticks - thug_ticks > 640):
                thug_st = 0
                th_st = 0
                thug_ticks = ticks
                th_delay = ticks

            # Реакция на удар 1
            if thug_st == -2 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx -= 3
                else:
                    th_sdvigx += 3
            elif thug_st == -2 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx -= 2
                else:
                    th_sdvigx += 2
            elif thug_st == -2 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
            elif thug_st == -2 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
            elif thug_st == -2 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == -2 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
            elif thug_st == -2 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
            elif thug_st == -2 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
            elif thug_st == -2 and thug_type_of_react == 0 and (ticks - thug_ticks > 640):
                thug_st = 0
                th_st = 0
                thug_ticks = ticks

            # Реакция на удар 2
            if thug_st == -2 and thug_type_of_react == 1 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx -= 2
                else:
                    th_sdvigx += 2
            elif thug_st == -2 and thug_type_of_react == 1 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
            elif thug_st == -2 and thug_type_of_react == 1 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
            elif thug_st == -2 and thug_type_of_react == 1 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
            elif thug_st == -2 and thug_type_of_react == 1 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == -2 and thug_type_of_react == 1 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
            elif thug_st == -2 and thug_type_of_react == 1 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
            elif thug_st == -2 and thug_type_of_react == 1 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
            elif thug_st == -2 and thug_type_of_react == 1 and (640 <= ticks - thug_ticks <= 720):
                th_st = 8
            elif thug_st == -2 and thug_type_of_react == 1 and (ticks - thug_ticks > 720):
                thug_st = 0
                th_st = 0
                thug_ticks = ticks

            # Стандартная реакция на сильный удар
            if thug_st == 3 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
            elif thug_st == 3 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
            elif thug_st == 3 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
            elif thug_st == 3 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
            elif thug_st == 3 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == 3 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 3 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 3 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
                if th_revst == 0:
                    th_sdvigx -= 4
                else:
                    th_sdvigx += 4
            elif thug_st == 3 and thug_type_of_react == 0 and (640 <= ticks - thug_ticks <= 720):
                th_st = 8
                if th_revst == 0:
                    th_sdvigx -= 3
                else:
                    th_sdvigx += 3
            elif thug_st == 3 and thug_type_of_react == 0 and (720 <= ticks - thug_ticks <= 800):
                th_st = 9
                if th_revst == 0:
                    th_sdvigx -= 2
                else:
                    th_sdvigx += 2
            elif thug_st == 3 and thug_type_of_react == 0 and (800 <= ticks - thug_ticks <= 880):
                th_st = 10
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
            elif thug_st == 3 and thug_type_of_react == 0 and (880 <= ticks - thug_ticks <= 960):
                th_st = 11
            elif thug_st == 3 and thug_type_of_react == 0 and (960 <= ticks - thug_ticks <= 1040):
                th_st = 12
            elif thug_st == 3 and thug_type_of_react == 0 and (1040 <= ticks - thug_ticks <= 1120):
                th_st = 13
            elif thug_st == 3 and thug_type_of_react == 0 and (ticks - thug_ticks > 2500):
                th_st = 0
                thug_ticks = ticks

            # Стандартная реакция на сильный удар 1
            if thug_st == 3 and thug_type_of_react == 1 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 3 and thug_type_of_react == 1 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 3 and thug_type_of_react == 1 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 3 and thug_type_of_react == 1 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
                if th_revst == 0:
                    th_sdvigx -= 4
                else:
                    th_sdvigx += 4
            elif thug_st == 3 and thug_type_of_react == 1 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
                if th_revst == 0:
                    th_sdvigx -= 4
                else:
                    th_sdvigx += 4
            elif thug_st == 3 and thug_type_of_react == 1 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
                if th_revst == 0:
                    th_sdvigx -= 3
                else:
                    th_sdvigx += 3
            elif thug_st == 3 and thug_type_of_react == 1 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
                if th_revst == 0:
                    th_sdvigx -= 2
                else:
                    th_sdvigx += 2
            elif thug_st == 3 and thug_type_of_react == 1 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
                if th_revst == 0:
                    th_sdvigx -= 1
                else:
                    th_sdvigx += 1
                th_sdvigx += 1
            elif thug_st == 3 and thug_type_of_react == 1 and (640 <= ticks - thug_ticks <= 720):
                th_st = 8
            elif thug_st == 3 and thug_type_of_react == 1 and (720 <= ticks - thug_ticks <= 800):
                th_st = 9
            elif thug_st == 3 and thug_type_of_react == 1 and (ticks - thug_ticks > 800):
                th_st = 0
                thug_ticks = ticks

            # Подъем после удара
            if thug_st == 4 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
            elif thug_st == 4 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
            elif thug_st == 4 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
            elif thug_st == 4 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
            elif thug_st == 4 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
            elif thug_st == 4 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
            elif thug_st == 4 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
            elif thug_st == 4 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
            elif thug_st == 4 and thug_type_of_react == 0 and (640 <= ticks - thug_ticks <= 820):
                th_st = 8
            elif thug_st == 4 and thug_type_of_react == 0 and (ticks - thug_ticks > 820):
                thug_st = 0
                th_st = 0
                thug_ticks = ticks

            # Вырубание
            if thug_st == 5 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
                th_st = 0
            elif thug_st == 5 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
                th_st = 1
                if th_revst == 0:
                    th_sdvigx -= 15
                else:
                    th_sdvigx += 15
            elif thug_st == 5 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
                th_st = 2
                if th_revst == 0:
                    th_sdvigx -= 12
                else:
                    th_sdvigx += 12
            elif thug_st == 5 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
                th_st = 3
                if th_revst == 0:
                    th_sdvigx -= 12
                else:
                    th_sdvigx += 12
            elif thug_st == 5 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
                th_st = 4
                if th_revst == 0:
                    th_sdvigx -= 9
                else:
                    th_sdvigx += 9
            elif thug_st == 5 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
                th_st = 5
                if th_revst == 0:
                    th_sdvigx -= 9
                else:
                    th_sdvigx += 9
            elif thug_st == 5 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
                th_st = 6
                if th_revst == 0:
                    th_sdvigx -= 7
                else:
                    th_sdvigx += 7
            elif thug_st == 5 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
                th_st = 7
                if th_revst == 0:
                    th_sdvigx -= 5
                else:
                    th_sdvigx += 5
            elif thug_st == 5 and thug_type_of_react == 0 and (640 <= ticks - thug_ticks <= 720):
                th_st = 8
            elif thug_st == 5 and thug_type_of_react == 0 and (720 <= ticks - thug_ticks <= 800):
                th_st = 9
            elif thug_st == 5 and thug_type_of_react == 0 and (800 <= ticks - thug_ticks <= 880):
                th_st = 10
            elif thug_st == 5 and thug_type_of_react == 0 and (880 <= ticks - thug_ticks <= 960):
                th_st = 11
            elif thug_st == 5 and thug_type_of_react == 0 and (960 <= ticks - thug_ticks <= 1040):
                th_st = 12
            elif thug_st == 5 and thug_type_of_react == 0 and (ticks - thug_ticks > 1040):
                thug_st = -10  # лежит
                st = 2
                fight_ready_pose = 1
                th_st = 0
                thug_ticks = sp_ticks = ticks

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print(sdvigx, sdvigy)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                pygame.mixer.music.unload()
                menu()




main_menu()
