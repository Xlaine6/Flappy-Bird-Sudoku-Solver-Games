import pygame
pygame.init()

frame=0
map_width=284
map_height=512
FPS=60

gameScreen = pygame.display.set_mode((map_width,map_height))
clock=pygame.time.Clock()

bird_wing_up = pygame.image.load("images/bird_wing_up.png")
bird_wing_down = pygame.image.load("images/bird_wing_down.png")
background = pygame.image.load("images/background.png")

def draw_bird(x,y):
    global frame
    if 0<=frame<=30: 
            gameScreen.blit(bird_wing_up,(x,y))
            frame += 1
    elif  30<frame<=60 :
            gameScreen.blit(bird_wing_down,(x,y))
            frame += 1
            if frame==60 : frame=0

def gameLoop():
    while True: 
        gameScreen.blit(background,(0,0))
        draw_bird(20,map_height//2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                pygame.quit() 
                return 
        pygame.display.update()
        clock.tick(FPS)
gameLoop()