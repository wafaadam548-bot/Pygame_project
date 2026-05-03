import pygame as pg
from sys import exit
pg.init()
width=1000
height=500
screen=pg.display.set_mode((width,height))
pg.display.set_caption("Escape Run  ")#change the name in the caption
clock=pg.time.Clock()#it's going to help with the frame rate 
sky_imaage=pg.image.load("Image/sky.jpg")
sky_imaage=pg.transform.scale(sky_imaage,(1000,400))#resize the image
ground_image=pg.image.load("Image/ground.png")
ground_image=pg.transform.scale(ground_image,(1000,260))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()#tell python to shut down all the pygame moudel 
            exit()#telling python to stop running the entire file
    screen.blit(sky_imaage,(0,0))
    screen.blit(ground_image,(0,300))
    pg.display.update()
    clock.tick(60)#Consistent Game Speed