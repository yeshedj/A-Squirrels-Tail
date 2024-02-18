import pygame
import random

# Global variables for player state
ape_speed_y = 0
is_jumping = False

# Initialize Pygame
def initialize_pygame():
    pygame.init()

# Create game window
def create_game_window(width, height, title):
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return window

# Load game assets
def load_assets():
    background_img = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/treeTrunk.png')
    ape_img = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/PlayGameButton.JPG')
    banana_img = pygame.image.load('/Users/destinyosemwengie/Documents/GitHub/CupidJam/QuitGameButton.JPG')
    return background_img, ape_img, banana_img

# Draw platforms
def draw_platforms(window, platforms):
    for platform in platforms:
        pygame.draw.rect(window, (139, 69, 19), platform)

# Draw bananas
def draw_bananas(window, banana_img, bananas):
    for banana_pos in bananas:
        window.blit(banana_img, banana_pos)

# Generate random banana positions
def generate_banana_positions(num_bananas, level_width, level_height, platform_areas, banana_size):
    bananas = []
    for _ in range(num_bananas):
        x = random.randint(0, level_width - banana_size[0])
        y = random.randint(0, level_height - banana_size[1])
        banana_rect = pygame.Rect(x, y, banana_size[0], banana_size[1])
        while any(banana_rect.colliderect(pygame.Rect(platform)) for platform in platform_areas):
            x = random.randint(0, level_width - banana_size[0])
            y = random.randint(0, level_height - banana_size[1])
            banana_rect = pygame.Rect(x, y, banana_size[0], banana_size[1])
        bananas.append((x, y))
    return bananas

# Initialize levels
def initialize_level(level, banana_img):
    if level == 1:
        platforms = [(50, 300, 150, 50), (200, 400, 150, 50)]
        time_limit = 60  # 60 seconds for level 1
    elif level == 2:
        platforms = [(100, 350, 150, 50), (300, 200, 150, 50), (550, 450, 150, 50)]
        time_limit = 50  # 50 seconds for level 2
    else:
        platforms = []  # Add more levels with custom platforms and time limits as needed
        time_limit = 0
    bananas = generate_banana_positions(10 + 5 * (level - 1), 800, 600, platforms, banana_img.get_size())
    return platforms, bananas, time_limit

# Check platform collision
def check_platform_collision(ape_rect, platforms):
    global ape_speed_y
    for platform in platforms:
        platform_rect = pygame.Rect(platform)
        if ape_rect.colliderect(platform_rect) and ape_speed_y > 0:
            if ape_rect.bottom <= platform_rect.top + ape_speed_y:
                return platform_rect.top
    return None

# Apply gravity to ape
def apply_gravity(ape_position, platforms, ape_img):
    global ape_speed_y, is_jumping
    ape_position[1] += ape_speed_y
    ape_speed_y += 1
    ape_rect = pygame.Rect(ape_position[0], ape_position[1], ape_img.get_width(), ape_img.get_height())
    collision_y = check_platform_collision(ape_rect, platforms)
    if collision_y is not None:
        ape_position[1] = collision_y - ape_img.get_height()
        is_jumping = False
        ape_speed_y = 0
    elif ape_position[1] >= 500:
        ape_position[1] = 500
        is_jumping = False
        ape_speed_y = 0

# Handle player input
def handle_events():
    global is_jumping, ape_speed_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, None
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return True, 'left'
    elif keys[pygame.K_RIGHT]:
        return True, 'right'
    elif keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        ape_speed_y = -20
        return True, None
    return True, None

# Update ape position
def update_ape_position(ape_position, direction, speed, ape_width):
    if direction == 'left':
        ape_position[0] = max(0, ape_position[0] - speed)
    elif direction == 'right':
        ape_position[0] = min(800 - ape_width, ape_position[0] + speed)

# Collect bananas
def collect_bananas(ape_position, bananas, score, ape_size, banana_size):
    ape_rect = pygame.Rect(ape_position[0], ape_position[1], ape_size[0], ape_size[1])
    for banana in bananas[:]:
        banana_rect = pygame.Rect(banana[0], banana[1], banana_size[0], banana_size[1])
        if ape_rect.colliderect(banana_rect):
            bananas.remove(banana)
            score += 10
    return score

# Update the timer
def update_timer(start_time, time_limit):
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    remaining_time = max(time_limit - elapsed_time, 0)
    return remaining_time

# Draw game screen
def draw(window, background_img, ape_img, banana_img, platforms, bg_x, ape_position, bananas, font, remaining_time, score):
    window.blit(background_img, (bg_x, 0))
    window.blit(background_img, (bg_x + 800, 0))
    draw_platforms(window, platforms)
    draw_bananas(window, banana_img, bananas)
    window.blit(ape_img, ape_position)

    # Displaying the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))  # Display at the top left corner

    # Display the timer
    timer_text = font.render(f"Time left: {remaining_time}s", True, (255, 255, 255))
    window.blit(timer_text, (650, 10))

# Main game function
def main():
    initialize_pygame()
    window = create_game_window(800, 600, "Jungle Adventure")
    background_img, ape_img, banana_img = load_assets()
    font = pygame.font.SysFont(None, 36)
    bg_x = 0
    current_level = 1
    platforms, bananas, time_limit = initialize_level(current_level, banana_img)
    global ape_speed_y, is_jumping
    ape_position = [100, 500]
    ape_speed = 5
    score = 0
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    running = True
    while running:
        running, direction = handle_events()
        if not running:
            break

        update_ape_position(ape_position, direction, ape_speed, ape_img.get_width())
        apply_gravity(ape_position, platforms, ape_img)
        score = collect_bananas(ape_position, bananas, score, ape_img.get_size(), banana_img.get_size())
        remaining_time = update_timer(start_time, time_limit)

        if remaining_time == 0 or len(bananas) == 0:
            current_level += 1
            platforms, bananas, time_limit = initialize_level(current_level, banana_img)
            if time_limit == 0:  # No more levels
                print(f"Game Over! Final Score: {score}")
                break
            start_time = pygame.time.get_ticks()

        bg_x -= 2
        if bg_x <= -800:
            bg_x = 0

        draw(window, background_img, ape_img, banana_img, platforms, bg_x, ape_position, bananas, font, remaining_time, score)
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
