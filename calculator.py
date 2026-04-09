import pygame

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

numbers = [[7,8,9],[4,5,6],[1,2,3]]
text = ""

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
                        if i == 0:
                            text+="7"
                        if i == 3:
                            text+="8"
                        if i == 6:
                            text+="9"
                        if i == 1:
                            text+="4"
                        if i == 4:
                            text+="5"
                        if i == 7:
                            text+="6"
                        if i == 2:
                            text+="1"
                        if i == 5:
                            text+="2"
                        if i == 8:
                            text+="3"

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

    pygame.draw.rect(screen, colours[6], (round(float(screen_width/10)), round(float(screen_height/20)),(round(float((screen_width/10)*8))) , round(float(screen_height/20))), 5, 10)

    screen.blit(font_stats.render(f"{text}", True, colours[1]),(round(float((screen_width*1.1) / 10)), round(float((screen_height * 1.25) / 20))))

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

    for c in range(3):
        for d in range(3):
            screen.blit(font_stats.render(f"{numbers[d][c]}", True, colours[1]),(round(float(screen_width / 10) * 1.33 * c + (screen_width*3)/20), round((float(screen_height / 20)) * (1.2 * d) + (screen_height / 20) * 4.2)))








    pygame.display.flip()
    clock.tick(60)

pygame.quit()
