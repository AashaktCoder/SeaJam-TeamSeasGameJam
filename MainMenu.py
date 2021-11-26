import pygame


def Menu(WIN, Text, Main):
    run1 = True
    FPS = 60
    clock = pygame.time.Clock()

    def MouseClick(x, y, width, height, mouse, Func):
        if x+width > mouse[0] > x and y+height > mouse[1] > y:
            pygame.mouse.set_cursor(
                *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            if pygame.mouse.get_pressed()[0]:
                pygame.mouse.set_cursor(
                    *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                Func()
        else:
            pygame.mouse.set_cursor(
                *pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

    def Difficulty(run1):
        run2 = True
        run1 = False

        def SetDifficulty(number):
            f = open("Difficulty.txt", 'w')
            f.write(str(number))
            f.close
        while run2:
            mouse = pygame.mouse.get_pos()
            WIN.fill((39, 141, 232))
            Text("Difficulty", 50, 25, (0, 0, 0), 100)
            pygame.draw.rect(WIN, (0, 0, 0), [175, 140, 150, 75], 8, 10)
            Text("Easy", 215, 150, (0, 0, 0), 50)
            pygame.draw.rect(WIN, (0, 0, 0), [175, 220, 150, 75], 8, 10)
            Text("Medium", 193, 230, (0, 0, 0), 50)
            pygame.draw.rect(WIN, (0, 0, 0), [175, 300, 150, 75], 8, 10)
            Text("Hard", 197, 310, (0, 0, 0), 50)
            pygame.draw.rect(WIN, (0, 0, 0), [160, 380, 180, 75], 8, 10)
            Text("Impossible", 168, 390, (0, 0, 0), 50)
            pygame.draw.rect(WIN, (0, 0, 0), [350, 0, 150, 75], 8, 10)
            Text("Back", 378, 8, (0, 0, 0), 50)
            MouseClick(350, 0, 150, 75, mouse, lambda: Menu(WIN, Text, Main))
            MouseClick(175, 140, 150, 75, mouse, lambda: SetDifficulty(985))
            MouseClick(175, 220, 150, 75, mouse, lambda: SetDifficulty(945))
            MouseClick(175, 300, 150, 75, mouse, lambda: SetDifficulty(900))
            MouseClick(160, 380, 180, 75, mouse, lambda: SetDifficulty(850))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                    pygame.quit()
                    quit()
            pygame.display.update()

    while run1:
        mouse = pygame.mouse.get_pos()
        WIN.fill((39, 141, 232))
        Text("Dodge The Trash", 10, 25, (0, 0, 0), 100)
        pygame.draw.rect(WIN, (0, 0, 0), [175, 218, 150, 75], 8, 10)
        Text("Play", 215, 223, (0, 0, 0), 50)
        pygame.draw.rect(WIN, (0, 0, 0), [165, 300, 170, 75], 8, 10)
        Text("Difficulty", 173, 310, (0, 0, 0), 50)
        MouseClick(175, 218, 150, 75, mouse, Main)
        MouseClick(175, 300, 150, 75, mouse, lambda: Difficulty(run1))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(FPS)
