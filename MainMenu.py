import pygame


def Menu(WIN, Text):
    run1 = True
    FPS = 60
    clock = pygame.time.Clock()
    while run1:
        WIN.fill((39, 141, 232))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(FPS)
