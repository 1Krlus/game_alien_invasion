import pygame
from pygame.sprite import Sprite

class Alien(Sprite): # Uma classe que representa um único alien da frota
    def __init__(self, settings, screen): # Inicializa o alien e define sua posição inicial
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/green.bmp') #Carrega a imagem do alien e define seu atributo rect
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width # Inicia cada novo alien próximo a parte superior esquerda da tela
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) # Armazena a posição exata do alien

    def blitme(self):
        self.screen.blit(self.image, self.rect) # Desenha o alien em sua posição atual