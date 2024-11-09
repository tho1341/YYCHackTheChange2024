import os
import pygame
import sys

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canadian Driving")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load Images
background_image = pygame.image.load("../images/sample.png")
character_car_image = pygame.image.load("../images/car.png")
police_car_image = pygame.image.load("../images/car.png")

# Resize images if necessary
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
character_car_image = pygame.transform.scale(character_car_image, (100, 50))
police_car_image = pygame.transform.scale(police_car_image, (100, 50))

# Initial positions
# Position the cop car in front of the character car, both lower on the screen
character_car_pos = [WIDTH - 150, HEIGHT // 2 + 65]  # Lower on the screen
police_car_pos = [WIDTH - 500, HEIGHT // 2 + 65]  # Slightly in front of the character car

# Font settings
main_font = pygame.font.Font(None, 36)

def draw_text_wrapped(surface, text, font, color, x, y, max_width):
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

def show_dialogue():
    dialogue_running = True
    option_selected = None

    # Dialogue options
    options = [
        "Comply and politely ask why.",
        "Refuse to show ID and walk away."
    ]

    while dialogue_running:
        screen.fill(WHITE)
        
        # Display scenario text
        draw_text_wrapped(screen, "The officer has stopped you and asked for identification.", main_font, BLACK, 50, 50, WIDTH - 100)
        
        # Display choices
        for i, option in enumerate(options):
            text = f"{i + 1}. {option}"
            draw_text_wrapped(screen, text, main_font, BLACK, 100, 200 + i * 50, WIDTH - 200)
        
        # Handle option selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    option_selected = options[0]
                    dialogue_running = False
                elif event.key == pygame.K_2:
                    option_selected = options[1]
                    dialogue_running = False

        pygame.display.flip()

    display_consequences(option_selected)

def display_consequences(selected_option):
    screen.fill(WHITE)
    feedback = ""

    if selected_option == "Comply and politely ask why.":
        feedback = ("Good choice. You have the right to know why you're being stopped, and "
                    "interacting respectfully is usually the best approach.")
    elif selected_option == "Refuse to show ID and walk away.":
        feedback = ("This may not be the best option. In some cases, refusing to comply without knowing your rights "
                    "can lead to further questioning or suspicion.")
    
    draw_text_wrapped(screen, feedback, main_font, BLACK, 50, HEIGHT // 2, WIDTH - 100)
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    dialogue_active = False

    while True:
        screen.blit(background_image, (0, 0))


        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Character movement with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_car_pos[0] -= 0.2
        if keys[pygame.K_RIGHT]:
            character_car_pos[0] += 0.2
        if keys[pygame.K_UP]:
            character_car_pos[1] -= 0.2
        if keys[pygame.K_DOWN]:
            character_car_pos[1] += 0.2

        # Draw the cars
        screen.blit(character_car_image, character_car_pos)
        screen.blit(police_car_image, police_car_pos)

        # Create rects for collision detection
        character_rect = pygame.Rect(character_car_pos[0], character_car_pos[1], character_car_image.get_width(), character_car_image.get_height())
        police_rect = pygame.Rect(police_car_pos[0], police_car_pos[1], police_car_image.get_width(), police_car_image.get_height())

        # Check for collision between character and cop car
        if character_rect.colliderect(police_rect) and not dialogue_active:
            dialogue_active = True  # Activate dialogue on collision
            show_dialogue()

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
