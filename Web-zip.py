import random

import pygame
import math

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
thug_st = 0
th_st = 0
sp_ticks = 0
thug_ticks = 0
bg = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                       "Textures/fhomewthspandpavmnt.jpg").convert()
bg = pygame.transform.scale(bg, (1414, 2000))
road = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                         "Textures/дорога.jpeg").convert()
road = pygame.transform.scale(road, (2011, 354))
sdvigx = 0
sdvigy = -330
th_sdvigx = 0
th_sdvigy = 0
thug_type_of_hit = 0
thug_type_of_react = 0
podst = 0
revst = 0
tiles = math.ceil(display_w / bg.get_width()) + 1
i = 0
running = True

# display_w, display_h = pygame.display.Info().current_w, pygame.display.Info().current_h
# time_wait = 0
# ticks, sp_ticks, podst, zvukst, thwipsound, dif_image, dif_image_m, hp = 0, 0, 0, 0, 0, 0, 0, 100
# colors = [(127, 127, 127), (210, 150, 75), (200, 190, 140), (200, 190, 140)]
# tx, sdvigx, sdvigy, coords_increase, SMXstart, SMYstart = 0, -500, 0, 0, 0, 0
# fight, ftticks = 0, 0
# sdvigxconst, sdvigyconst, revk, revst, f_t_colors, f_t_coords = 0, 0, 0, 0, [], []
# hcolors, hcoords, hsize, length_ofr = [], [], [], 0
# SMw, SMh = 160, 200
SMx, SMy = display_w // 2 - 150 + 15, display_h // 2 - 200 + 7
Thx, Thy = display_w // 2 + 150 + 15, display_h // 2 - 200 + 7
# SMXstart, SMYstart = 0, 0
# SMRt, srt = -50, -40
# coords_increase, sdvigxconst, sdvigyconst, zvukst = 0, 0, 0, 0


while running:
    ticks = pygame.time.get_ticks()

# Стандартная стойка
    if thug_st == 0 and sdvigy <= -330 \
            and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Fisk_thug = pygame.image.load('Тима 37.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


# Триггеры
    if thug_st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_a]:
        thug_st = 1  # Бег
        thug_ticks = ticks
        th_st = 0

    if thug_st == 1 and sdvigy <= -330 and not pygame.key.get_pressed()[pygame.K_a]:
        thug_st = 0  # Остановка
        thug_ticks = ticks
        th_st = 0

    if thug_st == 0 and sdvigy <= -330 and pygame.mouse.get_pressed() == (True, False, False):
        # thug_st = 2  # Удар
        # thug_ticks = ticks
        # th_st = 0
        # #thug_type_of_hit = random.randint(0, 1)
        # thug_type_of_hit = 1
        thug_st = 5  #
        thug_ticks = ticks
        th_st = 0
        # thug_type_of_react = random.randint(0, 1)
        thug_type_of_react = 0


# Бег
    if thug_st == 1 and th_st == 0 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 1.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 1 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 2.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 2 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 3.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 3 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 4.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 4 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 5.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 5 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 6.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 6 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 7.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))
    elif thug_st == 1 and th_st == 7 and pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 8.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 103 + th_sdvigy))


# Удар 1
    if thug_st == 2 and th_st == 0 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 55.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 1 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 56.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 2 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 57.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 3 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 58.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 4 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 59.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 5 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 60.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 6 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 61.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 7 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 62.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 8 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 63.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 9 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 64.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 10 and thug_type_of_hit == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 65.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))


# Удар 2
    if thug_st == 2 and th_st == 0 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 77.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 1 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 78.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 2 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 79.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 3 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 80.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 4 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 81.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 5 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 82.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 6 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 83.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 2 and th_st == 7 and thug_type_of_hit == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 84.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))


# Реакция на удар 1
    if thug_st == -2 and th_st == 0 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 17.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 1 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 18.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 2 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 19.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 3 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 20.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 4 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 21.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 5 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 22.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 6 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 23.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == -2 and th_st == 7 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 24.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
    elif thug_st == -2 and th_st == 6 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 25.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 121 + th_sdvigy))
    elif thug_st == -2 and th_st == 7 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 26.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 122 + th_sdvigy))


# Реакция на удар 2
    if thug_st == -2 and th_st == 0 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 37.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 1 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 38.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 2 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 39.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 3 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 40.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 4 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 41.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 5 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 42.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 6 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 43.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 7 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 44.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == -2 and th_st == 8 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 45.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (360, 370))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))


