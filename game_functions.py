import sys
import pygame

# Responde a pressionamentos de tecla
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

# Responde a solturas de tecla
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    #Responde a eventos de pressionamento de teclas e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship): # Atualiza as imagens na tela e alterna para a nova tela.
    #Redesenha a tela a cada passagem pelo laço
    screen.blit(settings.bg_image, (0, 0))
    ship.blitme()
    # Deixa a tela mais recente visível
    pygame.display.flip()
