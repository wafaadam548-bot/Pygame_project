import pygame as pg
from sys import exit
import random
pg.init()
width=1000
hieght=500
screen=pg.display.set_mode((width,hieght))
Caption=pg.display.set_caption("Game World ")
font=pg.font.Font("Font/Archivo_Black/ArchivoBlack-Regular.ttf",30)
greating=font.render("""Hi To the game world choose what game do you want to play
                      """,False,(34,54,21))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
    screen.blit(greating,(100,200))        

    pg.display.update()
