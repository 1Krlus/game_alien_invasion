import pygame

class Settings():
# Uma classe para armazenar todas as configurações do jogo
    # Inicializa as configurações do jogo
    def __init__(self):
        # Configurações da tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_image = pygame.image.load('images/fundo.jpg')

        # Configurações da nave
        self.ship_speed_factor = 1.5
