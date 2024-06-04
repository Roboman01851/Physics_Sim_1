import pygame, pgzrun,  math, time, settings, vpython


pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()
def startProgram():
    running = True

    ground = settings.height - 60
    center_x, center_y = settings.width // 2, settings.height // 2

    while running:


        radius = 100
        vertex_count = 4

        vertex_max = 100
        vertex_min = 3
        rotation = 1

        shape_color = [255, 255, 255]


        button_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        game_window.fill((0, 0, 0))


        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    startProgram()