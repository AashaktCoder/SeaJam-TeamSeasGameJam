import pygame
import time
from random import randint

pygame.init()

HEIGHT, WIDTH = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def Main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    last_time = time.time()

    # Position Variables
    PlayerX = 100
    PlayerY = 400

    # Physics Variables
    VelX = 6
    Direction = 1
    VelY = 4

    TrashList = []
    Health = 2

    # Functions
    def SpawnTrash():
        global TrashX
        global TrashY
        TrashX = randint(0, 450)
        TrashY = 50
        Trash = [TrashX, TrashY, 50, 50]
        return Trash

    def Text(msg, x, y, color, fontsize):
        font = pygame.font.Font("BoyzRGrossNF.ttf", fontsize)
        text = font.render(msg, True, color)
        WIN.blit(text, (x, y))

    while run:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # Drawing Everything
        WIN.fill((255, 255, 255))
        Player = pygame.draw.rect(WIN, (0, 0, 0), [PlayerX, PlayerY, 50, 50])
        Text(f"Health: {Health}", 0, 0, (0, 0, 0), 30)
        for TrashPosition in TrashList:
            Trash = pygame.draw.rect(WIN, (0, 0, 255), TrashPosition)
            TrashPosition[1] += VelY * dt
            if Player.colliderect(TrashPosition):
                TrashList.clear()
                Health -= 1
            if TrashPosition[1] >= 500:
                TrashList.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and PlayerX <= HEIGHT-50:
            Direction = 1
            PlayerX += VelX * Direction * dt
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and PlayerX >= 0:
            Direction = -1
            PlayerX += VelX * Direction * dt
        RandomTrash = randint(0, 10)
        if (RandomTrash > 5 and len(TrashList) <= 5):
            TrashPos = SpawnTrash()
            TrashList.append(TrashPos)
        if Health <= 0:
            run = False
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(FPS)


Main()
