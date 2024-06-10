import pygame, math, time, settings, numpy


pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()
def startProgram():
    running = True
    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 20
    deg = 45
    angle = math.radians(deg)

    shape_color = [0 , 255, 255]
    ground_color = [0, 255, 0]

    ground = settings.height - 60
    startingPos = [center_x, center_y]

    t = 0

    while running:
        #clock.tick(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0, 0, 0))
        grav = 9.81
        Vel = 100

        R = ((Vel ** 2) * (math.sin(t / (2 * angle)))) / (grav)
        H = ((Vel ** 2) * ((math.sin(t / (angle))) ** 2)) / (2 * grav)

        yOffset = - H
        xOffset = - R

        x = (radius) - xOffset
        y = (ground - radius) + yOffset


        button_pressed = pygame.key.get_pressed()

        pygame.draw.circle(game_window, shape_color, [x, y], radius)

        pygame.draw.rect(game_window, ground_color, [(0, ground), (settings.width, settings.height)])


        if button_pressed[pygame.K_SPACE]:
            if t > 0 and yOffset > 0:
                t = 0
            
            if t >= 0:
                t += 1 / 60

            print(R)

            #print(f"x: {x}, y: {y}, t: {t}")
            time.sleep(1 / 60)


        pygame.display.flip()

    pygame.quit()

# v = 34m/s
# theta = 40 deg
# R = (V ** 2 sin 2 * theta)/g
# H = (V ** 2 sin ^2 theta)/2g


def drawTangent(angle):


    initPosX = 500
    initPosY = 500

    # pygame.draw.line(game_window, [255, 255, 255], [initPosX, initPosY], [initPosX + R, initPosY + H])



if __name__ == '__main__':
    startProgram()