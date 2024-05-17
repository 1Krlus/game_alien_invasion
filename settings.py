import pygame

class Settings():
# Uma classe para armazenar todas as configurações do jogo
    def __init__(self): # Inicializa as configurações do jogo
        # Configurações da tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_image = pygame.image.load('images/fundo.jpg')
