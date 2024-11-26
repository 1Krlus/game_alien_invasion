import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game(): 
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(settings,  screen)
    #Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Limita o alcance dos projéteis para sumirem ao chegar no topo da tela
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        
        gf.update_screen(settings, screen, ship, bullets)

run_game()
