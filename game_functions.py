import sys
import pygame
from bullet import Bullet
from alien import Alien

def create_fleet(settings, screen, aliens): # Cria uma frota de aliens
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width # Cria um alien e calcula o número de aliens em uma linha
    number_aliens_x = int(available_space_x / (2 * alien_width)) # O espaçamento entre os aliens é igual à largura de um alien

    for alien_number in range(number_aliens_x): # Cria a primeira linha de aliens
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def check_keydown_events(event, settings, screen, ship, bullets): # Responde a pressionamentos de tecla
    if event.key == pygame.K_d: # Se a tecla D foi pressionada
        ship.moving_right = True # Define que a nave deve se mover para a direita
    elif event.key == pygame.K_a: # Se a tecla A foi pressionada
        ship.moving_left = True # Define que a nave deve se mover para a esquerda
    elif event.key == pygame.K_w: # Se a tecla W foi pressionada
        ship.moving_up = True # Define que a nave deve se mover para cima
    elif event.key == pygame.K_s: # Se a tecla S foi pressionada
        ship.moving_down = True # Define que a nave deve se mover para baixo
    elif event.key == pygame.K_SPACE: # Se a tecla espaço for precionada
        new_bullet = Bullet(settings, screen, ship, "images/bullet.bmp") #Cria um novo projétil e o adiciona ao grupo de projéteis
        bullets.add(new_bullet)
    elif event.key == pygame.K_BACKSPACE:
        sys.exit()

def check_keyup_events(event, ship): # Responde a solturas de tecla
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False

def check_events(settings, screen, ship, bullets): #Responde a eventos de pressionamento de teclas e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship, aliens, bullets): # Atualiza as imagens na tela e alterna para a nova tela.
    screen.blit(settings.bg_image, (0, 0)) #Redesenha a tela a cada passagem pelo laço
   
    for bullet in bullets.sprites(): # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip() # Deixa a tela mais recente visível
