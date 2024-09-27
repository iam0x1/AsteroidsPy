import pygame
import constants


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        pygame.display.flip()

if __name__ == "__main__":
    main()