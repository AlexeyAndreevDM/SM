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

# ['Тема 7.png', 'Тема 10.png', 'Тема 11.png', 'Тема 14.png', 'Тема 15.png', 'Тема 18.png', 'Тема 19.png']
# images_stay = ['Тема 23.png'] # 'Тема 22.png'
while running:
    ticks = pygame.time.get_ticks()

    if st == 0 and sdvigy <= -330 and (0 <= ticks - sp_ticks <= 5000) \
            and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and (5000 <= ticks - sp_ticks <= 10000 or sp_ticks == 0) \
            and not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_SPACE] \
            and not pygame.key.get_pressed()[pygame.K_a]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 22.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and (0 <= ticks - sp_ticks <= 80 or sp_ticks == 0):
        if podst != 1:
            podst = 1
        if revst == 1:
            revst = 0
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 7.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (115, 300))
        SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
        if sp_ticks == 0:
            sp_ticks = ticks


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 80 <= ticks - sp_ticks <= 130:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 10.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (170, 300))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0




    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 130 <= ticks - sp_ticks <= 180:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 11.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (210, 300))
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 123))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0




    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 180 <= ticks - sp_ticks <= 230:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 14.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (203, 300))
        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 130))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 230 <= ticks - sp_ticks <= 310:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 15.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 310 <= ticks - sp_ticks <= 360:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 18.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (114, 300))
        SCREEN.blit(Spider_Man, (SMx, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0



    elif st == 10000 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 360 <= ticks - sp_ticks <= 410:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 19.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (210, 300))
        SCREEN.blit(Spider_Man, (SMx + 27, SMy + 130))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 410 <= ticks - sp_ticks <= 460:
        sdvigx += 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 28.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
        SCREEN.blit(Spider_Man, (SMx - 45, SMy + 123))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 460 <= ticks - sp_ticks <= 510:
        sdvigx -= 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 29.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (204, 300))
        SCREEN.blit(Spider_Man, (SMx - 35, SMy + 130))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    elif st == 0 and sdvigy <= -330 and pygame.key.get_pressed()[pygame.K_d] \
            and 510 <= ticks - sp_ticks <= 580:
        sdvigx -= 4
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        Spider_Man = pygame.image.load('Тема 32.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
        SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0


    else:
        sp_ticks = ticks

    # Spider_Man = pygame.image.load('Тема 7.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (115, 300))
    # SCREEN.blit(Spider_Man, (SMx - 5, SMy + 140))
    # Spider_Man = pygame.image.load('Тема 10.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (170, 300))
    # SCREEN.blit(Spider_Man, (SMx - 20, SMy + 130))
    # Spider_Man = pygame.image.load('Тема 11.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (210, 300))
    # SCREEN.blit(Spider_Man, (SMx - 40, SMy + 123))
    # Spider_Man = pygame.image.load('Тема 14.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (203, 300))
    # SCREEN.blit(Spider_Man, (SMx - 45, SMy + 130))
    # Spider_Man = pygame.image.load('Тема 15.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (147, 300))
    # SCREEN.blit(Spider_Man, (SMx - 20, SMy + 140))
    # Spider_Man = pygame.image.load('Тема 18.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (114, 300))
    # SCREEN.blit(Spider_Man, (SMx, SMy + 140))
    # Spider_Man = pygame.image.load('Тема 28.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (215, 300))
    # SCREEN.blit(Spider_Man, (SMx - 45, SMy + 123))
    # Spider_Man = pygame.image.load('Тема 29.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (204, 300))
    # SCREEN.blit(Spider_Man, (SMx - 35, SMy + 130))
    # Spider_Man = pygame.image.load('Тема 32.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (144, 300))
    # SCREEN.blit(Spider_Man, (SMx, SMy + 140))







    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

