import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    time = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        player.draw(screen)
        pygame.display.flip()
        
    
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()