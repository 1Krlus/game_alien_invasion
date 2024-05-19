import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # Uma classe para administrar projéteis disparados pela nave
    def __init__(self, settings, screen, ship):
        #Cria um objeto para o projétil na posição atual da nave
        super(Bullet, self).__self.screen = screen
        # Cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 
        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
    # Move o projétil para cima da tela
        # Atualiza a posição decimal do projétil
        self.rect.y = self.speed_factor
        # Atualiza a posição de rect
        self.rect.y = self.y
    
    def draw_bullet(self):
    # Desenha o projétil na tela.
        pygame.draw.rect(self.screen, self.color, self.rect)
