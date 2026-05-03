import pygame as pg
from sys import exit
pg.init()
width=1000
height=500
screen=pg.display.set_mode((width,height))
pg.display.set_caption("Escape Run  ")#change the name in the caption
clock=pg.time.Clock()#it's going to help with the frame rate 
test_surface=pg.image.load("Image/Sky.png")
test_surface.fill("White")
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()#tell python to shut down all the pygame moudel 
            exit()#telling python to stop running the entire file
    screen.blit(test_surface,(200,100))
    pg.display.update()
    clock.tick(60)#Consistent Game Speed