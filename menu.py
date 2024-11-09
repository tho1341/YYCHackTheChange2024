import pygame
from YYCHackTheChange2024.settings import WHITE, BLUE, BLACK, font, small_font

menu_options = ["Start", "Options", "Quit"]
selected_option = 0

def draw_main_menu(screen):
    screen.fill(BLACK)
    
    title_text = font.render("Main Menu", True, WHITE)
    title_rect = title_text.get_rect(center=(400, 150))
    screen.blit(title_text, title_rect)
    
    for index, option in enumerate(menu_options):
        option_text = small_font.render(option, True, BLUE if index == selected_option else WHITE)
        option_rect = option_text.get_rect(center=(400, 300 + index * 60))
        screen.blit(option_text, option_rect)

def handle_menu_events(event):
    global selected_option
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif event.key == pygame.K_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif event.key == pygame.K_RETURN:
            if selected_option == 2:  # Quit
                pygame.quit()
                sys.exit()
