import pygame.image

class Settings ():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализируем настройки игры."""

        self.bg_color = (0, 191, 255)

        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3