import pygame
import time
from random import randint

pygame.init()

HEIGHT, WIDTH = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Trash")


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

    # Loading the Images
    FishImage = pygame.image.load("Fish.png").convert_alpha()
    FishImage = pygame.transform.scale(FishImage, (60, 60))
    TrashImages = [pygame.image.load("Bottle.png").convert_alpha()]
    Background = pygame.image.load("Background.png").convert_alpha()
    PlayerMask = pygame.mask.from_surface(FishImage)
    TrashMask = pygame.mask.from_surface(TrashImages[0])

    while run:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # Drawing Everything
        WIN.fill((255, 255, 255))
        Player = WIN.blit(FishImage, (PlayerX, PlayerY))
        Text(f"Health: {Health}", 0, 0, (0, 0, 0), 30)
        for TrashPosition in TrashList:
            Trash = WIN.blit(
                TrashImages[0], (TrashPosition[0], TrashPosition[1]))
            TrashPosition[1] += VelY * dt
            offset = (
                int(PlayerX-TrashPosition[0]), int(PlayerY-TrashPosition[1]))
            collision = PlayerMask.overlap(TrashMask, offset)
            if collision:
                TrashList.clear()
                Health -= 1
            if TrashPosition[1] >= 500:
                TrashList.clear()
        WIN.blit(Background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and PlayerX <= HEIGHT-50:
            Direction = 1
            PlayerX += VelX * Direction * dt
            FishImage = pygame.image.load("Fish2.png").convert_alpha()
            FishImage = pygame.transform.scale(FishImage, (60, 60))
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and PlayerX >= 0:
            Direction = -1
            PlayerX += VelX * Direction * dt
            FishImage = pygame.image.load("Fish.png").convert_alpha()
            FishImage = pygame.transform.scale(FishImage, (60, 60))
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
