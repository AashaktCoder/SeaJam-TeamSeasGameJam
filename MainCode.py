import pygame
import time
from random import randint
from MainMenu import Menu

pygame.init()

HEIGHT, WIDTH = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Trash")
Icon = pygame.image.load("Images\\Logo.png")
Icon = pygame.transform.scale(Icon, (32, 32))
pygame.display.set_icon(Icon)


def Text(msg, x, y, color, fontsize):
    font = pygame.font.Font("BoyzRGrossNF.ttf", fontsize)
    text = font.render(msg, True, color)
    WIN.blit(text, (x, y))


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
    CoinList = []
    FoodList = []
    CoinCollect = 0
    Health = 2

    # Functions
    def SpawnObjects():
        global ObjectX
        global ObjectY
        ObjectX = randint(0, 450)
        ObjectY = randint(-100, 0)
        Object = [ObjectX, ObjectY, 50, 50]
        return Object

    # Loading the Images
    FishImage = pygame.image.load("Images\\Fish.png").convert_alpha()
    FishImage = pygame.transform.scale(FishImage, (60, 60))
    TrashImages = [pygame.image.load("Images\\Bottle.png").convert_alpha()]
    CoinImage = pygame.image.load("Images\\Coin.png").convert_alpha()
    FoodImage = pygame.image.load("Images\\Food.png").convert_alpha()
    PlayerMask = pygame.mask.from_surface(FishImage)
    TrashMask = pygame.mask.from_surface(TrashImages[0])

    # Reading from files
    CoinFile = open("Coins.txt", 'r')
    CoinNumber = int(CoinFile.read())
    CoinFile.close()
    HighScoreFile = open("HighScore.txt", 'r')
    HighScore = HighScoreFile.read()
    HighScoreFile.close()
    Score = 0
    DifficultyFile = open("Difficulty.txt", 'r')
    DifficultyLevel = int(DifficultyFile.read())
    DifficultyFile.close()

    while run:
        mouse = pygame.mouse.get_pos()
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # Drawing Everything
        WIN.fill((39, 141, 232))
        Player = WIN.blit(FishImage, (PlayerX, PlayerY))
        Text(f"Health: {Health}", 0, 0, (0, 0, 0), 30)
        Text(f"Coins: {CoinNumber+CoinCollect}", 100, 0, (0, 0, 0), 30)
        Text(f"HighScore: {HighScore}", 0, 30, (0, 0, 0), 30)
        Text(f"Score: {Score}", 0, 60, (0, 0, 0), 30)
        pygame.draw.rect(WIN, (0, 0, 0), [400, 0, 100, 50], 5, 10)
        Text("Menu", 418, 8, (0, 0, 0), 30)
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
                TrashList.pop(len(TrashList)-1)
                Score += 1
        for CoinPosition in CoinList:
            Coin = WIN.blit(CoinImage, (CoinPosition[0], CoinPosition[1]))
            CoinPosition[1] += VelY * dt
            if Player.colliderect(Coin):
                CoinCollect += 1
                CoinFile = open("Coins.txt", 'w')
                CoinFile.write(str(CoinNumber+CoinCollect))
                CoinFile.close()
                CoinList.pop(len(CoinList) - 1)
            if CoinPosition[1] >= 500:
                CoinList.pop(len(CoinList) - 1)
        for FoodPosition in FoodList:
            Food = WIN.blit(FoodImage, (FoodPosition[0], FoodPosition[1]))
            FoodPosition[1] += VelY * dt
            if Player.colliderect(Food):
                FoodList.clear()
                Health += 1
            if FoodPosition[1] >= 500:
                FoodList.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and PlayerX <= HEIGHT-50:
            Direction = 1
            PlayerX += VelX * Direction * dt
            FishImage = pygame.image.load("Images\\Fish2.png").convert_alpha()
            FishImage = pygame.transform.scale(FishImage, (60, 60))
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and PlayerX >= 0:
            Direction = -1
            PlayerX += VelX * Direction * dt
            FishImage = pygame.image.load("Images\\Fish.png").convert_alpha()
            FishImage = pygame.transform.scale(FishImage, (60, 60))
        RandomTrash = randint(0, 1000)
        if (RandomTrash > DifficultyLevel and len(TrashList) <= 10):
            TrashPos = SpawnObjects()
            TrashList.insert(0, TrashPos)
        if (RandomTrash > 995 and len(CoinList) < 2):
            CoinPos = SpawnObjects()
            CoinList.insert(0, CoinPos)
        if (RandomTrash > 997 and len(FoodList) < 1):
            FoodPos = SpawnObjects()
            FoodList.insert(0, FoodPos)
        if Health <= 0:
            Menu(WIN, Text, Main)
            CoinFile.write(str(CoinNumber))
            CoinFile.truncate()
            CoinFile.close()
        if Score > int(HighScore):
            HighScore = Score
            f = open("HighScore.txt", 'w')
            f.write(str(HighScore))
            f.close()
        if 500 > mouse[0] > 400 and 50 > mouse[1] > 0:
            if pygame.mouse.get_pressed()[0]:
                Menu(WIN, Text, Main)
        pygame.display.update()
        clock.tick(FPS)


# Running the Functions
Menu(WIN, Text, Main)
