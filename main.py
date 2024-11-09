import pygame
import sys
from menu import draw_main_menu, handle_menu_events, selected_option
from game import game_loop
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Main Menu")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle menu events
        handle_menu_events(event)

    # Draw the main menu
    draw_main_menu(screen)
    pygame.display.flip()

    # Check if "Start" is selected
    if selected_option == 0:
        game_loop(screen)  # Start the main game loop
        selected_option = -1  # Reset to return to menu after scenario

    elif selected_option == 2:  # Quit option
        pygame.quit()
        sys.exit()
