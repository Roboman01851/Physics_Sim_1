import pygame, math, time, settings, numpy


pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()
def startProgram():
    running = True
    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 100
    angle = 0

    shape_color = [0 , 255, 255]
    ground_color = [0, 255, 0]

    ground = settings.height - 60
    startingPos = [center_x, center_y]


    while running:
        #clock.tick(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0,0,0))

        button_pressed = pygame.key.get_pressed()

        pygame.draw.circle(game_window, shape_color, [500, 500], 20)

        pygame.draw.rect(game_window, ground_color, [(0, ground), (settings.width, settings.height)])

        if button_pressed[pygame.K_UP]:
            angle += 0.1
            time.sleep(0.2)
        if button_pressed[pygame.K_DOWN]:
            angle -= 0.1
            time.sleep(0.2)

        drawTangent(angle)



        pygame.display.flip()

    pygame.quit()

# v = 34m/s
# theta = 40 deg
# R = (V ** 2 sin 2 * theta)/g
# H = (V ** 2 sin ^2 theta)/2g


def drawTangent(angle):
    grav = 9.81
    Vel = 34
    H = ((Vel ** 2) * (math.sin(2 * angle))) / grav
    R = ((Vel ** 2) * (math.sin(angle) ** 2)) / (2 * grav)

    initPosX = 500
    initPosY = 500

    pygame.draw.line(game_window, [255, 255, 255], [initPosX, initPosY], [initPosX + R, initPosY + H])



if __name__ == '__main__':
    startProgram()