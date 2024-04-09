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
sp_ticks = 0
bg = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                       "Textures/fhomewthspandpavmnt.jpg").convert()
bg = pygame.transform.scale(bg, (1414, 2000))
road = pygame.image.load("/Users/aleksej/PycharmProjects/pythonProject/Marvel's Spider-Man 2D/"
                         "Textures/дорога.jpeg").convert()
road = pygame.transform.scale(road, (2011, 354))
sdvigx = -680
sdvigy = -330
sdvigx = -550
sdvigy = 300
SMx, SMy = display_w // 2 - 150 + 15, display_h // 2 - 200 + 7
type_of_landing = -1
podst = 0
revst = 0
crawl_st, dcrawl_st = 0, 0
SMRt = 90
cc = SMx
wbx, wby = SMx + 90, SMy + 160
lh = 0
web_ticks = 0
amplitude = 10
frequency = 0.05
angle = 45
xx = 1090
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

# Триггеры
    if (st == 0 or st == 1 or st == 7) and -330 < sdvigy <= 1600 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        st = 9  # Раскачка на паутине
        sp_ticks = ticks
        crawl_st = 0

    if st == 9 and (1380 <= ticks - sp_ticks <= 2300) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        st = 10  # Выталкивание
        sp_ticks = ticks
        crawl_st = 0

    if st == 9 and (ticks - sp_ticks > 2300) and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        st = 11  # Слабое качание на паутине
        sp_ticks = ticks
        crawl_st = 0

    if st == 9 and (1380 > ticks - sp_ticks) and not pygame.key.get_pressed()[pygame.K_LSHIFT]:
        st = 7  # Падение при отпускании паутины
        sp_ticks = ticks
        crawl_st = 0

    if st == 9 and sdvigy <= -310 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        st = 12  # Приземление при низкой высоте полета
        if type_of_landing == -1:
            type_of_landing = random.randint(0, 2)
        sdvigy = -330
        sp_ticks = ticks
        crawl_st = 0


# Раскачка на паутине
    if st == 9 and crawl_st == 0 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        if sdvigy < 1400:
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 490.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (380, 340))
        Spider_Man = pygame.transform.rotate(Spider_Man, -50)
        SCREEN.blit(Spider_Man, (SMx - 130, SMy - 85))
    elif st == 10 and crawl_st == 3:
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
        Spider_Man = pygame.transform.rotate(Spider_Man, SMRt)
        SCREEN.blit(Spider_Man, (SMx - 40, SMy + 10))


# Приземление при низком полете №1
    if st == 12 and type_of_landing == 0 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 465.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 90, SMy + 100))
    elif st == 12 and type_of_landing == 0 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 466.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 130))
    elif st == 12 and type_of_landing == 0 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 467.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 150))
    elif st == 12 and type_of_landing == 0 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 468.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 160))
    elif st == 12 and type_of_landing == 0 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 469.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
        SCREEN.blit(Spider_Man, (SMx - 80, SMy + 170))


# Приземление при низком полете №2
    if st == 12 and type_of_landing == 1 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 493.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 90))
    elif st == 12 and type_of_landing == 1 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 494.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 100, SMy + 50))
    elif st == 12 and type_of_landing == 1 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 495.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 110, SMy + 50))
    elif st == 12 and type_of_landing == 1 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 496.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 120, SMy + 50))
    elif st == 12 and type_of_landing == 1 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 497.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 55))
    elif st == 12 and type_of_landing == 1 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 498.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 130, SMy + 115))
    elif st == 12 and type_of_landing == 1 and crawl_st == 7:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 499.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 130, SMy + 130))
    elif st == 12 and type_of_landing == 1 and crawl_st == 8:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 500.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 120, SMy + 165))
    elif st == 12 and type_of_landing == 1 and crawl_st == 9:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 501.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
        SCREEN.blit(Spider_Man, (SMx - 95, SMy + 192))
    elif st == 12 and type_of_landing == 1 and crawl_st == 10:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 502.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (340, 350))
        SCREEN.blit(Spider_Man, (SMx - 55, SMy + 223))


# Приземление при низком полете №3
    if st == 12 and type_of_landing == 2 and crawl_st == 0:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
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
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 504.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (410, 410))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 105))
    elif st == 12 and type_of_landing == 2 and crawl_st == 2:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 505.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
    elif st == 12 and type_of_landing == 2 and crawl_st == 3:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 506.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 138))
    elif st == 12 and type_of_landing == 2 and crawl_st == 4:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 507.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
    elif st == 12 and type_of_landing == 2 and crawl_st == 5:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 508.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
        SCREEN.blit(Spider_Man, (SMx - 140, SMy + 150))
    elif st == 12 and type_of_landing == 2 and crawl_st == 6:
        SCREEN.fill(pygame.Color('Black'))
        i = 0
        while i < tiles:
            SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
            SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
            i += 1
        if abs(sdvigx) > bg.get_width():
            sdvigx = 0
        Spider_Man = pygame.image.load('Тема 509.png').convert_alpha()
        Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
        SCREEN.blit(Spider_Man, (SMx - 135, SMy + 170))