# Стандартная реакция на сильный удар
    if thug_st == 3 and th_st == 0 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 93.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 1 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 94.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 2 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 95.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 3 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 96.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 4 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 97.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 5 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 98.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 6 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 99.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 7 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 100.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 8 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 101.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 8 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 102.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 9 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 103.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 10 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 104.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 335))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 11 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 105.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (375, 375))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 12 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 106.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 140 + th_sdvigy))
    elif thug_st == 3 and th_st == 13 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 107.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (395, 395))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))


# Стандартная реакция на сильный удар 1
    if thug_st == 3 and th_st == 0 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 123.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 108 + th_sdvigy))
    elif thug_st == 3 and th_st == 1 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 124.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 120 + th_sdvigy))
    elif thug_st == 3 and th_st == 2 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 125.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 3 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 126.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 4 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 127.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 5 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 128.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 6 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 129.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 7 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 130.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 130 + th_sdvigy))
    elif thug_st == 3 and th_st == 8 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 131.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
    elif thug_st == 3 and th_st == 9 and thug_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 132.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 315))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 145 + th_sdvigy))


# Подъем после удара
    if thug_st == 4 and th_st == 0 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 143.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 1 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 144.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 2 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 145.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 3 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 146.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 4 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 147.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 5 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 148.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 175 + th_sdvigy))
    elif thug_st == 4 and th_st == 6 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 149.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (325, 325))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 4 and th_st == 7 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 150.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))
    elif thug_st == 4 and th_st == 8 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 151.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (340, 360))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 105 + th_sdvigy))


# Вырубание
    if thug_st == 5 and th_st == 0 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 161.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 115 + th_sdvigy))
    elif thug_st == 5 and th_st == 1 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 162.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
    elif thug_st == 5 and th_st == 2 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 163.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
    elif thug_st == 5 and th_st == 3 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 164.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
    elif thug_st == 5 and th_st == 4 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 165.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (310, 320))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 125 + th_sdvigy))
    elif thug_st == 5 and th_st == 5 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 166.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 135 + th_sdvigy))
    elif thug_st == 5 and th_st == 6 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 167.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (320, 330))
        SCREEN.blit(Fisk_thug, (Thx + 45 - th_sdvigx, Thy + 160 + th_sdvigy))
    elif thug_st == 5 and th_st == 7 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 168.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 8 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 169.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 10 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 8 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 170.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 9 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 171.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 10 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 172.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 11 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 173.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))
    elif thug_st == 5 and th_st == 12 and thug_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Fisk_thug = pygame.image.load('Тима 174.png').convert_alpha()
        Fisk_thug = pygame.transform.scale(Fisk_thug, (330, 340))
        SCREEN.blit(Fisk_thug, (Thx + 27 - th_sdvigx, Thy + 170 + th_sdvigy))


# Бег
    if thug_st == 1 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
        th_sdvigx += 6
    elif thug_st == 1 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx += 6
    elif thug_st == 1 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx += 6
    elif thug_st == 1 and (240 <= ticks - thug_ticks <= 320):
        th_st = 3
        th_sdvigx += 6
    elif thug_st == 1 and (320 <= ticks - thug_ticks <= 400):
        th_st = 4
        th_sdvigx += 6
    elif thug_st == 1 and (400 <= ticks - thug_ticks <= 480):
        th_st = 5
        th_sdvigx += 6
    elif thug_st == 1 and (480 <= ticks - thug_ticks <= 560):
        th_st = 6
        th_sdvigx += 6
    elif thug_st == 1 and (480 <= ticks - thug_ticks <= 560):
        th_st = 7
        th_sdvigx += 6
    elif thug_st == 1 and (ticks - thug_ticks > 560):
        th_st = 0
        thug_ticks = ticks


# Удар 1
    if thug_st == 2 and thug_type_of_hit == 0 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
        th_sdvigx += 1
    elif thug_st == 2 and thug_type_of_hit == 0 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx += 1
    elif thug_st == 2 and thug_type_of_hit == 0 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx += 1
    elif thug_st == 2 and thug_type_of_hit == 0 and (240 <= ticks - thug_ticks <= 320):
        th_st = 3
        th_sdvigx += 1
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
        th_st = 0
        thug_ticks = ticks


