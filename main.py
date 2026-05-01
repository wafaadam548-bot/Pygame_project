import pygame as pg
pg.init()
width=1000
height=500
pg.display.set_mode((width,height))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
    pg.display.update()