import pygame
from random import randrange 
pygame.init()

frame=0
map_width=284
map_height=512
FPS=60
pipes=[[150,4]]

gameScreen = pygame.display.set_mode((map_width,map_height))
clock=pygame.time.Clock()

bird_wing_up = pygame.image.load("images/bird_wing_up.png")
bird_wing_down = pygame.image.load("images/bird_wing_down.png")
background = pygame.image.load("images/background.png")
pipe_body = pygame.image.load("images/pipe_body.png")
pipe_end = pygame.image.load("images/pipe_end.png")

def draw_pipes():
    global pipes
    for n in range( len(pipes) ):
        for m in range( pipes[n][1] ):
            gameScreen.blit( pipe_body , ( pipes[n][0] , m*32 ) )
        for m in range( pipes[n][1]+6 , 16 ):
            gameScreen.blit( pipe_body , ( pipes[n][0] , m*32 ) )
        gameScreen.blit( pipe_end , (pipes[n][0] , (pipes[n][1])*32 ) )
        gameScreen.blit( pipe_end , (pipes[n][0] , (pipes[n][1]+5)*32 ) )
        pipes[n][0] -= 1

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
        if len(pipes)<4:
            x = pipes[-1][0] + 200
            open_pos = randrange(1,9)
            pipes.append([x,open_pos])
        if pipes[0][0]<-100:
            pipes.pop(0)
        gameScreen.blit(background,(0,0))
        draw_bird(20,map_height//2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                pygame.quit() 
                return 
        draw_pipes()
        pygame.display.update()
        clock.tick(FPS)
gameLoop()