import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game(): 
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Cria uma espaçonave
    ship = Ship(screen)
    
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)

run_game()