# Раскачка на паутине
    if st == 9 and (0 <= ticks - sp_ticks <= 75) and sdvigy >= -1010:
        crawl_st = 0
        sdvigy -= 5
        sdvigx -= 5
    elif st == 9 and (75 <= ticks - sp_ticks <= 150) and sdvigy >= -1010:
        if xx > 1090:
            xx = 1090
        crawl_st = 3
        sdvigy -= 5
        sdvigx -= 5
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
    elif st == 10 and (120 <= ticks - sp_ticks <= 200):
        crawl_st = 1
        sdvigy += 8
        sdvigx -= 10
    elif st == 10 and (200 <= ticks - sp_ticks <= 550):
        crawl_st = 2
        sdvigy += 7
        sdvigx -= 9
    elif st == 10 and (550 <= ticks - sp_ticks <= 800):
        crawl_st = 3
        sdvigy += 7
        sdvigx -= 9
        SMRt -= 1
    elif st == 10 and (ticks - sp_ticks > 800):
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
    elif st == 12 and type_of_landing == 0 and (ticks - sp_ticks > 1100):
        st = 0
        type_of_landing = -1


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
    elif st == 12 and type_of_landing == 1 and (800 <= ticks - sp_ticks <= 900):
        crawl_st = 8
    elif st == 12 and type_of_landing == 1 and (900 <= ticks - sp_ticks <= 1000):
        crawl_st = 9
    elif st == 12 and type_of_landing == 1 and (1000 <= ticks - sp_ticks <= 1500):
        crawl_st = 10
    elif st == 12 and type_of_landing == 1 and (ticks - sp_ticks > 1500):
        st = 0
        type_of_landing = -1


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
    elif st == 12 and type_of_landing == 2 and (600 <= ticks - sp_ticks <= 1100):
        crawl_st = 6
    elif st == 12 and type_of_landing == 2 and (ticks - sp_ticks > 1100):
        st = 0
        type_of_landing = -1



    # i = 0
    # SCREEN.fill(pygame.Color('Black'))
    # while i < tiles:
    #     SCREEN.blit(bg, (bg.get_width() * i + sdvigx, -2000 + display_h - 100 + sdvigy))
    #     SCREEN.blit(road, (road.get_width() * i + sdvigx, 800 + sdvigy))
    #     i += 1
    # if abs(sdvigx) > bg.get_width():
    #     sdvigx = 0


    # Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 75, SMy + 65))
    # Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
    # SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
    # Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))


    # Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 30))
    # Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # SCREEN.blit(Spider_Man, (SMx - 90, SMy + 65))
    # Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 100, SMy + 35))


    # Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 135, SMy + 30))
    # Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # SCREEN.blit(Spider_Man, (SMx - 82, SMy + 65))
    # Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 86, SMy + 33))


    # Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 85, SMy - 15))
    # Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 45, SMy + 10))
    # Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 58, SMy - 22))


    # Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 100, SMy - 25))
    # Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 60, SMy + 3))
    # Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 75, SMy - 25))


    # Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 95, SMy - 45))
    # Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 55, SMy - 15))
    # Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 75, SMy - 45))


    # Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -10)
    # SCREEN.blit(Spider_Man, (SMx - 85, SMy - 40))
    # Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 50, SMy - 10))
    # Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 10)
    # SCREEN.blit(Spider_Man, (SMx - 70, SMy - 40))




    # Spider_Man = pygame.image.load('Тема 23.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (72, 300))
    # SCREEN.blit(Spider_Man, (SMx + 27, SMy + 140))

    # Spider_Man = pygame.image.load('Тема 463.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 40)
    # wbx, wby = SMx + 90, SMy + 160
    # if cc > -100000:
    #     xx = SMx + 90
    #     if ticks - web_ticks >= 10 and cc > 0:
    #         cc -= 25
    #         web_ticks = 0
    #     for x in range(SMx + 60, cc, -1):
    #         if lh == 0:
    #             xx += 1
    #         elif lh == 1:
    #             if x % 4 == 0:
    #                 xx += 1
    #         y = amplitude * math.sin(frequency * x) - 240
    #         pygame.draw.circle(SCREEN, pygame.Color('White'), (xx, int(y + x * math.tan(math.radians(angle)))), 1)
    # xx = 1090
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 5, wby), (xx, 0), 1)
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy - 40))

    # xx = 1050
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 20, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 477.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (340, 365))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 50))
    # xx = 960
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 20, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 478.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (340, 365))
    # SCREEN.blit(Spider_Man, (SMx - 125, SMy + 55))
    # xx = 870
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 20, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 479.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (185, 280))
    # SCREEN.blit(Spider_Man, (SMx - 35, SMy + 90))
    # xx = 780
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 20, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 480.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # SCREEN.blit(Spider_Man, (SMx - 90, SMy + 65))
    # xx = 690
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 40, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 481.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # SCREEN.blit(Spider_Man, (SMx - 82, SMy + 65))
    # xx = 620
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 45, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 482.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 375))
    # SCREEN.blit(Spider_Man, (SMx - 60, SMy + 50))
    # xx = 550
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 55, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 483.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 45, SMy + 10))
    # xx = 480
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 65, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 484.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 60, SMy + 3))
    # xx = 410
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 70, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 485.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 50, SMy - 3))
    # xx = 380
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 73, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 486.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 55, SMy - 15))
    # xx = 340
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx + 65, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 487.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (390, 390))
    # SCREEN.blit(Spider_Man, (SMx - 60, SMy - 10))


    # xx = 310
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 70, wby + 35), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 488.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (360, 360))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -20)
    # SCREEN.blit(Spider_Man, (SMx - 115, SMy - 105))
    # xx = 240
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 80, wby + 55), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 489.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (360, 340))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -50)
    # SCREEN.blit(Spider_Man, (SMx - 115, SMy - 95))
    # Spider_Man = pygame.image.load('Тема 490.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (380, 340))
    # Spider_Man = pygame.transform.rotate(Spider_Man, -70)
    # SCREEN.blit(Spider_Man, (SMx - 130, SMy - 85))
    # Spider_Man = pygame.image.load('Тема 429.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (290, 290))
    # Spider_Man = pygame.transform.rotate(Spider_Man, 90)
    # SCREEN.blit(Spider_Man, (SMx - 40, SMy + 10))


    # xx = 240
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 75, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 464.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 80, SMy + 70))
    # Spider_Man = pygame.image.load('Тема 465.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 90, SMy + 100))
    # Spider_Man = pygame.image.load('Тема 466.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 80, SMy + 130))
    # Spider_Man = pygame.image.load('Тема 467.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 80, SMy + 150))
    # Spider_Man = pygame.image.load('Тема 468.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 80, SMy + 160))
    # Spider_Man = pygame.image.load('Тема 469.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (320, 330))
    # SCREEN.blit(Spider_Man, (SMx - 80, SMy + 170))

    # xx = 240
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 492.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 100, SMy + 90))
    # Spider_Man = pygame.image.load('Тема 493.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 100, SMy + 90))
    # Spider_Man = pygame.image.load('Тема 494.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 100, SMy + 50))
    # Spider_Man = pygame.image.load('Тема 495.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 110, SMy + 50))
    # Spider_Man = pygame.image.load('Тема 496.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 120, SMy + 50))
    # Spider_Man = pygame.image.load('Тема 497.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 55))
    # Spider_Man = pygame.image.load('Тема 498.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 130, SMy + 115))
    # Spider_Man = pygame.image.load('Тема 499.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 130, SMy + 130))
    # Spider_Man = pygame.image.load('Тема 500.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 120, SMy + 165))
    # Spider_Man = pygame.image.load('Тема 501.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (345, 340))
    # SCREEN.blit(Spider_Man, (SMx - 95, SMy + 192))
    # Spider_Man = pygame.image.load('Тема 502.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (340, 350))
    # SCREEN.blit(Spider_Man, (SMx - 55, SMy + 223))


    # xx = 240
    # pygame.draw.line(SCREEN, pygame.Color('White'), (wbx - 35, wby), (xx, 0), 1)
    # Spider_Man = pygame.image.load('Тема 503.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (410, 410))
    # SCREEN.blit(Spider_Man, (SMx - 120, SMy + 45))
    # Spider_Man = pygame.image.load('Тема 504.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 105))
    # Spider_Man = pygame.image.load('Тема 505.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
    # Spider_Man = pygame.image.load('Тема 506.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 138))
    # Spider_Man = pygame.image.load('Тема 507.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 133))
    # Spider_Man = pygame.image.load('Тема 508.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 140, SMy + 150))
    # Spider_Man = pygame.image.load('Тема 509.png').convert_alpha()
    # Spider_Man = pygame.transform.scale(Spider_Man, (420, 420))
    # SCREEN.blit(Spider_Man, (SMx - 135, SMy + 170))





    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

