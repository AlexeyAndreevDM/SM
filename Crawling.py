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
sdvigx = -680
sdvigy = -330
# sdvigx = -680
# sdvigy = 1580
podst = 0
revst = 0
crawl_st = 0
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



    if st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_SPACE]\
            and st != 3:
        st = 3


    # Запрыгивание на стену
    if st == 3 and (0 <= ticks - sp_ticks <= 70):
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


    elif st == 3 and (70 <= ticks - sp_ticks <= 140) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
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


    elif st == 3 and (140 <= ticks - sp_ticks <= 210) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
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


    elif st == 3 and (210 <= ticks - sp_ticks <= 310) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 70
        Spider_Man = pygame.image.load('Тема 40.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 290))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 135))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 3 and (310 <= ticks - sp_ticks <= 410) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 60
        Spider_Man = pygame.image.load('Тема 41.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 325))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 80))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 3 and (410 <= ticks - sp_ticks <= 510) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        sdvigy += 100
        Spider_Man = pygame.image.load('Тема 346.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (165, 320))
        SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        st = 4

    else:
        if st == 3:
            sp_ticks = ticks


    # Ползанье по стене вверх
    if st == 4 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 309.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 320))
        SCREEN.blit(Spider_Man, (SMx + 22, SMy + 100))
    elif st == 4 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 310.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (135, 300))
        SCREEN.blit(Spider_Man, (SMx + 19, SMy + 125))
    elif st == 4 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 313.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (125, 270))
        SCREEN.blit(Spider_Man, (SMx + 28, SMy + 135))
    elif st == 4 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 314.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (125, 265))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 137))
    elif st == 4 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 317.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (121, 265))
        SCREEN.blit(Spider_Man, (SMx + 32, SMy + 120))
    elif st == 4 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 318.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (125, 265))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 106))
    elif st == 4 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 321.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 95))
    elif st == 4 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 324.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
    elif st == 4 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 326.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
        SCREEN.blit(Spider_Man, (SMx + 23, SMy + 115))
    elif st == 4 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 327.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 280))
        SCREEN.blit(Spider_Man, (SMx + 24, SMy + 130))
    elif st == 4 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 329.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
        SCREEN.blit(Spider_Man, (SMx + 18, SMy + 125))
    elif st == 4 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 330.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (135, 290))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 133))
    elif st == 4 and crawl_st == 12:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 333.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 285))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 135))
    elif st == 4 and crawl_st == 13:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 334.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 310))
        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 112))
    elif st == 4 and crawl_st == 14:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 336.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (135, 300))
        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 101))
    elif st == 4 and crawl_st == 15:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 337.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 300))
        SCREEN.blit(Spider_Man, (SMx + 15, SMy + 90))
    elif st == 4 and crawl_st == 16:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 340.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 310))
        SCREEN.blit(Spider_Man, (SMx + 14, SMy + 83))
    elif st == 4 and crawl_st == 17:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 341.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
        SCREEN.blit(Spider_Man, (SMx + 28, SMy + 83))



    # Ползанье по стене вниз
    if st == -4 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 308.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 300))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 100))
    elif st == -4 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 311.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (135, 280))
        SCREEN.blit(Spider_Man, (SMx + 19, SMy + 105))
    elif st == -4 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 312.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (125, 270))
        SCREEN.blit(Spider_Man, (SMx + 28, SMy + 110))
    elif st == -4 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 315.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 277))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
    elif st == -4 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 316.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx + 28, SMy + 110))
    elif st == -4 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 319.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 120))
    elif st == -4 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 320.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (140, 290))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 115))
    elif st == -4 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 322.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (85, 260))
        SCREEN.blit(Spider_Man, (SMx + 55, SMy + 115))
    elif st == -4 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 323.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (90, 250))
        SCREEN.blit(Spider_Man, (SMx + 50, SMy + 120))
    elif st == -4 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 325.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 280))
        SCREEN.blit(Spider_Man, (SMx + 29, SMy + 120))
    elif st == -4 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 328.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (90, 250))
        SCREEN.blit(Spider_Man, (SMx + 50, SMy + 120))
    elif st == -4 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 331.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
    elif st == -4 and crawl_st == 12:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 332.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 265))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
    elif st == -4 and crawl_st == 13:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 335.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (130, 275))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 105))
    elif st == -4 and crawl_st == 14:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 345.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (95, 270))
        SCREEN.blit(Spider_Man, (SMx + 45, SMy + 120))
    elif st == -4 and crawl_st == 15:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 338.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (135, 280))
        SCREEN.blit(Spider_Man, (SMx + 25, SMy + 110))
    elif st == -4 and crawl_st == 16:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 339.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 300))
        SCREEN.blit(Spider_Man, (SMx + 14, SMy + 105))
    elif st == -4 and crawl_st == 17:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 342.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 315))
        SCREEN.blit(Spider_Man, (SMx + 28, SMy + 95))


    # Запрыгивание на крышу
    if st == 5 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 348.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (152, 340))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy - 20))
    elif st == 5 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 349.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (160, 370))
        SCREEN.blit(Spider_Man, (SMx - 13, SMy - 20))
    elif st == 5 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 352.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
        SCREEN.blit(Spider_Man, (SMx + 9, SMy - 20))
    elif st == 5 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 353.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (137, 310))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
    elif st == 5 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 356.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 333))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
    elif st == 5 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 357.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 333))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy - 3))
    elif st == 5 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 360.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 35))
    elif st == 5 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 361.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (145, 325))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 0))
    elif st == 5 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 364.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (180, 385))
        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 10))
    elif st == 5 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 365.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 320))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 52))
    elif st == 5 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 368.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (150, 320))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 72))
    elif st == 5 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 369.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (133, 177))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 126))
        st = 0


    # Спрыгивание со стены
    if st == -5 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 372.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (152, 320))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 100))
    elif st == -5 and crawl_st == 1:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 373.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (152, 330))
        SCREEN.blit(Spider_Man, (SMx + 2, SMy + 100))
    elif st == -5 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 376.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 350))
        SCREEN.blit(Spider_Man, (SMx - 17, SMy + 97))
    elif st == -5 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 377.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (230, 445))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 70))
    elif st == -5 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 380.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (255, 470))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 70))
    elif st == -5 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 406.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (235, 215))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 70))
    elif st == -5 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 383.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (210, 435))
        SCREEN.blit(Spider_Man, (SMx - 17, SMy - 27))
    elif st == -5 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 384.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (190, 410))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy + 0))
    elif st == -5 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 405.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (205, 245))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 60))
    elif st == -5 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 386.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (200, 430))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 22))
    elif st == -5 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 389.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (240, 510))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 0))
    elif st == -5 and crawl_st == 11:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 400.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (250, 200))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 160))
    elif st == -5 and crawl_st == 12:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 391.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (250, 495))
        SCREEN.blit(Spider_Man, (SMx + 20, SMy - 20))
    elif st == -5 and crawl_st == 13:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 392.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (210, 460))
        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 65))
    elif st == -5 and crawl_st == 14:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 402.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (200, 205))
        SCREEN.blit(Spider_Man, (SMx + 10, SMy + 235))
    elif st == -5 and crawl_st == 15:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 394.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (180, 390))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 125))
    elif st == -5 and crawl_st == 16:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 397.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 380))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 115))
    elif st == -5 and crawl_st == 17:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 398.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (160, 340))
        SCREEN.blit(Spider_Man, (SMx + 0, SMy + 155))


