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
sp_ticks = 0
bg = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                       "Textures/fhomewthspandpavmnt.jpg").convert()
bg = pygame.transform.scale(bg, (1414, 2000))
road = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                         "Textures/дорога.jpeg").convert()
road = pygame.transform.scale(road, (2011, 354))
sdvigx = 0
sdvigy = -330
podst = 0
revst = 0
coords_increase = 0
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
# SMXstart, SMYstart = 0, 0
# SMRt, srt = -50, -40
# coords_increase, sdvigxconst, sdvigyconst, zvukst = 0, 0, 0, 0


while running:
    ticks = pygame.time.get_ticks()

    # if st == 0 and sdvigy <= -330 and (0 <= ticks - sp_ticks <= 5000) \
    #         and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
    #         and not pygame.key.get_pressed()[pygame.K_a]:
    #     SCREEN.fill(pygame.Color('Black'))
    #     i = 0
    #     while i < tiles:
    #         SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
    #         SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
    #         i += 1
    #     Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
    #     Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
    #     SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
    #     if abs(sdvigx) > bg.get_width():
    #         sdvigx = 0
    #
    #
    # elif st == 0 and sdvigy <= -330 and (5000 <= ticks - sp_ticks <= 10000 or sp_ticks == 0) \
    #         and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
    #         and not pygame.key.get_pressed()[pygame.K_a]:
    #     SCREEN.fill(pygame.Color('Black'))
    #     i = 0
    #     while i < tiles:
    #         SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
    #         SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
    #         i += 1
    #     Spider_Man = pygame.image.load('Тема 22.png').convert_alpha()
    #     Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
    #     SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
    #     if abs(sdvigx) > bg.get_width():
    #         sdvigx = 0
    #     sp_ticks = ticks

    # Триггер
    if st == 0 and pygame.key.get_pressed()[pygame.K_SPACE] and st != 1:
        st = 1

    if st == 1 and revst == 0 and (0 <= ticks - sp_ticks <= 70) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 33.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 175))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 36.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 215))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 225))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 0 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 37.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (185, 265))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 0 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 65
        Spider_Man = pygame.image.load('Тема 40.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (182, 305))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 45
        Spider_Man = pygame.image.load('Тема 41.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (155, 360))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 0 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 35
        Spider_Man = pygame.image.load('Тема 44.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (155, 290))
        SCREEN.blit(Spider_Man, (SMx - 35, SMy + 150))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 0 and (510 <= ticks - sp_ticks <= 700) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 45.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 220))
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 150))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0




    elif st == 1 and revst == 0 and (700 <= ticks - sp_ticks <= 830) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy -= 50
        Spider_Man = pygame.image.load('Тема 48.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (198, 300))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0



    elif st == 1 and revst == 0 and (sdvigy > -330 or (830 <= ticks - sp_ticks <= 900)) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy -= 83
        Spider_Man = pygame.image.load('Тема 49.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (230, 280))
        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 160))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (900 <= ticks - sp_ticks <= 970) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        if sdvigy != -330:
            sdvigy = -330
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 52.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (205, 230))
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 210))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (970 <= ticks - sp_ticks <= 1040) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        if sdvigy != -330:
            sdvigy = -330
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 53.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (173, 200))
        SCREEN.blit(Spider_Man, (SMx - 32, SMy + 240))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (1040 <= ticks - sp_ticks <= 1110) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 56.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 230))
        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 210))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (1110 <= ticks - sp_ticks <= 1180) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 57.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 270))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 170))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 0 and (1180 <= ticks - sp_ticks <= 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 60.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (129, 300))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0

    elif st == 1 and revst == 0 and (ticks - sp_ticks > 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        sp_ticks = ticks
        st = 0










    if st == 1 and revst == 1 and (0 <= ticks - sp_ticks <= 70) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 34.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 175))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 35.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 215))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 225))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 1 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 38.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (185, 265))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 175))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 1 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 10
        Spider_Man = pygame.image.load('Тема 39.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (182, 305))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 1 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 30
        Spider_Man = pygame.image.load('Тема 42.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (155, 360))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 1 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 20
        Spider_Man = pygame.image.load('Тема 43.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (155, 290))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 150))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        print(sdvigy)


    elif st == 1 and revst == 1 and (510 <= ticks - sp_ticks <= 700) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 46.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 220))
        SCREEN.blit(Spider_Man, (SMx - 10, SMy + 150))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0




    elif st == 1 and revst == 1 and (700 <= ticks - sp_ticks <= 830) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy -= 20
        Spider_Man = pygame.image.load('Тема 47.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (198, 300))
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0



    elif st == 1 and revst == 1 and (sdvigy > -330 or (830 <= ticks - sp_ticks <= 900)) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy -= 40
        Spider_Man = pygame.image.load('Тема 50.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (230, 280))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 160))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (900 <= ticks - sp_ticks <= 970) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        if sdvigy != -330:
            sdvigy = -330
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 51.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (205, 230))
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 210))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (970 <= ticks - sp_ticks <= 1040) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        if sdvigy != -330:
            sdvigy = -330
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 54.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (173, 200))
        SCREEN.blit(Spider_Man, (SMx - 32, SMy + 240))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (1040 <= ticks - sp_ticks <= 1110) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 55.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 230))
        SCREEN.blit(Spider_Man, (SMx - 30, SMy + 210))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (1110 <= ticks - sp_ticks <= 1180) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 58.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 270))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 170))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 1 and revst == 1 and (1180 <= ticks - sp_ticks <= 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 59.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (129, 300))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0

    elif st == 1 and revst == 1 and (ticks - sp_ticks > 1350) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        sp_ticks = ticks
        st = 0



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

