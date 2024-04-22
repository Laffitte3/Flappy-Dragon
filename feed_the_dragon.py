import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set text
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Flappy Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

#Background
bg_image=pygame.image.load("flappy.png")
bg_image=pygame.transform.scale(bg_image,(WINDOW_WIDTH,WINDOW_HEIGHT))


game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#Set sounds and music
coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("ftd_background_music.wav")

#Set images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

#Pendiente aca
altura_tubo=[150,200,300]
random_altura=random.choice(altura_tubo)



tubo1_image = pygame.image.load("pipe1.png")
tubo1_image =pygame.transform.scale(tubo1_image,(70,random_altura))
tubo1_rect = tubo1_image.get_rect()
tubo1_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
tubo1_rect.y = 0

tubo2_image = pygame.image.load("pipe2.png")
tubo2_image =pygame.transform.scale(tubo2_image,(70,300))
tubo2_rect = tubo2_image.get_rect()
tubo2_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
tubo2_rect.y = random.randint(400,WINDOW_HEIGHT-100)


#The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:


    player_rect.y += 5
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Check to see if the user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    

    #Pediente ACA
    if (tubo1_rect.x < 0) and (tubo2_rect.x < 0):

        score +=1

        random_altura=random.choice(altura_tubo)

        tubo1_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        tubo1_rect.y = 0
        tubo1_image =pygame.transform.scale(tubo1_image,(70,random_altura))

        tubo2_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        tubo2_rect.y = random.randint(400,WINDOW_HEIGHT-100)
        

    else:
        #Move the coin
        tubo1_rect.x -= coin_velocity
        tubo2_rect.x -= coin_velocity

    #Check for collisions = game over
    
    if (player_rect.colliderect(tubo1_rect)) or (player_rect.colliderect(tubo2_rect)):


        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_rect.y = WINDOW_HEIGHT//2
                    tubo2_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
                    tubo1_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False

                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    #Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

    

    #Fill the display
    display_surface.blit(bg_image,(0,0))

    #Blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    

    #Blit assets to screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(tubo1_image, tubo1_rect)
    display_surface.blit(tubo2_image, tubo2_rect)

    #Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()