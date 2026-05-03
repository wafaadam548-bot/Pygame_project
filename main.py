import pygame as pg
from sys import exit
pg.init()
width=1000
height=500
screen=pg.display.set_mode((width,height))
pg.display.set_caption("Escape Run  ")#change the name in the caption
clock=pg.time.Clock()#it's going to help with the frame rate 
score=pg.font.Font("Font/Archivo_Black/ArchivoBlack-Regular.ttf",50)
sky_imaage=pg.image.load("Image/sky.jpg").convert_alpha()
sky_imaage=pg.transform.scale(sky_imaage,(1000,400))#resize the image
ground_image=pg.image.load("Image/ground.png").convert_alpha()
ground_image=pg.transform.scale(ground_image,(1000,270))
enemy_image=pg.image.load("Image/enemy.png").convert_alpha() #pygame is going to work with conver.alpha faster 
enemy_image=pg.transform.scale(enemy_image,(130,105))
player1=pg.image.load("Image/Player/Player1.png").convert_alpha()
player1=pg.transform.scale(player1,(100,75))
player1_rect=player1.get_rect(topleft=(20,310))

enemy_x_position=800
score_image=score.render("Hi",False,"Black")
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()#tell python to shut down all the pygame moudel 
            exit()#telling python to stop running the entire file
    screen.blit(sky_imaage,(0,0))
    screen.blit(ground_image,(0,340))
    screen.blit(score_image,(width/2,height/2))
    enemy_x_position-=6
    screen.blit(enemy_image,(enemy_x_position,310))
    screen.blit(player1,player1_rect)
    if enemy_x_position<=-100:
        enemy_x_position=1000
    pg.display.update()
    clock.tick(60)#Consistent Game Speed