from pygame import *
import sys

from pygame.locals import QUIT, KEYDOWN

clock = time.Clock()

kirk_img = image.load("kirky.gif")
speed_img = image.load("speedy_fofo.gif")
speed_laser_img = image.load("speedy.gif")

loc_x = 0
loc_y = 0

hero_img = image.load("assets/assets/Hero_walk_01.png")

run_animation = False
run_animation_d = False
current_frame = 0
anim_time = 0
anim_time_d = 0
kirk_walk_list = []
for i in range(4):
    kirk_walk_list.append(image.load(f"assets/assets/Hero_walk_0{i+1}.png"))

current_frame_gui = 0
anim_time_gui = 0
gui_receba_farinha = image.load("assets/assets/Hero_walk_01.png")


init()
screen = display.set_mode((800,600))
display.set_caption("Welcome kirk")

while True:
    key_pressed = key.get_pressed()
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit
        #eventos do pygame
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                run_animation = True
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_d and loc_x<700:
                loc_x = loc_x+10
                run_animation_d = True


    #run_animation = False
    keys = key.get_pressed()
    clock.tick(60)
    dt = clock.get_time()
    
    if keys[K_a] and loc_x<710:
        loc_x = loc_x+2
        run_animation_d = True

    anim_time = anim_time + dt
    #print(anim_time)
    anim_time_sec = anim_time/1000

    anim_time_d = anim_time_d + dt
    anim_time_sec_d = anim_time_d/1000

    if run_animation_d:
        if anim_time_sec > 0.2:
            current_frame += 1
            if current_frame > len(kirk_walk_list) - 1:
                current_frame = 0
                run_animation = False
            anim_time = 0
        



    if run_animation:
        if anim_time_sec > 0.2:
            current_frame += 1
            if current_frame > len(kirk_walk_list) - 1:
                current_frame = 0
                run_animation = False
            anim_time = 0


    #desenha
    screen.fill((155,155,155))

    #screen blit elementos da tela
    screen.blit(kirk_img, (550,100))
    screen.blit(speed_img, (100,100), (100,100,200,200)) #o tamanho funciona de indo da cordenada 100,100 com o tamanho 200,200
    screen.blit(speed_laser_img, (400,300))



    #animacao
    screen.blit(kirk_walk_list[current_frame], (loc_x,loc_y))


    display.update()

