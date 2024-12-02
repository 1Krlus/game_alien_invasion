import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game(): # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings,  screen) # Cria uma espaçonave
    bullets = Group() # Cria um grupo no qual serão armazenados os projéteis
    aliens = Group() # Cria um grupo no qual serão armazenados os aliens

    gf.create_fleet(settings, screen, aliens, ship) # Cria a frota de aliens

    while True:  # Inicia o laço principal do jogo
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, aliens, bullets)

run_game()
