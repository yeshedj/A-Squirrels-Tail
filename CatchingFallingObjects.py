import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catching Falling Objects')

# Define colors and game properties
background_color = (255, 255, 255)
object_color = (255, 0, 0)
player_color = (0, 0, 255)
object_size, player_size = 50, 50
object_x = random.randint(0, screen_width - object_size)
object_y = 0
player_x = screen_width // 2
player_y = screen_height - player_size
object_speed = 10
score = 0
is_paused = False  # Initialize pause state

# Initialize font for score display and pause message
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    is_paused = False
                else:
                    is_paused = True
            if not is_paused:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= player_size
                elif event.key == pygame.K_RIGHT and player_x < screen_width - player_size:
                    player_x += player_size

    # Game logic when not paused
    if not is_paused:
        object_y += object_speed
        if object_y > screen_height:
            running = False  # End the game
        if player_y < object_y + object_size and player_x < object_x + object_size and player_x + player_size > object_x:
            score += 1
            object_x = random.randint(0, screen_width - object_size)
            object_y = 0

    # Drawing objects and score
    screen.fill(background_color)
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_size, object_size))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    if not is_paused:
        text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 10))
    else:
        pause_text = font.render("Paused - Press Space to Resume", True, (0, 0, 0))
        screen.blit(pause_text, (screen_width // 2 - 200, screen_height // 2))

    pygame.display.flip()
    clock.tick(30)

# Game over screen
screen.fill(background_color)
game_over_text = font.render("Game Over! Press any key to quit.", True, (0, 0, 0))
screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2))
pygame.display.flip()

# Wait for player input to quit
waiting_for_input = True
while waiting_for_input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN):
            waiting_for_input = False

pygame.quit()