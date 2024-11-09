import pygame
import sys
from typing import Dict, List, Tuple
from player import Player  # Import the Player class

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canadian Law For Employees")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (200, 50, 50)
NPC_COLOR = (180, 100, 50)
GREEN = (34, 139, 34)

# Player settings
player_size = (50, 50)
player_speed = 0.1
vertical_speed = 0.1  # Added vertical speed
player = Player(start_pos=(100, HEIGHT // 2), player_size=player_size, player_speed=player_speed, vertical_speed=vertical_speed)

# NPC sprite and law information (unchanged from your code)
npc_sprite = pygame.Surface((50, 50))
npc_sprite.fill(NPC_COLOR)

# NPC positions with varied y positions
npc_positions = [
    (400, HEIGHT // 2 - 100),
    (1200, HEIGHT // 2 + 50),
    (2000, HEIGHT // 2 - 50),
    (2800, HEIGHT // 2 + 100),
    (3600, HEIGHT // 2 - 75)
]

# Scenario-based quiz questions (unchanged)
scenarios = [
    # Same list of scenarios as in your original code
]

# Main loop to run the game
def tutorial_level():
    in_tutorial = True
    showing_details = False
    current_details = None
    player_x_offset = 0
    visited_npcs = set()  # Track which NPCs have been visited

    while in_tutorial:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and current_details is not None:
                    showing_details = not showing_details
                elif event.key == pygame.K_ESCAPE:
                    showing_details = False

        # Move player
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT, player_x_offset, npc_positions)

        # Draw player
        player.draw(screen, keys)

        # Draw and handle NPCs
        for i, (npc_x, npc_y) in enumerate(npc_positions):
            adjusted_x = npc_x + player_x_offset
            if 0 < adjusted_x < WIDTH:  # Only draw NPCs on screen
                screen.blit(npc_sprite, (adjusted_x, npc_y))

        pygame.display.flip()

if __name__ == "__main__":
    tutorial_level()
    pygame.quit()
