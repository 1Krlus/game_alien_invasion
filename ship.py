import pygame

class Ship():
    # Inicializa a espaço nave e define sua posição inicial
    def __init__(self, screen):
        self.screen = screen
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
       
     # Atualiza a posição da nave de acordo com a flag de movimento
    def update(self):
        # Move a nave para a direita
        if self.moving_right:
            self.rect.centerx +=1
        
        # Move a nave para a esquerda
        if self.moving_left:
            self.rect.centerx -=1
    
    # Desenha a espaçonave em sua posição atual.
    def blitme(self):
        self.screen.blit(self.image, self.rect)
