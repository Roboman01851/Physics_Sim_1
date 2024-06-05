import pygame, math, time, settings, numpy


pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()
def startProgram():
    running = True
    center_x, center_y = settings.width // 2, settings.height // 2
    radius = 100


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

        drawTangent()

        pygame.display.flip()

    pygame.quit()


def drawTangent():

    xVect = [100, math.cos(50)]
    yVect = [100, math.sin(0)]
    print(numpy.cross(xVect, yVect))


    pygame.draw.line(game_window, [255, 255, 255], [500, 500], [500 + numpy.cross(xVect, yVect), 500 + numpy.cross(xVect, yVect)])

if __name__ == '__main__':
    startProgram()