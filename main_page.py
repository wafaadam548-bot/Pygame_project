import pygame as pg
from sys import exit
import random
import main
pg.init()
width=1000
hieght=500
screen=pg.display.set_mode((width,hieght))
Caption=pg.display.set_caption("Game World ")
font=pg.font.Font("Font/Archivo_Black/ArchivoBlack-Regular.ttf",30)
greating=font.render("""Hi To the Escape game... Press shift to start 
                      """,False,(34,54,21))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RSHIFT or event.key==pg.K_LSHIFT:
                #import the game file 
                main.start_game()
    screen.blit(greating,(100,200))        

    pg.display.update()
