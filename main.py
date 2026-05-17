import pygame as pg
from sys import exit
import random

pg.init()
pg.mixer.init()
width=1000
height=500
game_active=False
coin_sound=pg.mixer.Sound("Sound/sound.wav")
game_over_sound=pg.mixer.Sound("Sound/game_over.wav")
Jump_sound=pg.mixer.Sound("Sound/jump.wav")
win_sound=pg.mixer.Sound("Sound/win.wav")
def start_game():
    print("Game Started")

def display_score():
    score_image=font.render(f"{score}",False,"Black")
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
enemy_image=pg.transform.scale(enemy_image,(95,65))
enemy_rect=enemy_image.get_rect(midbottom=(800,400))
player1=pg.image.load("Image/Player/Player1.png").convert_alpha()
player1=pg.transform.scale(player1,(120,95))
door_image=pg.image.load("Image/door.png").convert_alpha()
door_image=pg.transform.scale(door_image,(100,200))
door_rect=door_image.get_rect(center=(900,300))
move=50
win_played = False
greating=font.render("Hi To the Escape game... Press shift to start",False,(34,54,21))
player3=pg.image.load("Image/Player/Player3.png").convert_alpha()
player3=pg.transform.scale(player3,(300,300))
player3_rect=player3.get_rect(center=(100,300))
coins=pg.image.load("Image/coins.png").convert_alpha()
coins=pg.transform.scale(coins,(70,70))
player2=pg.image.load("Image/Player/Player2.png").convert_alpha()
start_time=0
player1_rect=player1.get_rect(midbottom=(move,400))
score=0
enemy_x_position=800
game_over=font.render("Game over. Press space to play again =) ", False,"Black")
game_end=font.render("#Press enter to exite the game =) ", False,"Black")
player_gravity=0
coins_rect=[]
for i in range(90):
    coin_rect=coins.get_rect(midbottom=(100+ i * 200,300))#the i represent the space betwen each coin
    coins_rect.append(coin_rect)
enemy_rects=[]    
for i in range(4):
    enemy_rect=enemy_image.get_rect(midbottom=(800+i*300,400))
    enemy_rects.append(enemy_rect)

while True:
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()#tell python to shut down all the pygame moudel 
            exit()#telling python to stop running the entire file
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RSHIFT:
                game_active=True
                start_time = int(pg.time.get_ticks() / 1000)
            if game_active: #if the game is runing    
                if event.type==pg.KEYDOWN:
                    if player1_rect.bottom>=380:# the player can't jump until the player tuch the ground 
                        if event.key==pg.K_UP:
                            player_gravity=-24
                            Jump_sound.play()              
            else:#if the game is not runing 
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        pg.quit()
                        exit()
                    if event.key==pg.K_SPACE:
                        game_active=True
                        enemy_rect.left=1000 
                        start_time=int(pg.time.get_ticks()/1000)
                        score=0
                        win_played=False
                        coins_rect=[]
                        for i in range(90):
                            coin_rect=coins.get_rect(midbottom=(100+ i * 200,350))#the i represent the space betwen each coin
                            coins_rect.append(coin_rect)
                        enemy_rects=[]    
                        for i in range(4):
                            enemy_rect=enemy_image.get_rect(midbottom=(800+i*300,400))
                            enemy_rects.append(enemy_rect)
                        player_gravity = 0
    
                        player1_rect.midbottom = (move, 400)
    if  not game_active and start_time==0:
        screen.fill((120,225,225))
        screen.blit(greating,(230,300))
        screen.blit(player3,player3_rect)
    elif game_active==True:            
        screen.blit(sky_imaage,(0,0))
        screen.blit(ground_image,(0,340))
        screen.blit(door_image,door_rect)
        if player1_rect.colliderect(door_rect):
            game_active=False
            if not win_played:
                win_sound.play()
                win_played = True

        #enemy_x_position-=6
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            player1_rect.x -= 3

        if keys[pg.K_RIGHT]:
            player1_rect.x += 3
        for coin_rect in coins_rect[:]:
            screen.blit(coins, coin_rect)

            coin_rect.x -= 2

            if coin_rect.right <= 0:
                coin_rect.left = 1000
            if player1_rect.colliderect(coin_rect):
                coins_rect.remove(coin_rect)
                score += 1
                coin_sound.play()
        for enemy_rect in enemy_rects[:]:
            screen.blit(enemy_image, enemy_rect)

            enemy_rect.x -= 2

            if enemy_rect.right <= 0:
                enemy_rect.left = 1000 
            enemy_hitbox = enemy_rect.inflate(-80, -40)
            if enemy_hitbox.colliderect(player1_rect):#if the player touch the enemy
                game_over_sound.play()
                game_active=False     
        screen.blit(enemy_image,(enemy_rect))
        player_gravity+=1
        player1_rect.y+=player_gravity
        if player1_rect.bottom>=380:#If the player's bottom is at 380, they are standing on the ground.
            player1_rect.bottom=380#if it is bigger it is inside the ground 
        screen.blit(player1,player1_rect)
        display_score()
    else:
        screen.fill((120,225,225))
        screen.blit(game_over,(200,height/2))
        screen.blit(game_end,(200,height/2+50))
        screen.blit(player2,(100,200))
        score_massege=font.render(f"Your Score is {score}",False,(0,0,0))
        score_massege_rect=score_massege.get_rect(center=(500,100))
        screen.blit(score_massege,score_massege_rect)
        if player1_rect.colliderect(door_rect):
            screen.fill((120,225,225))
            game_over=font.render("   You Win =)...Press Enter to exit the game :) ", False,"Black")
            screen.blit(game_over,(250,height/2))
            screen.blit(player3,player3_rect)

 
    pg.display.update()
    clock.tick(60)#Consistent Game Speed