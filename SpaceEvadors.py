import pygame
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Create the display surface with a background image
background_image = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/treeMid.png')  # Load the background image
screen = pygame.display.set_mode((screen_width, screen_height))
screen.blit(background_image, (0, 0))  # Set the background image

# Set the title of the window
pygame.display.set_caption("Space Invaders")

# Load and set the window icon
icon = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/IMG_2938.JPG')
pygame.display.set_icon(icon)

# Load the player image
player_image = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/PlayGameButton.JPG')

# Load the laser image
laser_image = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/PlayGameButton.JPG')

# Load the enemy image
enemy_image = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/QuitGameButton.JPG')  # Corrected image filename

# Initialize player position
player_x = screen_width // 2
player_y = screen_height - 60

# Initialize laser position
laser_x = 0
laser_y = 480

# Initialize laser speed
laser_speed = 10

# Initialize laser state (ready to fire)
laser_state = "ready"

# Initialize enemy variables
enemy_x1 = random.randint(0, screen_width - 64)  # Random initial X position for enemy 1
enemy_y1 = random.randint(50, 150)  # Random initial Y position for enemy 1
enemy_speed1 = 2
enemy_direction1 = 1

enemy_x2 = random.randint(0, screen_width - 64)  # Random initial X position for enemy 2
enemy_y2 = random.randint(50, 150)  # Random initial Y position for enemy 2
enemy_speed2 = 2
enemy_direction2 = 1

# Initialize score
score = 0

# Initialize paused state
paused = False

# Initialize Pygame fonts and create a font object
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle player movement
        player_speed = 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Ensure the player stays within the screen boundaries
        if player_x < 0:
            player_x = 0
        if player_x > screen_width - player_image.get_width():
            player_x = screen_width - player_image.get_width()

        # Toggle pause state with the 'P' key
        if keys[pygame.K_p]:
            paused = not paused

    # Only update game elements if the game is not paused
    if not paused:
        # Handle shooting lasers
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Detect spacebar press
                if laser_state == "ready":
                    # Set the laser's initial position to the spaceship's tip
                    laser_x = player_x + 16  # Adjust as needed
                    laser_y = player_y  # Set to the player's position
                    laser_state = "fire"

        # Reset the background
        screen.blit(background_image, (0, 0))  # Set the background image

        # Move enemy 1
        enemy_x1 += enemy_speed1 * enemy_direction1

        # Check if enemy 1 has hit the screen's edge
        if enemy_x1 <= 0:
            enemy_direction1 = 1  # Change direction to right
        elif enemy_x1 >= screen_width - 64:
            enemy_direction1 = -1  # Change direction to left

        # Move enemy 2
        enemy_x2 += enemy_speed2 * enemy_direction2

        # Check if enemy 2 has hit the screen's edge
        if enemy_x2 <= 0:
            enemy_direction2 = 1  # Change direction to right
        elif enemy_x2 >= screen_width - 64:
            enemy_direction2 = -1  # Change direction to left

        # Collision Detection: Laser-enemy collision
        if laser_state == "fire":
            if (
                enemy_x1 < laser_x < enemy_x1 + 64
                and enemy_y1 < laser_y < enemy_y1 + 64
            ):
                # Reset the laser
                laser_state = "ready"
                # Reset enemy 1
                enemy_x1 = random.randint(0, screen_width - 64)
                enemy_y1 = random.randint(50, 150)

                # Increase the score
                score += 10

            if (
                enemy_x2 < laser_x < enemy_x2 + 64
                and enemy_y2 < laser_y < enemy_y2 + 64
            ):
                # Reset the laser
                laser_state = "ready"
                # Reset enemy 2
                enemy_x2 = random.randint(0, screen_width - 64)
                enemy_y2 = random.randint(50, 150)

                # Increase the score
                score += 10

        # Laser movement
        if laser_state == "fire":
            screen.blit(laser_image, (laser_x, laser_y))
            laser_y -= laser_speed

            # Check if the laser has gone off-screen
            if laser_y < 0:
                laser_state = "ready"

        # Draw the player
        screen.blit(player_image, (player_x, player_y))

        # Draw enemy 1
        screen.blit(enemy_image, (enemy_x1, enemy_y1))

        # Draw enemy 2
        screen.blit(enemy_image, (enemy_x2, enemy_y2))

    # Display the score regardless of the pause state
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Display pause text if the game is paused
    if paused:
        pause_text = font.render("Paused", True, (255, 255, 255))
        screen.blit(pause_text, (screen_width // 2 - 50, screen_height // 2))

    # Update the display
    pygame.display.flip()

# Clean up and quit
pygame.quit()