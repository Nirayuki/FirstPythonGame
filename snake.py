import pygame
from pygame.locals import *
from sys import exit
from random import randint

def main():
    pygame.init()

    pygame.mixer.music.set_volume(0.15)
    bg_music = pygame.mixer.music.load('data/sfx/audio.wav')
    pygame.mixer.music.play(-1)

    coin_colision = pygame.mixer.Sound('data/sfx/normal-hitnormal.wav')
    
    screen_width = 640
    screen_height = 480

    x_snake = int(screen_width / 2)
    y_snake = int(screen_height / 2)

    velocity = 10
    x_control = velocity
    y_control = 0

    x_coin = randint(40, 600)
    y_coin = randint(50, 430)
 
    points = 0
    font = pygame.font.SysFont('arial', 40, True, True)

    
    

    logo = pygame.image.load('data/ufx/teste.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sadge")
    clock = pygame.time.Clock()
    snake_body = []
    initial_size = 5
    dead = False

    
    #Aqui é aonde eu faço a tela
    screen = pygame.display.set_mode((screen_width, screen_height))


    # Aqui eu pego a lógica do corpo da cobra
    
    def get_body(snake_body):
        for XandY in snake_body:
            pygame.draw.rect(screen, (0, 255,0), (XandY[0], XandY[1], 20, 20))

    
    while True:
        clock.tick(30)
        screen.fill((255,255,255))
        mensagem = f'Points: {points}'
        text_format = font.render(mensagem, True, (0, 0, 0))
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()

            #Aqui fica o tópico de movimento da cobra
            if event.type == pygame.KEYDOWN:

                if event.key == K_a:
                    if x_control == velocity:
                        pass
                    else:
                        x_control = -velocity
                        y_control = 0

                if event.key == K_d:
                    if x_control == -velocity:
                        pass
                    else:
                        x_control = velocity
                        y_control = 0

                if event.key == K_w:
                    if y_control == velocity:
                        pass
                    else:
                        y_control = -velocity
                        x_control = 0

                if event.key == K_s:
                    if y_control == -velocity:
                        pass
                    else:
                        y_control = velocity
                        x_control = 0

        x_snake = x_snake + x_control
        y_snake = y_snake + y_control

      

        #Aqui são os sprites da cobra e da moeda
        snake= pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 20, 20))
        coin = pygame.draw.rect(screen, (255, 0, 0),(x_coin, y_coin, 20, 20))

        
        # Aqui fica a colisão com a moeda
        
        if snake.colliderect(coin):
            x_coin = randint(40, 600)
            y_coin = randint(50, 430)
            points = points + 1
            coin_colision.play()
            initial_size = initial_size + 1


        #Aqui eu continuo aplicando a lógica da cobra

        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)

       
        snake_body.append(snake_head)

        # Aqui é a lógica de morte da cobra e de restart

        if snake_body.count(snake_head) > 1:
            font_2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game Over, press R to restart'
            text_format = font_2.render(mensagem, True, (0,0,0))
            ret_text = text_format.get_rect()

            dead = True
            while dead:
                screen.fill((255,255,255))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            points = 0
                            initial_size = 5
                            x_snake = int(screen_width / 2)
                            y_snake = int(screen_height / 2)
                            snake_body = []
                            snake_head = []
                            x_coin = randint(40, 600)
                            y_coin = randint(50, 430)
                            dead = False

                ret_text.center = (screen_width//2, screen_height//2)
                screen.blit(text_format, ret_text)            
                pygame.display.update()


        # Aqui faz a lógica das paredes, de aparecer do outro lado

        if x_snake > screen_width:
            x_snake = 0

        if x_snake < 0:
            x_snake = screen_width

        if y_snake < 0:
            y_snake = screen_height

        if y_snake > screen_height:
            y_snake = 0


        # Aqui é o valor inicial da cobra, o tamanho do corpo dela

        if len(snake_body) > initial_size:
            del snake_body[0]

        get_body(snake_body)

        #Aqui é aonde eu renderizo o texto dos Pontos
        screen.blit(text_format, (420, 10))


        pygame.display.update()

if __name__ == "__main__":
    main()