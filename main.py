import pygame
from pygame.locals import *
from sys import exit
from random import randint

def main():
    pygame.init()

    bg_music = pygame.mixer.music.load('data/sfx/BoxCat_Games_-_CPU_Talk.mp3')
    pygame.mixer.music.play(-1)
    
    screen_width = 640
    screen_height = 480

    x = screen_width / 2
    y = screen_height / 2

    x_blue = randint(40, 600)
    y_blue = randint(50, 430)
 
    points = 0
    font = pygame.font.SysFont('arial', 40, True, True)

    
    

    logo = pygame.image.load('data/ufx/teste.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sadge")
    clock = pygame.time.Clock()

    

    screen = pygame.display.set_mode((screen_width, screen_height))



    running = True
    
    while running:
        clock.tick(50)
        screen.fill((0,0,0))
        mensagem = f'Pontos: {points}'
        text_format = font.render(mensagem, True, (255, 255, 255))
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == K_a:
            #         x = x - 20
            #     if event.key == K_d:
            #         x = x + 20
            #     if event.key == K_w:
            #         y = y - 20
            #     if event.key == K_s:
            #         y = y + 20


        if pygame.key.get_pressed()[K_a]:
            x = x - 10
        if pygame.key.get_pressed()[K_d]:
             x = x + 10
        if pygame.key.get_pressed()[K_w]:
            y = y - 10
        if pygame.key.get_pressed()[K_s]:
            y = y + 10

        sprite_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
        sprite_blue = pygame.draw.rect(screen, (0, 0, 255),(x_blue, y_blue, 40, 50))

        if sprite_red.colliderect(sprite_blue):
            x_blue = randint(40, 600)
            y_blue = randint(50, 430)
            points = points + 1

        screen.blit(text_format, (430, 20))
        pygame.display.update()

if __name__ == "__main__":
    main()