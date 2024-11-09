import pygame
import sys
from player import Player
from YYCHackTheChange2024.settings import WHITE, BLACK

# Main game loop
def game_loop(screen):
    player = Player(400, 300)
    all_sprites = pygame.sprite.Group(player)
    
    # Initialize which scenario to play (e.g., scenario1)
    current_scenario = scenario1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update sprites
        all_sprites.update()
        
        # Draw background and sprites
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Run the current scenario logic
        current_scenario.run_scenario(screen, player)  # Pass player to scenario

        pygame.display.flip()
