import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Main Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Menu options
menu_options = ["Start", "Options", "Quit"]
selected_option = 0

# Main Menu Function
def draw_main_menu():
    screen.fill(BLACK)
    
    # Draw Title
    title_text = font.render("Main Menu", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    screen.blit(title_text, title_rect)
    
    # Draw menu options
    for index, option in enumerate(menu_options):
        if index == selected_option:
            option_text = small_font.render(option, True, BLUE)
        else:
            option_text = small_font.render(option, True, WHITE)
        option_rect = option_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + index * 60))
        screen.blit(option_text, option_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Navigate through menu
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:  # Start
                    print("Game Started!")
                    # Add code here to start the game
                elif selected_option == 1:  # Options
                    print("Options Selected!")
                    # Add code for options here
                elif selected_option == 2:  # Quit
                    pygame.quit()
                    sys.exit()
    
    # Draw the main menu
    draw_main_menu()
    pygame.display.flip()
