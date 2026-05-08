import pygame as pg
from sys import exit
pg.init()
width=1000
height=500
game_active=True
def display_score():
    time=int(pg.time.get_ticks()/1000)-start_time
    score_image=font.render(f"{time}",False,"Black")
    score_rect=score_image.get_rect(center=(400,50))
    screen.blit(score_image,score_rect)




screen=pg.display.set_mode((width,height))
pg.display.set_caption("Escape Run  ")#change the name in the caption
clock=pg.time.Clock()#it's going to help with the frame rate 
font=pg.font.Font("Font/Archivo_Black/ArchivoBlack-Regular.ttf",30)
sky_imaage=pg.image.load("Image/sky.jpg").convert_alpha()
sky_imaage=pg.transform.scale(sky_imaage,(1000,400))#resize the image
ground_image=pg.image.load("Image/ground.png").convert_alpha()
ground_image=pg.transform.scale(ground_image,(1000,270))
enemy_image=pg.image.load("Image/enemy.png").convert_alpha() #pygame is going to work with conver.alpha faster 
enemy_image=pg.transform.scale(enemy_image,(130,105))
enemy_rect=enemy_image.get_rect(midbottom=(800,400))
player1=pg.image.load("Image/Player/Player1.png").convert_alpha()
player1=pg.transform.scale(player1,(100,75))
move=50
player2=pg.image.load("Image/Player/Player2.png").convert_alpha()
start_time=0
player1_rect=player1.get_rect(midbottom=(move,400))
score=display_score()
enemy_x_position=800
game_over=score.render("Game over. Press space to play again =) ", False,"Black")
player_gravity=0
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()#tell python to shut down all the pygame moudel 
            exit()#telling python to stop running the entire file
        if game_active: #if the game is runing    
            if event.type==pg.KEYDOWN:
                if player1_rect.bottom>=380:# the player can't jump until the player tuch the ground 
                    if event.key==pg.K_UP:
                        player_gravity=-20
                if event.key==pg.K_LEFT:
                    player1_rect.right-=3  
                if event.key==pg.K_RIGHT:
                    player1_rect.right+=3
                    
        else:#if the game is not runing 
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    game_active=True
                    enemy_rect.left=1000 
                    start_time=int(pg.time.get_ticks()/1000)
    if game_active:            
        screen.blit(sky_imaage,(0,0))
        screen.blit(ground_image,(0,340))
        #enemy_x_position-=6
        screen.blit(enemy_image,(enemy_rect))
        player_gravity+=1
        player1_rect.y+=player_gravity
        if player1_rect.bottom>=380:
            player1_rect.bottom=380
        screen.blit(player1,player1_rect)
        display_score()
        enemy_rect.left-=4
        if enemy_rect.right<=-0:
            enemy_rect.left=1000
        if enemy_rect.colliderect(player1_rect):#if the player touch the enemy
            game_active=False
    else:
        screen.fill((120,225,225))
        screen.blit(game_over,(200,height/2))
        screen.blit(player2,(100,200))

    pg.display.update()
    clock.tick(60)#Consistent Game Speed