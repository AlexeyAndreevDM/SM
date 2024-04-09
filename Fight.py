import pygame
import math
import random

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
dlt_sdvigx = 0
dlt_sdvigy = 0
th_sdvigx = 0
th_sdvigy = 0
thug_type_of_hit = 0
thug_type_of_react = 0
th_revst = 0
th_delay = 0
hit = 0
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
tiles = math.ceil(display_w / bg.get_width()) + 1
i = 0
running = True
fight_ready = 0
fight_ready_pose = 0
l_hit, r_hit = 0, 0
type_of_evasion = 0
health = 100
harm = 20
th_health = 100
p_of_hit = 5
evasion = 0
crawl_st, dcrawl_st = 0, 0
spider_type_of_react = 0
type_of_hit = 0

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

    dlt_sdvigx, dlt_sdvigy = sdvigx, sdvigy

    if st == 0 and sdvigy <= -330 and (0 <= ticks - sp_ticks <= 5000) \
            and not pygame.key.get_pressed()[pygame.K_j] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_k] and pygame.mouse.get_pressed() == (False, False, False):
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))


    elif st == 0 and sdvigy <= -330 and (5000 <= ticks - sp_ticks <= 10000) \
            and not pygame.key.get_pressed()[pygame.K_k] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_j] and pygame.mouse.get_pressed() == (False, False, False):
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 22.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))


    elif st == 0 and sdvigy <= -330 and (ticks - sp_ticks >= 10000 or sp_ticks == 0) \
            and not pygame.key.get_pressed()[pygame.K_j] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_k] and pygame.mouse.get_pressed() == (False, False, False):
        sp_ticks = ticks

    # Триггеры

    # Реакция на удар
    if (sdvigy <= -330 and ((thug_st == 2 and th_st == 3 and thug_type_of_hit == 0)
                            or thug_st == 2 and th_st == 3 and thug_type_of_hit == 1) and health - harm <= 0
        and spider_type_of_react != 0) and st != 12:
        st = 12
        sp_ticks = ticks
        crawl_st = 0
        health -= harm
        spider_type_of_react = 0  # смерть от удара в лицо
        thug_st = -11
    elif (sdvigy <= -330 and ((thug_st == 2 and th_st == 3 and thug_type_of_hit == 0)
                              or thug_st == 2 and th_st == 3 and thug_type_of_hit == 1) and health - harm >= 0
          and st != 12):
        st = 12
        sp_ticks = ticks
        crawl_st = 0
        health -= harm
        spider_type_of_react = 2  # реакция на удар в лицо

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
    if st == 12 and crawl_st == 0 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 525.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 100))
    elif st == 12 and crawl_st == 1 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 526.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 98))
    elif st == 12 and crawl_st == 2 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 527.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 98))
    elif st == 12 and crawl_st == 3 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 528.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
    elif st == 12 and crawl_st == 4 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 529.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
    elif st == 12 and crawl_st == 5 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 530.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
    elif st == 12 and crawl_st == 6 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 531.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 95))
    elif st == 12 and crawl_st == 7 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 532.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 100))
    elif st == 12 and crawl_st == 8 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 533.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
    elif st == 12 and crawl_st == 9 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 534.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 155))
    elif st == 12 and crawl_st == 10 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 535.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 165))
    elif st == 12 and crawl_st == 11 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 536.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 195))
    elif st == 12 and crawl_st == 12 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 537.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 400))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 185))
    elif st == 12 and crawl_st == 13 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 538.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 185))
    elif st == 12 and crawl_st == 14 and spider_type_of_react == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 539.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (400, 395))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))

    # Смерть от удара в лицо
    if st == 12 and spider_type_of_react == 0 and (0 <= ticks - sp_ticks <= 80):
        crawl_st = 0
    elif st == 12 and spider_type_of_react == 0 and (80 <= ticks - sp_ticks <= 160):
        crawl_st = 1
    elif st == 12 and spider_type_of_react == 0 and (160 <= ticks - sp_ticks <= 240):
        crawl_st = 2
    elif st == 12 and spider_type_of_react == 0 and (240 <= ticks - sp_ticks <= 320):
        crawl_st = 3
    elif st == 12 and spider_type_of_react == 0 and (320 <= ticks - sp_ticks <= 400):
        crawl_st = 4
    elif st == 12 and spider_type_of_react == 0 and (400 <= ticks - sp_ticks <= 480):
        crawl_st = 5
    elif st == 12 and spider_type_of_react == 0 and (480 <= ticks - sp_ticks <= 560):
        crawl_st = 6
    elif st == 12 and spider_type_of_react == 0 and (560 <= ticks - sp_ticks <= 640):
        crawl_st = 7
    elif st == 12 and spider_type_of_react == 0 and (640 <= ticks - sp_ticks <= 720):
        crawl_st = 8
    elif st == 12 and spider_type_of_react == 0 and (720 <= ticks - sp_ticks <= 800):
        crawl_st = 9
    elif st == 12 and spider_type_of_react == 0 and (800 <= ticks - sp_ticks <= 880):
        crawl_st = 10
    elif st == 12 and spider_type_of_react == 0 and (880 <= ticks - sp_ticks <= 960):
        crawl_st = 11
    elif st == 12 and spider_type_of_react == 0 and (960 <= ticks - sp_ticks <= 1040):
        crawl_st = 12
    elif st == 12 and spider_type_of_react == 0 and (1040 <= ticks - sp_ticks <= 1120):
        crawl_st = 13
    elif st == 12 and spider_type_of_react == 0 and (1120 <= ticks - sp_ticks <= 1200):
        crawl_st = 14
    elif st == 12 and spider_type_of_react == 0 and (ticks - sp_ticks > 1200):
        crawl_st = 0
        sp_ticks = ticks
        st = -1

    # Смерть от удара в спину
    if st == 12 and crawl_st == 0 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 570.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
    elif st == 12 and crawl_st == 1 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 571.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
    elif st == 12 and crawl_st == 2 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 572.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 120))
    elif st == 12 and crawl_st == 3 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 573.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 150))
    elif st == 12 and crawl_st == 4 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 574.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
    elif st == 12 and crawl_st == 5 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 575.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
    elif st == 12 and crawl_st == 6 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 576.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
    elif st == 12 and crawl_st == 7 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 577.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 190))
    elif st == 12 and crawl_st == 8 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 578.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
    elif st == 12 and crawl_st == 9 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 579.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
    elif st == 12 and crawl_st == 10 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 580.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 200))
    elif st == 12 and crawl_st == 11 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 581.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))
    elif st == 12 and crawl_st == 12 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 582.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))
    elif st == 12 and crawl_st == 13 and spider_type_of_react == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 583.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (355, 355))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 230))

    # Смерть от удара в спину
    if st == 12 and spider_type_of_react == 1 and (0 <= ticks - sp_ticks <= 80):
        crawl_st = 0
        sdvigx -= 10
    elif st == 12 and spider_type_of_react == 1 and (80 <= ticks - sp_ticks <= 160):
        crawl_st = 1
        sdvigx -= 6
    elif st == 12 and spider_type_of_react == 1 and (160 <= ticks - sp_ticks <= 240):
        crawl_st = 2
        sdvigx -= 4
    elif st == 12 and spider_type_of_react == 1 and (240 <= ticks - sp_ticks <= 320):
        crawl_st = 3
        sdvigx -= 3
    elif st == 12 and spider_type_of_react == 1 and (320 <= ticks - sp_ticks <= 400):
        crawl_st = 4
        sdvigx -= 2
    elif st == 12 and spider_type_of_react == 1 and (400 <= ticks - sp_ticks <= 480):
        crawl_st = 5
        sdvigx -= 1
    elif st == 12 and spider_type_of_react == 1 and (480 <= ticks - sp_ticks <= 560):
        crawl_st = 6
        sdvigx -= 1
    elif st == 12 and spider_type_of_react == 1 and (560 <= ticks - sp_ticks <= 640):
        crawl_st = 7
        sdvigx -= 1
    elif st == 12 and spider_type_of_react == 1 and (640 <= ticks - sp_ticks <= 720):
        crawl_st = 8
    elif st == 12 and spider_type_of_react == 1 and (720 <= ticks - sp_ticks <= 800):
        crawl_st = 9
    elif st == 12 and spider_type_of_react == 1 and (800 <= ticks - sp_ticks <= 880):
        crawl_st = 10
    elif st == 12 and spider_type_of_react == 1 and (880 <= ticks - sp_ticks <= 960):
        crawl_st = 11
    elif st == 12 and spider_type_of_react == 1 and (960 <= ticks - sp_ticks <= 1040):
        crawl_st = 12
    elif st == 12 and spider_type_of_react == 1 and (1040 <= ticks - sp_ticks <= 1120):
        crawl_st = 13
    elif st == 12 and spider_type_of_react == 1 and (ticks - sp_ticks > 1120):
        crawl_st = 0
        sp_ticks = ticks

    # Реакция на удар в лицо
    if st == 12 and crawl_st == 0 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 548.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
    elif st == 12 and crawl_st == 1 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 549.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
    elif st == 12 and crawl_st == 2 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 550.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
    elif st == 12 and crawl_st == 3 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 551.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 140))
    elif st == 12 and crawl_st == 4 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 552.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 143))
    elif st == 12 and crawl_st == 5 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 553.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))
    elif st == 12 and crawl_st == 6 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 554.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))
    elif st == 12 and crawl_st == 7 and spider_type_of_react == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 555.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 310))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 145))

    # Реакция на удар в лицо
    if st == 12 and spider_type_of_react == 2 and (0 <= ticks - sp_ticks <= 80):
        crawl_st = 0
    elif st == 12 and spider_type_of_react == 2 and (80 <= ticks - sp_ticks <= 160):
        crawl_st = 1
    elif st == 12 and spider_type_of_react == 2 and (160 <= ticks - sp_ticks <= 240):
        crawl_st = 2
    elif st == 12 and spider_type_of_react == 2 and (240 <= ticks - sp_ticks <= 320):
        crawl_st = 3
    elif st == 12 and spider_type_of_react == 2 and (320 <= ticks - sp_ticks <= 400):
        crawl_st = 4
    elif st == 12 and spider_type_of_react == 2 and (400 <= ticks - sp_ticks <= 480):
        crawl_st = 5
    elif st == 12 and spider_type_of_react == 2 and (480 <= ticks - sp_ticks <= 560):
        crawl_st = 6
    elif st == 12 and spider_type_of_react == 2 and (560 <= ticks - sp_ticks <= 640):
        crawl_st = 7
    elif st == 12 and spider_type_of_react == 2 and (ticks - sp_ticks > 640):
        st = 2
        fight_ready_pose = 0
        crawl_st = 0
        sp_ticks = ticks

    # Реакция на удар в спину
    if st == 12 and crawl_st == 0 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 592.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 1 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 593.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 2 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 594.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 3 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 595.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 4 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 596.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 5 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 597.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 6 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 598.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))
    elif st == 12 and crawl_st == 7 and spider_type_of_react == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(sky, (sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            SCREEN.blit(sky, (-sky.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy - 1000))
            SCREEN.blit(bg, (-bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (-road.get_width() * i + sdvigx, 800 + sdvigy))
            SCREEN.blit(ground, (-ground.get_width() * i + sdvigx, 800 + sdvigy + 335))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 599.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 320))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 133))

    # Реакция на удар в спину
    if st == 12 and spider_type_of_react == 3 and (0 <= ticks - sp_ticks <= 80):
        crawl_st = 0
    elif st == 12 and spider_type_of_react == 3 and (80 <= ticks - sp_ticks <= 160):
        crawl_st = 1
    elif st == 12 and spider_type_of_react == 3 and (160 <= ticks - sp_ticks <= 240):
        crawl_st = 2
    elif st == 12 and spider_type_of_react == 3 and (240 <= ticks - sp_ticks <= 320):
        crawl_st = 3
    elif st == 12 and spider_type_of_react == 3 and (320 <= ticks - sp_ticks <= 400):
        crawl_st = 4
    elif st == 12 and spider_type_of_react == 3 and (400 <= ticks - sp_ticks <= 480):
        crawl_st = 5
    elif st == 12 and spider_type_of_react == 3 and (480 <= ticks - sp_ticks <= 560):
        crawl_st = 6
    elif st == 12 and spider_type_of_react == 3 and (560 <= ticks - sp_ticks <= 640):
        crawl_st = 7
    elif st == 12 and spider_type_of_react == 3 and (ticks - sp_ticks > 640):
        st = 2
        fight_ready_pose = 1
        crawl_st = 0
        sp_ticks = ticks

    # Fisk thug
    if ticks >= 0:
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

        print(st, crawl_st, ticks - sp_ticks)

        # Триггеры

        # Реакция на удар
        if (sdvigy <= -330 and st == 2 and ((type_of_hit == 0 and 370 <= ticks - sp_ticks <= 470)
                                            or (type_of_hit == 1 and 290 <= ticks - sp_ticks <= 490)
                                            or (type_of_hit == 2 and 290 <= ticks - sp_ticks <= 490)
                                            or (type_of_hit == 3 and 350 <= ticks - sp_ticks <= 550)
                                            or (type_of_hit == 4 and 240 <= ticks - sp_ticks <= 440)
                                            or (type_of_hit == 5 and 1100 <= ticks - sp_ticks <= 1450)
                                            or (type_of_hit == 6 and 450 <= ticks - sp_ticks <= 650))
                and th_health - p_of_hit <= 0 and (thug_type_of_react != 0 or thug_type_of_react != 1) and thug_st != -2
                and thug_st == 0 and ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0)
                                      or (th_revst == 1 and SMx - (Thx - th_sdvigx) <= 100))):
            thug_st = 5
            thug_ticks = ticks
            th_st = 0
            th_health -= p_of_hit
            thug_type_of_react = 0  # вырубание бандита от удара в лицо
        elif (sdvigy <= -330 and st == 2 and ((type_of_hit == 0 and 370 <= ticks - sp_ticks <= 470)
                                              or (type_of_hit == 1 and 290 <= ticks - sp_ticks <= 490)
                                              or (type_of_hit == 2 and 290 <= ticks - sp_ticks <= 490)
                                              or (type_of_hit == 3 and 350 <= ticks - sp_ticks <= 550)
                                              or (type_of_hit == 4 and 240 <= ticks - sp_ticks <= 440)
                                              or (type_of_hit == 5 and 1100 <= ticks - sp_ticks <= 1450)
                                              or (type_of_hit == 6 and 450 <= ticks - sp_ticks <= 650))
              and th_health - p_of_hit > 0 and (thug_type_of_react != 0 or thug_type_of_react != 1) and thug_st != -2
              and ((th_revst == 0 and SMx - (Thx - th_sdvigx) >= 0) and type_of_hit != -1
                   or (th_revst == 1 and SMx - (Thx - th_sdvigx) <= 100))):
            thug_st = -2
            thug_ticks = ticks
            th_st = 0
            th_health -= p_of_hit
            # thug_type_of_react = random.choice([0, 1])  # реакция бандита на удар в лицо
            thug_type_of_react = 1

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
            if ticks - th_delay > 1500:
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
