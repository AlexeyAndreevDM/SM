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
# sdvigx = -550
# sdvigy = -330
sdvigx = -830
sdvigy = 1758
podst = 0
revst = 1
crawl_st = 0
acs = 0
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

    if st == 0 and (sdvigy <= -330 or sdvigy >= 1600) and (0 <= ticks - sp_ticks <= 5000) \
            and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_a] and pygame.mouse.get_pressed() == (False, False, False):
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
        if sdvigy <= -330:
            Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
            SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
        elif sdvigy >= 1600:
            Spider_Man = pygame.transform.scale(Spider_Man, (68, 285))
            SCREEN.blit(Spider_Man, (SMx + 27, SMy + 16))


    elif st == 0 and (sdvigy <= -330 or sdvigy >= 1600) and (5000 <= ticks - sp_ticks <= 10000) \
            and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_a] and pygame.mouse.get_pressed() == (False, False, False):
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 22.png').convert_alpha()
        if sdvigy <= -330:
            Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
            SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
        elif sdvigy >= 1600:
            Spider_Man = pygame.transform.scale(Spider_Man, (68, 285))
            SCREEN.blit(Spider_Man, (SMx + 27, SMy + 16))



    if st == 0 and revst == 0 and sdvigy >= 1600 and sdvigx <= -550 and pygame.key.get_pressed()[pygame.K_d]:
        st = 6
        sp_ticks = ticks


# Сальто вперед
    if st == 6 and revst == 0 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 407.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 14))
    elif st == 6 and revst == 0 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 408.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 100, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 409.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 410.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 416.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 417.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 419.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 0 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 422.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 10))
    elif st == 6 and revst == 0 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 423.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 0))
    elif st == 6 and revst == 0 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 428.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 43, SMy + 25))
    elif st == 7 and revst == 0 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 429.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
    elif st == 7 and revst == 0 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 430.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
        sp_ticks = ticks


# Приземление + Кувырок
    if st == 8 and revst == 0 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 433.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
    elif st == 8 and revst == 0 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 434.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
    elif st == 8 and revst == 0 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 435.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
    elif st == 8 and revst == 0 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 436.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
    elif st == 8 and revst == 0 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 437.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 190))
    elif st == 8 and revst == 0 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 438.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 215))
    elif st == 8 and revst == 0 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 439.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 240))
    elif st == 8 and revst == 0 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 440.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 240))
    elif st == 8 and revst == 0 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 441.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 220))
    elif st == 8 and revst == 0 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 442.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 225))
    elif st == 8 and revst == 0 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 443.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 230))
    elif st == 8 and revst == 0 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 444.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 210))
    elif st == 8 and revst == 0 and crawl_st == 12:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 445.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 310))
        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 210))
    elif st == 8 and revst == 0 and crawl_st == 13:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 446.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 305))
        SCREEN.blit(Spider_Man, (SMx - 55, SMy + 170))
    elif st == 8 and revst == 0 and crawl_st == 14:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 447.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (310, 310))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 147))
        st = 0


    if st == 0 and revst == 1 and sdvigy >= 1600 and sdvigx >= -830 and pygame.key.get_pressed()[pygame.K_a]:
        st = 6
        sp_ticks = ticks

    # Сальто вперед
    if st == 6 and revst == 1 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 411.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 5))
    elif st == 6 and revst == 1 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 412.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 100, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 413.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 414.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 415.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 418.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 420.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 20))
    elif st == 6 and revst == 1 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 421.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy - 10))
    elif st == 6 and revst == 1 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 424.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (330, 340))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 0))
    elif st == 6 and revst == 1 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 427.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 43, SMy + 25))
    elif st == 7 and revst == 1 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 431.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
    elif st == 7 and revst == 1 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 432.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 25))
        sp_ticks = ticks

    # Приземление + Кувырок
    if st == 8 and revst == 1 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 448.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
    elif st == 8 and revst == 1 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 449.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
    elif st == 8 and revst == 1 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 450.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 115))
    elif st == 8 and revst == 1 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 451.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 115))
    elif st == 8 and revst == 1 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 452.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 300))
        SCREEN.blit(Spider_Man, (SMx - 73, SMy + 190))
    elif st == 8 and revst == 1 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 453.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 215))
    elif st == 8 and revst == 1 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 454.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 70, SMy + 240))
    elif st == 8 and revst == 1 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 455.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 240))
    elif st == 8 and revst == 1 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 456.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 220))
    elif st == 8 and revst == 1 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 457.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 225))
    elif st == 8 and revst == 1 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 458.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 230))
    elif st == 8 and revst == 1 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 459.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 330))
        SCREEN.blit(Spider_Man, (SMx - 50, SMy + 210))
    elif st == 8 and revst == 1 and crawl_st == 12:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 460.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (300, 310))
        SCREEN.blit(Spider_Man, (SMx - 60, SMy + 210))
    elif st == 8 and revst == 1 and crawl_st == 13:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 461.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (305, 305))
        SCREEN.blit(Spider_Man, (SMx - 55, SMy + 170))
    elif st == 8 and revst == 1 and crawl_st == 14:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 462.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (310, 310))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 147))
        st = 0



# Триггеры
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
            sdvigx -= 1
        elif revst == 1:
            sdvigx += 1
        if sdvigy - 5 - acs > -330:
            sdvigy -= (5 + acs)
        else:
            sdvigy = -330
        acs += 2


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
    elif st == 8 and (140 <= ticks - sp_ticks <= 200):
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
    elif st == 8 and (930 <= ticks - sp_ticks <= 1000):
        crawl_st = 14
    elif st == 8 and (ticks - sp_ticks > 1000):
        st = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

