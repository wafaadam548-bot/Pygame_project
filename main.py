import pygame as pg
from sys import exit
pg.init()
width=1000
height=500
pg.display.set_mode((width,height))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()