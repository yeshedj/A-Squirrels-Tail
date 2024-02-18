import pygame
import random

# Initialize pygame
pygame.init()

# Game Window
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750

# Create game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A Squirrel's Tail")

# Set frame rate
clock = pygame.time.Clock()
FPS = 60

# Game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load images
squirrel_img = pygame.image.load("LoverBoy.png").convert_alpha()
image = pygame.image.load("Bg Squirrel.png").convert_alpha()
bg_image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# cloud_img = pygame.image.load("Cloud.png").convert_alpha()
image2 = pygame.image.load("rolling bg.png").convert_alpha()
roll_bg = pygame.transform.scale(image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to draw background
def draw_bg(bg_scroll):
    window.blit(bg_image, (0, 0 + bg_scroll))
    window.blit(roll_bg, (0, -650 + bg_scroll))

clouds = [[500, 100, 1], [750, 330, 2], [350, 450, 3]]
cloud_images = []
for i in range(1, 4):
    img = pygame.image.load(f'Cloud{i}.png')
    cloud_images.append(img)

def draw_clouds(cloud_list, images):
    platforms = []
    for j in range(len(cloud_list)):
        image = images[cloud_list[j][2] - 1]
        image = pygame.transform.scale(image, (450, 250))
        platform = pygame.rect.Rect((cloud_list[j][0] + 165, cloud_list[j][1] + 120), (120, 20))
        # platform.rect = platform.get_rect()
        # platform.rect.center = (200, 220)
        window.blit(image, (cloud_list[j][0], cloud_list[j][1]))
        pygame.draw.rect(window, 'grey', platform)
        platforms.append(platform)

    return platforms

# Squirrel class
class Squirrel():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(squirrel_img, (550, 450))
        self.width = 120
        self.height = 140
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # Reset variables
        scroll = 0
        dx = 0
        dy = 0

        # Process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -10
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = 10
            self.flip = False

        # Gravity
        self.vel_y += GRAVITY
        dy += self.vel_y
        

        # Ensure squirrel doesn't go off the edge of the window
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        # Check collision with clouds
        # for platform in cloud_platforms:
        #     # Collision in the y direction
        #     if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
        #         # Check if above the platform
        #         if self.rect.bottom < platform.rect.centery:
        #             if self.vel_y > 0:
        #                 self.rect.bottom = platform.rect.top
        #                 dy = 0
        #                 self.vel_y = -20
        cloud_platforms = draw_clouds(clouds, cloud_images)
        for platform in cloud_platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:  # If falling
                    self.rect.bottom = platform.top
                    self.vel_y = 0




        # Check collision with ground
        if self.rect.bottom + dy > SCREEN_HEIGHT - 80:
            dy = 0
            self.vel_y = -20

        # Check if squirrel has bounced to the top of the screen
        if self.rect.top <= SCROLL_THRESH:
            # if player is jumping
            if self.vel_y < 0:
                scroll = -dy


        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        window.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 215, self.rect.y - 150))
        pygame.draw.rect(window, WHITE, self.rect, 2)



# Platform class
# class Platform(pygame.sprite.Sprite):
#     def __init__(self, x, y, width):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(cloud_img, (width, 500))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.rect.x = x
#         self.rect.y = y

#     def update(self, scroll):
#         # Update platform's vertical position
#         self.rect.y += scroll

#         # Check if platform has gone off the screen
#         if self.rect.top > SCREEN_HEIGHT: 
#             self.kill()

#     def draw(self):
#         window.blit(self.image, self.rect)
#         pygame.draw.rect(window, RED, self.rect)

    # def __init__(self, x, y):
    #     self.image = pygame.transform.scale(squirrel_img, (550, 450))
    #     self.width = 120
    #     self.height = 140
    #     self.rect = pygame.Rect(0, 0, self.width, self.height)
    #     self.rect.center = (x, y)



# Squirrel instance
LoverBoy = Squirrel(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#Create sprite groups
# platform_group = pygame.sprite.Group()

# Create starting platform
# platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 75)
# platform_group.add(platform)



# Create temporary clouds
# for p in range(MAX_PLATFORMS):
#     p_w = random.randint(350, 700)
#     p_x = random.randint(0, SCREEN_WIDTH - p_w)
#     p_y = p * random.randint(80, 120)
#     platform = Platform(p_x, p_y, p_w)
#     platform_group.add(platform)

# Game loop
run = True
while run:

    clock.tick(FPS)

    scroll = LoverBoy.move()

    # Draw backgroung
    bg_scroll += scroll
    if bg_scroll >= 650:
        bg_scroll = 25
    draw_bg(bg_scroll)

    # Draw temporary scroll threshold
    # pygame.draw.line(window, WHITE, (0, SCROLL_THRESH), (SCREEN_WIDTH, SCROLL_THRESH))

    # Generate platforms
    cloud_platforms = draw_clouds(clouds, cloud_images)

    # Collision with platforms

    


    # if len(platform_group) < MAX_PLATFORMS:
    #     p_w = random.randint(350, 700)
    #     p_x = random.randint(0, SCREEN_WIDTH - p_w)
    #     p_y = platform.rect.y - random.randint(80, 120)
    #     platform = Platform(p_x, p_y, p_w)
    #     platform_group.add(platform)
    # # Update platforms
    # platform_group.update(scroll)

    # # Draw sprites
    # platform_group.draw(window)
    LoverBoy.draw()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    # Update display window
    pygame.display.update()

pygame.quit()