import sys
import pygame
from bullet import Bullet

# Responde a pressionamentos de tecla
def check_keydown_events(event, settings, screen, ship, bullets):
    # Se a tecla direita foi pressionada
    if event.key == pygame.K_RIGHT:
        # Define que a nave deve se mover para a direita 
        ship.moving_right = True
    # Se a tecla esquerda foi pressionada
    elif event.key == pygame.K_LEFT:
        # Define que a nave deve se mover para a esquerda
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria um novo projétil e o adiciona ao grupo de projéteis
        new_bullet = Bullet(settings, screen, ship, "images/bullet.bmp")
        bullets.add(new_bullet)

# Responde a solturas de tecla
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings, screen, ship, bullets):
    #Responde a eventos de pressionamento de teclas e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship, bullets): # Atualiza as imagens na tela e alterna para a nova tela.
    #Redesenha a tela a cada passagem pelo laço
    screen.blit(settings.bg_image, (0, 0))
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Deixa a tela mais recente visível
    pygame.display.flip()
