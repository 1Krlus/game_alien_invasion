import sys
import pygame
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
        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(settings.bg_color)
        ship.blitme()
        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()