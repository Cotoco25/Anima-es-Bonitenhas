import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

kirk_img = pygame.image.load("kirky.gif")
speed_img = pygame.image.load("speedy_fofo.gif")
speed_laser_img = pygame.image.load("speedy.gif")

hero_img = pygame.image.load("assets/assets/Hero_walk_01.png")

run_animation = False
current_frame = 0
anim_time = 0
kirk_walk_list = []
for i in range(4):
    kirk_walk_list.append(pygame.image.load(f"assets/assets/Hero_walk_0{i+1}.png"))

current_frame_gui = 0
anim_time_gui = 0
gui_receba_farinha = pygame.image.load("assets/assets/Hero_walk_01.png")


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Welcome kirk")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        #eventos do pygame
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_animation = True


    run_animation = False

    clock.tick(60)
    dt = clock.get_time()
    
    
    anim_time = anim_time + dt
    #print(anim_time)
    anim_time_sec = anim_time/1000

    if run_animation:
        if anim_time_sec > 0.2:
            current_frame += 1
            if current_frame > len(kirk_walk_list) - 1:
                current_frame = 0
            anim_time = 0


    #desenha
    screen.fill((155,155,155))

    #screen blit elementos da tela
    screen.blit(kirk_img, (550,100))
    screen.blit(speed_img, (100,100), (100,100,200,200)) #o tamanho funciona de indo da cordenada 100,100 com o tamanho 200,200
    screen.blit(speed_laser_img, (400,300))



    #animacao
    screen.blit(kirk_walk_list[current_frame], (0,0))


    pygame.display.update()

