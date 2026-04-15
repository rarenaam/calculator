import pygame
import math
import re

resolution = [[640, 480],[1280, 720],[1920, 1080],[2560, 1440],[3840, 2160]]

pygame.init()
screen_height, screen_width =  resolution[4][0]/(16/9)**2, resolution[4][1]/(16/9)**2
font_stats = pygame.font.SysFont("Arial", 24, True)
screen = pygame.display.set_mode((int(screen_width), int(screen_height)))
clock = pygame.time.Clock()

red, orange, yellow, green, blue, purple, white = (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128), (255, 255, 255)
colours = [red, orange, yellow, green, blue, purple, white]
circles = []
circles.append([round(float(screen_width / 10) * 1.1), round(float(screen_height / 20)) * 3])
circles.append([round(float(screen_width / 10) * 1.1 * 2), round(float(screen_height / 20)) * 3])
circles.append([round(float(screen_width / 10) * 1.1 * 7), round(float(screen_height / 20)) * 3])
circles.append([round(float(screen_width / 10) * 1.1 * 8), round(float(screen_height / 20)) * 3])

rects = []
for a in range(6):
    for b in range(3):
        rect = pygame.Rect(round(float(screen_width / 10) * 1.25 * a + 5 * a + (screen_width / 20) * 2), round((float(screen_height / 20)) * (1.2 * b) + (screen_height / 20) * 4),  (round(float((screen_width / 10) * 1.25))), round(float(screen_height / 20)))
        rects.append(rect)

for g in range(5):
    for f in range(4):
        rect = pygame.Rect(round(float(screen_width / 10) * 1.5 * g + 5 * g + (screen_width / 20) * 2), round((float(screen_height / 20)) * (1.2 * (f+4)) + (screen_height / 20) * 4),  (round(float((screen_width / 10) * 1.5))), round(float(screen_height / 20)))
        rects.append(rect)
