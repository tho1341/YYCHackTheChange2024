import pygame
from typing import Tuple

# Player class to handle all player related functionality
class Player:
    def __init__(self, start_pos: Tuple[int, int], player_size: Tuple[int, int], player_speed: float, vertical_speed: float):
        self.position = list(start_pos)
        self.size = player_size
        self.speed = player_speed
        self.vertical_speed = vertical_speed
        self.walking_animation_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        
        # Load Sprites
        self.sprite_down = pygame.image.load('./images/look_down.png').convert_alpha()
        self.sprite_left = pygame.image.load('./images/look_left.png').convert_alpha()
        self.sprite_right = pygame.image.load('./images/look_right.png').convert_alpha()
        self.sprite_up = pygame.image.load('./images/look_up.png').convert_alpha()

        self.walk_down_1 = pygame.image.load('./images/walk_down_1.png').convert_alpha()
        self.walk_down_2 = pygame.image.load('./images/walk_down_2.png').convert_alpha()
        self.walk_left_1 = pygame.image.load('./images/walk_left_1.png').convert_alpha()
        self.walk_left_2 = pygame.image.load('./images/walk_left_2.png').convert_alpha()
        self.walk_right_1 = pygame.image.load('./images/walk_right_1.png').convert_alpha()
        self.walk_right_2 = pygame.image.load('./images/walk_right_2.png').convert_alpha()
        self.walk_up_1 = pygame.image.load('./images/walk_up_1.png').convert_alpha()
        self.walk_up_2 = pygame.image.load('./images/walk_up_2.png').convert_alpha()

        # Scale the images to player size
        self.sprite_down = pygame.transform.scale(self.sprite_down, self.size)
        self.sprite_left = pygame.transform.scale(self.sprite_left, self.size)
        self.sprite_right = pygame.transform.scale(self.sprite_right, self.size)
        self.sprite_up = pygame.transform.scale(self.sprite_up, self.size)

        self.walk_down_1 = pygame.transform.scale(self.walk_down_1, self.size)
        self.walk_down_2 = pygame.transform.scale(self.walk_down_2, self.size)
        self.walk_left_1 = pygame.transform.scale(self.walk_left_1, self.size)
        self.walk_left_2 = pygame.transform.scale(self.walk_left_2, self.size)
        self.walk_right_1 = pygame.transform.scale(self.walk_right_1, self.size)
        self.walk_right_2 = pygame.transform.scale(self.walk_right_2, self.size)
        self.walk_up_1 = pygame.transform.scale(self.walk_up_1, self.size)
        self.walk_up_2 = pygame.transform.scale(self.walk_up_2, self.size)

    def move(self, keys: pygame.key.get_pressed, screen_width: int, screen_height: int, player_x_offset: float, npc_positions: list):
        if keys[pygame.K_RIGHT]:
            if self.position[0] < screen_width // 2 or player_x_offset <= -npc_positions[-1][0] + screen_width - 200:
                self.position[0] += self.speed
            else:
                player_x_offset -= self.speed
            self.update_animation(2)  # Moving right
        elif keys[pygame.K_LEFT] and self.position[0] > 0:
            self.position[0] -= self.speed
            self.update_animation(3)  # Moving left
        if keys[pygame.K_UP] and self.position[1] > 0:
            self.position[1] -= self.vertical_speed
            self.update_animation(0)  # Moving up
        elif keys[pygame.K_DOWN] and self.position[1] < screen_height - self.size[1]:
            self.position[1] += self.vertical_speed
            self.update_animation(1)  # Moving down

    def update_animation(self, direction: int):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= 500:  # Update every 500ms for animation
            self.walking_animation_frame = (self.walking_animation_frame + 1) % 2
            self.last_update_time = current_time

    def draw(self, screen: pygame.Surface, keys: pygame.key.get_pressed):
        if keys[pygame.K_RIGHT]:
            if self.walking_animation_frame == 0:
                screen.blit(self.walk_right_1, (self.position[0], self.position[1]))
            else:
                screen.blit(self.walk_right_2, (self.position[0], self.position[1]))
        elif keys[pygame.K_LEFT]:
            if self.walking_animation_frame == 0:
                screen.blit(self.walk_left_1, (self.position[0], self.position[1]))
            else:
                screen.blit(self.walk_left_2, (self.position[0], self.position[1]))
        elif keys[pygame.K_UP]:
            if self.walking_animation_frame == 0:
                screen.blit(self.walk_up_1, (self.position[0], self.position[1]))
            else:
                screen.blit(self.walk_up_2, (self.position[0], self.position[1]))
        elif keys[pygame.K_DOWN]:
            if self.walking_animation_frame == 0:
                screen.blit(self.walk_down_1, (self.position[0], self.position[1]))
            else:
                screen.blit(self.walk_down_2, (self.position[0], self.position[1]))
        else:
            screen.blit(self.sprite_right, (self.position[0], self.position[1]))  # Idle right-facing

