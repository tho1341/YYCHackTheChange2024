# settings.py

import pygame

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
character_color = BLUE
character_size = 50

# Fonts
pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)
scenario_font = pygame.font.Font(None, 30)
