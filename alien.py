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

    def check_edges(self):
        # Devolve True se o alien estiver na borda da tela
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Move o alien para a direita ou para a esquerda
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