# Триггеры
    if st == 4 and st != -4 and pygame.key.get_pressed()[pygame.K_s]:
        st = -4
        sp_ticks = ticks

    if st == -4 and st != 4 and pygame.key.get_pressed()[pygame.K_w]:
        st = 4
        sp_ticks = ticks

    if st == 4 and pygame.key.get_pressed()[pygame.K_w] and 1550 <= sdvigy <= 1650:
        st = 5
        sp_ticks = ticks

    if st == 4 and pygame.key.get_pressed()[pygame.K_SPACE]:
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
        sdvigx -= 10
    elif st == 5 and (490 <= ticks - sp_ticks <= 560):
        crawl_st = 7
        sdvigy = 1758
        sdvigx -= 5
    elif st == 5 and (560 <= ticks - sp_ticks <= 630):
        crawl_st = 8
        sdvigx -= 5
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
    elif st == -5 and (980 <= ticks - sp_ticks <= 1050):
        crawl_st = 14
        sdvigy = -330
    elif st == -5 and (1050 <= ticks - sp_ticks <= 1120):
        crawl_st = 15
    elif st == -5 and (1120 <= ticks - sp_ticks <= 1190):
        crawl_st = 16
    elif st == -5 and (1190 <= ticks - sp_ticks <= 1400):
        crawl_st = 17
    elif st == -5 and (ticks - sp_ticks > 1400):
        st = 0







    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            print(sdvigx, sdvigy)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

