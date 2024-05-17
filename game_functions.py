import sys
import pygame

def check_events(ship):
    #Responde a eventos de pressionamento de teclas e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Move a nave para a direita
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(settings, screen, ship): # Atualiza as imagens na tela e alterna para a nova tela.
    #Redesenha a tela a cada passagem pelo laço
    screen.blit(settings.bg_image, (0, 0))
    ship.blitme()
    # Deixa a tela mais recente visível
    pygame.display.flip()