numbers_1 = [["a b/c","(-)","RCL"],["**0.5"," ````","ENG"],[" **2","  hyp","     ("],["**","   sin","     )"],["   log","   cos","  ,"],["   ln","   tan"," M+"]]
numbers_2 = [[7,4,1,0],[8,5,2,"."],[9,6,3,"*10**"],["DEL","*","+","ANS"],["AC","/","-","="]]
text = ""
text_result = ""
ANS = ""
result_given = 0
running = True
while running:
    cursor_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(rects)):
                    if rects[i].collidepoint(event.pos):
                        if i == 1:
                            if result_given == 1:
                                text = "-" + str(ANS)
                                result_given = 0
                            else:
                                text = "-"
                        if i == 3:
                            if result_given == 1:
                                text = "**0.5"
                                result_given = 0
                            else:
                                text += "**0.5"
                        if i == 6:
                            if result_given == 1:
                                text = str(ANS) + "**2"
                                result_given = 0
                            else:
                                text += "**2"
                        if i == 8:
                            if result_given == 1:
                                text = "("
                                result_given = 0
                            else:
                                text += "("
                        if i == 9:
                            if result_given == 1:
                                text = str(ANS) + "**"
                                result_given = 0
                            else:
                                text += "**"
                        if i == 10:
                            if result_given == 1:
                                text = "sin"
                                result_given = 0
                            else:
                                text += "sin"
                        if i == 11:
                            if result_given == 1:
                                text = ")"
                                result_given = 0
                            else:
                                text += ")"
                        if i == 18:
                            if result_given == 1:
                                text = "7"
                                result_given = 0
                            else:
                                text += "7"
                        if i == 22:
                            if result_given == 1:
                                text = "8"
                                result_given = 0
                            else:
                                text += "8"
                        if i == 26:
                            if result_given == 1:
                                text = "9"
                                result_given = 0
                            else:
                                text += "9"
                        if i == 19:
                            if result_given == 1:
                                text = "4"
                                result_given = 0
                            else:
                                text += "4"
                        if i == 23:
                            if result_given == 1:
                                text = "5"
                                result_given = 0
                            else:
                                text += "5"
                        if i == 27:
                            if result_given == 1:
                                text = "6"
                                result_given = 0
                            else:
                                text += "6"
                        if i == 20:
                            if result_given == 1:
                                text = "1"
                                result_given = 0
                            else:
                                text += "1"
                        if i == 24:
                            if result_given == 1:
                                text = "2"
                                result_given = 0
                            else:
                                text += "2"
                        if i == 28:
                            if result_given == 1:
                                text = "3"
                                result_given = 0
                            else:
                                text += "3"
                        if i == 21:
                            if result_given == 1:
                                text = "0"
                                result_given = 0
                            else:
                                text += "0"
                        if i == 25:
                            if result_given == 1:
                                text = "."
                                result_given = 0
                            else:
                                text += "."
                        if i == 29:
                            if result_given == 1:
                                text = "*10**"
                                result_given = 0
                            else:
                                text += "*10**"
                        if i == 30:
                            text = text[:-1]
                        if i == 31:
                            if result_given == 1:
                                text = str(ANS) + "*"
                                result_given = 0
                            else:
                                text += "*"
                        if i == 32:
                            if result_given == 1:
                                text = str(ANS) + "+"
                                result_given = 0
                            else:
                                text += "+"
                        if i == 33:
                            if result_given == 1:
                                text = "ANS"
                                result_given = 0
                            else:
                                text += "ANS"
                        if i == 34:
                            text = ""
                            text_given = ""
                        if i == 35:
                            if result_given == 1:
                                text = str(ANS) + "/"
                                result_given = 0
                            else:
                                text += "/"
                        if i == 36:
                            if result_given == 1:
                                text = str(ANS) + "-"
                                result_given = 0
                            else:
                                text += "-"
                        if i == 37:
                            if text != "":
                                try:
                                    waarde_ans = ANS
                                    text_niet = re.sub(r"sin\(.*?\)", "0", text)
                                    text_niet = text.replace("sin", "math.sin")
                                    text_niet = text.replace("tan", "math.tan")
                                    text_niet = text.replace("cos", "math.cos")
                                    print(text_niet)
                                    text_result = eval(text_niet)
                                    ANS = text_result
                                    result_given = 1
                                except:
                                    text_result = "Error"
                                    result_given = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, pos in enumerate(circles):
                    middelpunt = pygame.math.Vector2(pos)
                    muis = pygame.math.Vector2(cursor_pos)
                    if middelpunt.distance_to(muis) <= 15:
                        None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                for i in range(len(input)):
                    text += str(input[i])

    #scherm opnieuw zwart maken
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colours[6], (round(float(screen_width/10)), round(float(screen_height/20)),(round(float((screen_width/10)*8))) , round(float(screen_height/20)*1.5)), 5, 10)

    screen.blit(font_stats.render(f"{text}", True, colours[1]),(round(float((screen_width*1.1) / 10)), round(float((screen_height * 1.20) / 20))))
    screen.blit(font_stats.render(f"{text_result}", True, colours[1]),(round(float((screen_width * 1.1) / 10)), round(float((screen_height * 1.8) / 20))))

    for i in range(len(circles)):
        pygame.draw.circle(screen, colours[6], circles[i], 15, 3)

    for rect in rects:
        if rect.collidepoint(cursor_pos):
            kleur = colours[1]
        else:
            kleur = colours[6]

        pygame.draw.rect(screen, kleur, rect, 5, 5)

    for i, pos in enumerate(circles):
        middelpunt = pygame.math.Vector2(pos)
        muis = pygame.math.Vector2(cursor_pos)

        # Als de afstand tot het midden minder dan 10 pixels is (jouw straal)
        if middelpunt.distance_to(muis) <= 15:
            pygame.draw.circle(screen, colours[1], circles[i], 15, 3)

    for h in range(6):
        for r in range(3):
            screen.blit(font_stats.render(f"{numbers_1[h][r]}", True, colours[1]),(round(float(screen_width / 10) * 1.3 * h + (screen_width*2.5)/20), round((float(screen_height / 20)) * (1.2 * r) + (screen_height / 20) * 4.3)))


    for c in range(5):
        for d in range(4):
            screen.blit(font_stats.render(f"{numbers_2[c][d]}", True, colours[1]),(round(float(screen_width / 10) * 1.5 * c + (screen_width*3)/20), round((float(screen_height / 20)) * (1.2 * (d+3)) + (screen_height / 20) * 5.4)))






    pygame.display.flip()
    clock.tick(60)

pygame.quit()
