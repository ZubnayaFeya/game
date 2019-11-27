import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGTH = 640
NAME_WINDOW = 'My first game'
ICON_WINDOW = 'ico.png'

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
pygame.display.set_caption(NAME_WINDOW)

icon = pygame.image.load(ICON_WINDOW)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        display.fill((255, 255, 255))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
