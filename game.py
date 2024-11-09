import pygame
import sys
from player import Player
from scenarios import scenario1, scenario2, scenario3  # Import your scenarios
from settings import WHITE, BLACK  # Adjusted import

# Main game loop
def game_loop(screen):
    player = Player(400, 300)
    all_sprites = pygame.sprite.Group(player)
    
    # List of scenarios to play
    scenarios = [scenario1, scenario2, scenario3]
    current_scenario_index = 0

    while current_scenario_index < len(scenarios):
        current_scenario = scenarios[current_scenario_index]
        
        # Clear the screen and reset player position if needed
        screen.fill(WHITE)
        player.rect.topleft = (400, 300)
        
        # Run the current scenario logic
        current_scenario.run_scenario(screen, player)  # Pass player to scenario if required
        
        current_scenario_index += 1  # Move to the next scenario

    # After all scenarios are complete, you can return to the main menu or end the game
    return
