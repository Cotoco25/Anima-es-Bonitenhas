from pygame import *
import sys

from pygame.locals import QUIT, KEYDOWN

clock = time.Clock()

kirk_img = image.load("kirky.gif")
speed_img = image.load("speedy_fofo.gif")
speed_laser_img = image.load("speedy.gif")
grass_img = image.load("grass.png")
grass_img = transform.scale(grass_img, (800, 400))
ceu_img = image.load("ceunovo.jpg")
ceu_img = transform.scale(ceu_img, (800, 400))

loc_x = 0
loc_y = 400

hero_img = image.load("assets/assets/Hero_walk_01.png")

hero_standard = image.load("assets/assets/Hero_walk_14.png")


run_animation = False
run_animation_d = False
run_animation_backwards = False
run_animation_up = False
run_animation_down = False
current_frame = 0
anim_time = 0
anim_time_d = 0
kirk_walk_list = []
for i in range(4):
    kirk_walk_list.append(image.load(f"assets/assets/Hero_walk_0{i+1}.png"))

kirk_walk_list_2 = []
for i in range(4):
    kirk_walk_list_2.append(image.load(f"assets/assets/Hero_walk_0{i+5}.png"))

kirk_walk_list_up = []
for i in range(4):
    kirk_walk_list_up.append(image.load(f"assets/assets/Hero_walk_{i+9}.png"))

kirk_walk_list_down = []
for i in range(4):
    kirk_walk_list_down.append(image.load(f"assets/assets/Hero_walk_{i+13}.png"))

current_frame_gui = 0
anim_time_gui = 0
gui_receba_farinha = image.load("assets/assets/Hero_walk_01.png")


init()
screen = display.set_mode((800,600))
display.set_caption("Welkirk home")

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

    run_animation = False
    run_animation_backwards = False
    run_animation_up = False
    run_animation_down = False


    #run_animation = False
    keys = key.get_pressed()
    clock.tick(60)
    dt = clock.get_time()
    
    if keys[K_d] and loc_x<710:
        loc_x = loc_x+2
        run_animation = True

    if keys[K_a] and loc_x>-40:
        loc_x = loc_x-2
        run_animation_backwards = True

    if keys[K_w] and loc_y > 300:
        loc_y = loc_y - 2
        run_animation_up = True

    if keys[K_s] and loc_y < 480:
        loc_y = loc_y + 2
        run_animation_down = True

    anim_time = anim_time + dt
    #print(anim_time)
    anim_time_sec = anim_time/1000

    anim_time_d = anim_time_d + dt
    anim_time_sec_d = anim_time_d/1000

    if run_animation or run_animation_backwards or run_animation_up or run_animation_down:
        if anim_time_sec > 0.15:  
            current_frame += 1
            
            if run_animation and current_frame > len(kirk_walk_list) - 1:
                current_frame = 0 
            elif run_animation_backwards and current_frame > len(kirk_walk_list_2) - 1:
                current_frame = 0 
            elif run_animation_up and current_frame > len(kirk_walk_list_up) - 1:
                current_frame = 0 
            elif run_animation_down and current_frame > len(kirk_walk_list_down) - 1:
                current_frame = 0 
            anim_time = 0
    else:
        current_frame = 0
        anim_time = 0


    #desenha
    screen.fill((155,155,155))

    #screen blit elementos da tela
    screen.blit(ceu_img, (0,0))
    #screen.blit(kirk_img, (550,100))
    #screen.blit(speed_img, (100,100), (100,100,200,200)) #o tamanho funciona de indo da cordenada 100,100 com o tamanho 200,200
    #screen.blit(speed_laser_img, (400,300))
    screen.blit(grass_img, (0,200))


    #animacao
    if run_animation == True and run_animation_backwards == False and run_animation_up == False and run_animation_down == False:
        screen.blit(kirk_walk_list[current_frame], (loc_x,loc_y))
    if run_animation_backwards == True and run_animation == False and run_animation_up == False and run_animation_down == False:
        screen.blit(kirk_walk_list_2[current_frame], (loc_x,loc_y))
    if run_animation_up:
        screen.blit(kirk_walk_list_up[current_frame], (loc_x,loc_y))
    if run_animation_down:
        screen.blit(kirk_walk_list_down[current_frame], (loc_x,loc_y))
    if run_animation == False and run_animation_backwards == False and run_animation_up == False and run_animation_down == False:
        screen.blit(hero_standard, (loc_x,loc_y))
    if run_animation == True and run_animation_backwards == True and run_animation_up == False and run_animation_down == False:
        screen.blit(hero_standard, (loc_x,loc_y))


    display.update()