import pygame

from constans import *

pygame.init()


display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
pygame.display.set_caption(NAME_WINDOW)

icon = pygame.image.load(ICON_WINDOW)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

usr_width = 60
usr_height = 100
usr_x = DISPLAY_WIDTH // 3
usr_y = DISPLAY_HEIGTH -(100 + usr_height)

make_jump = False
jump_counter = 30


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # or exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

            if make_jump:
                jump()

        display.fill(COLORS.WHITE)

        pygame.draw.rect(display, COLORS.GREEN, (usr_x, usr_y, usr_width, usr_height))
        pygame.display.update()
        clock.tick(FPS)


def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


if __name__ == "__main__":
    run_game()
