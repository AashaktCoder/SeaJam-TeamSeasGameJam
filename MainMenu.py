import pygame


def Menu(WIN, Text, Main):
    run1 = True
    FPS = 60
    clock = pygame.time.Clock()
    while run1:
        mouse = pygame.mouse.get_pos()
        WIN.fill((39, 141, 232))
        Text("Dodge The Trash", 10, 25, (0, 0, 0), 100)
        pygame.draw.rect(WIN, (0, 0, 0), [175, 218, 150, 75], 8, 10)
        Text("Play", 215, 223, (0, 0, 0), 50)
        if 175+150 > mouse[0] > 175 and 218+75 > mouse[1] > 218:
            pygame.mouse.set_cursor(
                *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            if pygame.mouse.get_pressed()[0]:
                pygame.mouse.set_cursor(
                    *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                Main()
        else:
            pygame.mouse.set_cursor(
                *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)) 
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                pygame.quit()
                quit()       
        pygame.display.update()
        clock.tick(FPS)
