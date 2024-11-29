import pygame

class Ship():
    # Inicializa a espaço nave e define sua posição inicial
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da nave
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
     # Atualiza a posição da nave de acordo com as flags de movimento
    def update(self):
        # Move a nave para a direita
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0: # Move a nave para a esquerda
            self.centerx -= self.settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0: # Move a nave para cima
           self.centery -= self.settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # Move a nave para baixo
            self.centery += self.settings.ship_speed_factor
    
        self.rect.centerx = self.centerx # Atualiza o objeto rect de acordo com o eixo x
        self.rect.centery = self.centery # Atualiza o objeto rect de acordo com o eixo y

    def blitme(self): # Desenha a espaçonave em sua posição atual.
        self.screen.blit(self.image, self.rect)
