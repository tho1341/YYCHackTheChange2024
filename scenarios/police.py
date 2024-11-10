import os
import pygame
import sys

# Set up working directory to the script’s location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canadian Law Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIALOGUE_BOX_COLOR = (0, 0, 0, 128)  # Semi-transparent black for the dialogue box

# Load Images
background_image = pygame.image.load("../images/sample.png")
character_car_image = pygame.image.load("../images/car.png")
police_car_image = pygame.image.load("../images/car.png")
exclamation_image = pygame.image.load("../images/exclamation.png")

# Resize images if necessary
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
character_car_image = pygame.transform.scale(character_car_image, (100, 50))
police_car_image = pygame.transform.scale(police_car_image, (100, 50))
exclamation_image = pygame.transform.scale(exclamation_image, (30, 30))

# Initial positions
character_car_pos = [WIDTH - 150, HEIGHT // 2 + 65]
police_car_pos = [WIDTH - 500, HEIGHT // 2 + 65]

# Font settings
main_font = pygame.font.Font(None, 36)

def draw_text_wrapped(surface, text, font, color, x, y, max_width):
    """Draw wrapped text."""
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word + " ", True, color)
        word_width = word_surface.get_width()

        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width

    lines.append(" ".join(current_line))

    y_offset = y
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y_offset))
        y_offset += font.get_height()

    return y_offset

def show_exclamation():
    """Display an exclamation above the police car briefly."""
    exclamation_pos = (police_car_pos[0] + 35, police_car_pos[1] - 40)
    screen.blit(exclamation_image, exclamation_pos)
    pygame.display.flip()
    pygame.time.wait(500)  # Show the exclamation for half a second

def show_dialogue_with_next():
    """Display the dialogue box, text, and wait for Space to proceed."""
    dialogue_text = (
        "The officer has stopped you and asked for identification. Under Canadian law, "
        "you generally have the right to ask why you're being stopped. In specific cases, "
        "like driving, you may need to show ID."
    )

    # Draw dialogue box and text
    dialogue_box = pygame.Surface((WIDTH, 150), pygame.SRCALPHA)
    dialogue_box.fill(DIALOGUE_BOX_COLOR)
    screen.blit(dialogue_box, (0, HEIGHT - 150))

    draw_text_wrapped(screen, dialogue_text, main_font, WHITE, 20, HEIGHT - 130, WIDTH - 40)
    pygame.display.flip()

    # Wait for Space key to proceed
    waiting_for_space = True
    while waiting_for_space:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_space = False

def show_options():
    """Display options after Space is pressed."""
    screen.fill(WHITE)  # Clear the screen for new content
    dialogue_box = pygame.Surface((WIDTH, 150), pygame.SRCALPHA)
    dialogue_box.fill(DIALOGUE_BOX_COLOR)
    screen.blit(dialogue_box, (0, HEIGHT - 150))

    options_text = (
        "Based on what you've learned, how would you respond?"
    )
    draw_text_wrapped(screen, options_text, main_font, WHITE, 20, HEIGHT - 130, WIDTH - 40)

    options = [
        "Press 1 to Comply and politely ask why.",
        "Press 2 to Refuse to show ID and walk away."
    ]
    for i, option in enumerate(options):
        draw_text_wrapped(screen, option, main_font, WHITE, 20, HEIGHT - 90 + i * 30, WIDTH - 40)

    pygame.display.flip()

    # Handle option selection
    option_selected = None
    while option_selected is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    option_selected = options[0]
                elif event.key == pygame.K_2:
                    option_selected = options[1]

    display_consequences(option_selected)

def display_consequences(selected_option):
    """Display the consequence based on the player's choice."""
    screen.fill(WHITE)
    feedback = ""

    if selected_option == "Press 1 to Comply and politely ask why.":
        feedback = (
            "Good choice! You have the right to know why you're being stopped. "
            "Interacting respectfully can help de-escalate the situation."
        )
    elif selected_option == "Press 2 to Refuse to show ID and walk away.":
        feedback = (
            "This may not be the best option. Refusing to comply can lead to further questioning. "
            "In some cases, such as traffic stops, you are legally required to show ID."
        )

    dialogue_box = pygame.Surface((WIDTH, 150), pygame.SRCALPHA)
    dialogue_box.fill(DIALOGUE_BOX_COLOR)
    screen.blit(dialogue_box, (0, HEIGHT - 150))
    
    draw_text_wrapped(screen, feedback, main_font, WHITE, 20, HEIGHT - 130, WIDTH - 40)
    pygame.display.flip()
    pygame.time.wait(9000)

def main():
    dialogue_active = False

    while True:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_car_pos[0] -= 0.2
        if keys[pygame.K_RIGHT]:
            character_car_pos[0] += 0.2
        if keys[pygame.K_UP]:
            character_car_pos[1] -= 0.2
        if keys[pygame.K_DOWN]:
            character_car_pos[1] += 0.2

        screen.blit(character_car_image, character_car_pos)
        screen.blit(police_car_image, police_car_pos)

        character_rect = pygame.Rect(character_car_pos[0], character_car_pos[1], character_car_image.get_width(), character_car_image.get_height())
        police_rect = pygame.Rect(police_car_pos[0], police_car_pos[1], police_car_image.get_width(), police_car_image.get_height())

        if character_rect.colliderect(police_rect) and not dialogue_active:
            dialogue_active = True
            show_exclamation()
            show_dialogue_with_next()  # Show dialogue and wait for Space to proceed
            show_options()  # Show options after Space is pressed

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
