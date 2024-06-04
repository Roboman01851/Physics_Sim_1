import pygame, pgzrun, math, time, settings


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

        vertices = [
            [
                (center_x + radius * math.cos(rotation + (2 * math.pi * i / vertex_count))),
                (center_y + radius * math.sin(rotation + (2 * math.pi * i / vertex_count))),
            ]
            for i in range(vertex_count)
        ]

        pygame.draw.polygon(game_window, [255, 255, 255], )

        game_window.fill((0, 0, 0))




        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    startProgram()