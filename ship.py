import pygame

class Ship():
    """Класс для управления кораблем."""
    def __init__(self, ai_game,screen):
        """Инициализирует корабль и задает его начальную позицию"""

        self.ai_game = ai_game
        self.screen_rect = ai_game.srceen.get_rect()

#Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
#Кажый новый корабль появляеться у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

def bitme(self):
    """Рисует корабль в текущей позиции."""
    self.screen.blit(self.image, self.rect)