import pygame

class Settings():
# Uma classe para armazenar todas as configurações do jogo
    # Inicializa as configurações do jogo
    def __init__(self):
        # Configurações da tela
        self.screen_width = 1024
        self.screen_height = 1000
        self.bg_image = pygame.image.load('images/background.jpg')

        # Configurações da nave
        self.ship_speed_factor = 0.8

        # Configurações dos projéteis self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullet_speed_factor = 1.5
