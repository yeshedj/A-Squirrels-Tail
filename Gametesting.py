import pygame
import random

# Global variables for player state
squirrel_speed_y = 0
is_jumping = False
SCROLL_THRESH = 200
scroll = 0

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
    bg_img = pygame.image.load("treeTrunk.png")
    squirrel_img = pygame.image.load("loverboy.png")
    # heart_img = pygame.image.load("QuitGameButton.png")
    return bg_img, squirrel_img

# Draw platforms
def draw_platforms(window, platforms):
    for platform in platforms:
        pygame.draw.rect(window, (139, 69, 19), platform)

def update(self, scroll):

    #update platform vertical position
    self.rect.y += scroll

# # Draw bananas
# def draw_bananas(window, banana_img, bananas):
#     for banana_pos in bananas:
#         window.blit(banana_img, banana_pos)

# # Generate random banana positions
# def generate_banana_positions(num_bananas, level_width, level_height, platform_areas, banana_size):
#     bananas = []
#     for _ in range(num_bananas):
#         x = random.randint(0, level_width - banana_size[0])
#         y = random.randint(0, level_height - banana_size[1])
#         banana_rect = pygame.Rect(x, y, banana_size[0], banana_size[1])
#         while any(banana_rect.colliderect(pygame.Rect(platform)) for platform in platform_areas):
#             x = random.randint(0, level_width - banana_size[0])
#             y = random.randint(0, level_height - banana_size[1])
#             banana_rect = pygame.Rect(x, y, banana_size[0], banana_size[1])
#         bananas.append((x, y))
#     return bananas

# Initialize levels
def initialize_level(level):
    if level == 1:
        platforms = [(50, 300, 150, 50), (200, 400, 150, 50)]
        time_limit = 60  # 60 seconds for level 1
    elif level == 2:
        platforms = [(100, 350, 150, 50), (300, 200, 150, 50), (550, 450, 150, 50)]
        time_limit = 50  # 50 seconds for level 2
    else:
        platforms = []  # Add more levels with custom platforms and time limits as needed
        time_limit = 0
    # bananas = generate_banana_positions(10 + 5 * (level - 1), 800, 600, platforms, banana_img.get_size())
    return platforms, time_limit

# Check platform collision
def check_platform_collision(squirrel_rect, platforms):
    global squirrel_speed_y
    for platform in platforms:
        platform_rect = pygame.Rect(platform)
        if squirrel_rect.colliderect(platform_rect) and squirrel_speed_y > 0:
            if squirrel_rect.bottom <= platform_rect.top + squirrel_speed_y:
                return platform_rect.top
    return None

# Apply gravity to squirrel
def apply_gravity(squirrel_position, platforms, squirrel_img):
    global squirrel_speed_y, is_jumping
    squirrel_position[1] += squirrel_speed_y
    squirrel_speed_y += 1
    squirrel_rect = pygame.Rect(squirrel_position[0], squirrel_position[1], squirrel_img.get_width(), squirrel_img.get_height())
    collision_y = check_platform_collision(squirrel_rect, platforms)
    if collision_y is not None:
        squirrel_position[1] = collision_y - squirrel_img.get_height()
        is_jumping = False
        squirrel_speed_y = 0
    elif squirrel_position[1] >= 500:
        squirrel_position[1] = 500
        is_jumping = False
        squirrel_speed_y = 0

# Handle player input
def handle_events():
    global is_jumping, squirrel_speed_y
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
        squirrel_speed_y = -20
        return True, None
    return True, None

# Update squirrel position
def update_squirrel_position(squirrel_position, direction, speed, squirrel_width):
    if direction == 'left':
        squirrel_position[0] = max(0, squirrel_position[0] - speed)
    elif direction == 'right':
        squirrel_position[0] = min(800 - squirrel_width, squirrel_position[0] + speed)

# Collect bananas
# def collect_bananas(ape_position, bananas, score, ape_size, banana_size):
#     squirrel_rect = pygame.Rect(ape_position[0], ape_position[1], ape_size[0], ape_size[1])
#     for banana in bananas[:]:
#         banana_rect = pygame.Rect(banana[0], banana[1], banana_size[0], banana_size[1])
#         if squirrel_rect.colliderect(banana_rect):
#             bananas.remove(banana)
#             score += 10
#     return score

# Update the timer
def update_timer(start_time, time_limit):
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    remaining_time = max(time_limit - elapsed_time, 0)
    return remaining_time

# Draw game screen
def draw(window, bg_img, squirrel_img, platforms, bg_y, squirrel_position, font, remaining_time, score, squirrel_rect):
    scroll = 0
    # window.blit(bg_img, (0, bg_y))
    # window.blit(bg_img, (bg_y + 0, 800))
    if squirrel_rect.rect.top <= SCROLL_THRESH:
        scroll = -squirrel_speed_y

    draw_platforms(window, platforms)
    # draw_bananas(window, banana_img, bananas)
    window.add(squirrel_img, squirrel_position)

    # Displaying the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.add(score_text, (10, 10))  # Display at the top left corner

    # Display the timer
    timer_text = font.render(f"Time left: {remaining_time}s", True, (255, 255, 255))
    window.add(timer_text, (650, 10))

    return scroll

    
    

# Main game function
def main():
    initialize_pygame()
    window = create_game_window(1400, 750, "A Squirrel's Tail")
    bg_img, squirrel_img = load_assets()
    font = pygame.font.SysFont("papyrus", 36)
    bg_x = 0
    current_level = 1
    platforms, time_limit = initialize_level(current_level)
    global squirrel_speed_y, is_jumping
    squirrel_position = [0, 0]
    squirrel_speed = 5
    score = 0
    scroll = 0
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    running = True
    while running:
        running, direction = handle_events()
        # update platforms
        draw_platforms.update(scroll)
        if not running:
            break

        update_squirrel_position(squirrel_position, direction, squirrel_speed, squirrel_img.get_width())
        apply_gravity(squirrel_position, platforms, squirrel_img)
        # score = collect_bananas(ape_position, bananas, score, ape_img.get_size(), banana_img.get_size())
        remaining_time = update_timer(start_time, time_limit)

        # if remaining_time == 0 or len(bananas) == 0:
        if remaining_time == 0:
            current_level += 1
            platforms, time_limit = initialize_level(current_level)
            if time_limit == 0:  # No more levels
                print(f"Game Over! Final Score: {score}")
                break
            start_time = pygame.time.get_ticks()

        bg_x -= 2
        if bg_x <= -800:
            bg_x = 0

        draw(window, bg_img, squirrel_img, platforms, bg_x, squirrel_position, font, remaining_time, score)
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
