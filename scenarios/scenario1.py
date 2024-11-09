# scenarios/scenario1.py

import pygame
from YYCHackTheChange2024.settings import BLACK, scenario_font
import sys

def run_scenario(screen, player):
    # Scenario state variables
    scenario_complete = False
    choice_made = False
    choice = None

    while not scenario_complete:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not choice_made:
                if event.key == pygame.K_1:
                    choice = 'enter_anyway'
                    choice_made = True
                elif event.key == pygame.K_2:
                    choice = 'find_other_activity'
                    choice_made = True

        screen.fill((255, 255, 255))

        if not choice_made:
            # Display scenario description and choices
            scenario_text = "You are invited to an 18+ event but you're under 18. What do you do?"
            option1 = "1. Attempt to enter anyway."
            option2 = "2. Decide not to go or find another activity."

            render_text(screen, scenario_text, (50, 50))
            render_text(screen, option1, (50, 150))
            render_text(screen, option2, (50, 200))
        else:
            # Display consequences and learning points
            if choice == 'enter_anyway':
                consequence_text = "You were denied entry due to age restrictions."
                learning_point = "Learning Point: Age restrictions are enforced to comply with legal consent laws."
            elif choice == 'find_other_activity':
                consequence_text = "You found a fun alternative suitable for your age."
                learning_point = "Learning Point: Respecting age restrictions is important."

            render_text(screen, consequence_text, (50, 150))
            render_text(screen, learning_point, (50, 200))

            # Wait for a few seconds before ending the scenario
            pygame.display.flip()
            pygame.time.wait(3000)
            scenario_complete = True

        pygame.display.flip()

def render_text(screen, text, position):
    text_surface = scenario_font.render(text, True, BLACK)
    screen.blit(text_surface, position)