# Удар 2
    if thug_st == 2 and thug_type_of_hit == 1 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
        th_sdvigx += 1
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
        th_st = 0
        thug_ticks = ticks


# Реакция на удар 1
    if thug_st == -2 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
        th_sdvigx -= 3
    elif thug_st == -2 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx -= 2
    elif thug_st == -2 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx -= 1
    elif thug_st == -2 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
        th_st = 3
        th_sdvigx -= 1
    elif thug_st == -2 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
        th_st = 4
    elif thug_st == -2 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
        th_st = 5
    elif thug_st == -2 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
        th_st = 6
    elif thug_st == -2 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
        th_st = 7
    elif thug_st == -2 and thug_type_of_react == 0 and (ticks - thug_ticks > 640):
        th_st = 0
        thug_ticks = ticks


# Реакция на удар 2
    if thug_st == -2 and thug_type_of_react == 1 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
        th_sdvigx -= 2
    elif thug_st == -2 and thug_type_of_react == 1 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx -= 1
    elif thug_st == -2 and thug_type_of_react == 1 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx -= 1
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
        th_sdvigx -= 5
    elif thug_st == 3 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
        th_st = 6
        th_sdvigx -= 5
    elif thug_st == 3 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
        th_st = 7
        th_sdvigx -= 4
    elif thug_st == 3 and thug_type_of_react == 0 and (640 <= ticks - thug_ticks <= 720):
        th_st = 8
        th_sdvigx -= 3
    elif thug_st == 3 and thug_type_of_react == 0 and (720 <= ticks - thug_ticks <= 800):
        th_st = 9
        th_sdvigx -= 2
    elif thug_st == 3 and thug_type_of_react == 0 and (800 <= ticks - thug_ticks <= 880):
        th_st = 10
        th_sdvigx -= 1
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
        th_sdvigx -= 5
    elif thug_st == 3 and thug_type_of_react == 1 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx -= 5
    elif thug_st == 3 and thug_type_of_react == 1 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx -= 5
    elif thug_st == 3 and thug_type_of_react == 1 and (240 <= ticks - thug_ticks <= 320):
        th_st = 3
        th_sdvigx -= 4
    elif thug_st == 3 and thug_type_of_react == 1 and (320 <= ticks - thug_ticks <= 400):
        th_st = 4
        th_sdvigx -= 4
    elif thug_st == 3 and thug_type_of_react == 1 and (400 <= ticks - thug_ticks <= 480):
        th_st = 5
        th_sdvigx -= 3
    elif thug_st == 3 and thug_type_of_react == 1 and (480 <= ticks - thug_ticks <= 560):
        th_st = 6
        th_sdvigx -= 2
    elif thug_st == 3 and thug_type_of_react == 1 and (560 <= ticks - thug_ticks <= 640):
        th_st = 7
        th_sdvigx -= 1
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
        th_st = 0
        thug_ticks = ticks


# Вырубание
    if thug_st == 5 and thug_type_of_react == 0 and (0 <= ticks - thug_ticks <= 80):
        th_st = 0
    elif thug_st == 5 and thug_type_of_react == 0 and (80 <= ticks - thug_ticks <= 160):
        th_st = 1
        th_sdvigx -= 15
    elif thug_st == 5 and thug_type_of_react == 0 and (160 <= ticks - thug_ticks <= 240):
        th_st = 2
        th_sdvigx -= 12
    elif thug_st == 5 and thug_type_of_react == 0 and (240 <= ticks - thug_ticks <= 320):
        th_st = 3
        th_sdvigx -= 12
    elif thug_st == 5 and thug_type_of_react == 0 and (320 <= ticks - thug_ticks <= 400):
        th_st = 4
        th_sdvigx -= 9
    elif thug_st == 5 and thug_type_of_react == 0 and (400 <= ticks - thug_ticks <= 480):
        th_st = 5
        th_sdvigx -= 9
    elif thug_st == 5 and thug_type_of_react == 0 and (480 <= ticks - thug_ticks <= 560):
        th_st = 6
        th_sdvigx -= 7
    elif thug_st == 5 and thug_type_of_react == 0 and (560 <= ticks - thug_ticks <= 640):
        th_st = 7
        th_sdvigx -= 5
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
        th_st = 0
        thug_ticks = ticks


    # SCREEN.fill(pygame.Color('Black'))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

