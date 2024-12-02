import pygame

class Settings():
# Uma classe para armazenar todas as configurações do jogo
    # Inicializa as configurações do jogo
    def __init__(self):
        # Configurações da tela
        self.screen_width = 990
        self.screen_height = 990
        self.bg_image = pygame.image.load('images/background.jpg')

        # Configurações da nave
        self.ship_speed_factor = 1

        # Configurações dos projéteis self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullet_speed_factor = 2

        # Configurações dos aliens
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # fleet_direction igual a 1 representa a direita, -1 representa a esquerda


