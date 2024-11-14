import pygame

import random
def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x=0
        y=0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if x<=event.pos[0]<=32+x and y<=event.pos[1]<=y+32:
                        x=random.randrange(0,20)*32
                        y = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range(1, 16):
                pygame.draw.line(screen, (127, 127, 127), (0, i * 32), (640, i * 32))
            for j in range(1, 20):
                pygame.draw.line(screen, (127, 127, 127), (j * 32, 0), (j * 32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
