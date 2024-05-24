import pygame, math, time, settings

pygame.init()
game_window = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption(f"{settings.title}")
clock = pygame.time.Clock()
def startProgram():
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_window.fill((0, 0, 0))



if __name__ == '__main__':
    startProgram()