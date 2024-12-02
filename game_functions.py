import sys
import pygame
from bullet import Bullet
from alien import Alien

def get_number_alien_x(settings, alien_width): # Determina o número de aliens que cabem em uma linha
    available_space_x = settings.screen_width - 2 * alien_width # Cria um alien e calcula o número de aliens em uma linha
    number_aliens_x = int(available_space_x / (2 * alien_width)) # O espaçamento entre os aliens é igual à largura de um alien
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height): # Determmina o número de linhas com aliens que cabem na tela
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number): # Cria um alien e o posiciona na linha
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, aliens, ship): # Cria uma frota de aliens
    # Cria um alien e calcula o número de aliens em uma linha
    alien = Alien(settings, screen)
    number_aliens_x = get_number_alien_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    # Cria a primeira linha de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)

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

def update_bullets(aliens, bullets):
    # Atualiza a posição dos projéteis e se livra dos projéteis antigos
    bullets.update() # Chama a função update da classe Bullet para fazer os projéteis se moverem para cima
    for bullet in bullets.copy(): # Limita o alcance dos projéteis para sumirem ao chegar no topo da tela
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    # Verifica se algum projétil atingiu os aliens, em caso afirmativo, livra-se do projétil e do alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def update_screen(settings, screen, ship, aliens, bullets): # Atualiza as imagens na tela e alterna para a nova tela.
    screen.blit(settings.bg_image, (0, 0)) #Redesenha a tela a cada passagem pelo laço
   
    for bullet in bullets.sprites(): # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip() # Deixa a tela mais recente visível

def check_fleet_edges(settings, aliens):
    # Responde apropriadamente se algum alien alcançou uma borda
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    # Faz toda a frota descer e muda a sua direção
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def update_aliens(settings, aliens):
    check_fleet_edges(settings, aliens) 
    # Verifica se a frota setá em uma das bordas e então atualiza as posições de todos os aliens da frota
    aliens.update() # Atualiza as posições de todos os aliens da frota
