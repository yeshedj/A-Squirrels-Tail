# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2



def find_frame_dimensions(sprite_sheet):
    sheet_width, sheet_height = sprite_sheet.get_size()
    frame_width, frame_height = None, None

    # Scan the sprite sheet horizontally to find the frame width
    for x in range(sheet_width):
        pixel_count = sum(sprite_sheet.get_at((x, y)).a for y in range(sheet_height))
        if pixel_count > 0:
            frame_width = x + 1
            break

    # Scan the sprite sheet vertically to find the frame height
    for y in range(sheet_height):
        pixel_count = sum(sprite_sheet.get_at((x, y)).a for x in range(sheet_width))
        if pixel_count > 0:
            frame_height = y + 1
            break

    return frame_width, frame_height

class Squirrel(pg.sprite.Sprite):
    def __init__(self, sprite_sheet):
        super().__init__()
        self.sprite_sheet = sprite_sheet
        self.frame_index = 0
        self.frame_width, self.frame_height = find_frame_dimensions(sprite_sheet)
        self.frames = self.extract_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 100  # Initial x position
        self.rect.y = 100  # Initial y position
        self.speed = 5  # Movement speed
        self.animation_speed = 0.1  # Animation speed (delay between frames)
        self.last_update = pg.time.get_ticks()

    def extract_frames(self):
        frames = []
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        for y in range(0, sheet_height, self.frame_height):
            for x in range(0, sheet_width, self.frame_width):
                frame_rect = pg.Rect(x, y, self.frame_width, self.frame_height)
                frame = self.sprite_sheet.subsurface(frame_rect)
                frames.append(frame)
        return frames

    def update(self):
        # Move the squirrel horizontally
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed

        # Animation
        now = pg.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:  # Convert to milliseconds
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

# Initialize Pygame
pg.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Squirrel Animation")

# Load the sprite sheet
sprite_sheet = pg.image.load("SquirrelSpriteSheet.png").convert_alpha()

# Create the squirrel sprite
squirrel = Squirrel(sprite_sheet)
all_sprites = pg.sprite.Group(squirrel)

# Main loop
running = True
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Draw sprites
    screen.fill((255, 255, 255))  # Clear the screen
    all_sprites.draw(screen)

    pg.display.flip()
    clock.tick(10)  # Adjust the frame rate as needed

pg.quit()





# class Player(pg.sprite.Sprite):
#     def __init__(self, game):
#         pg.sprite.Sprite.__init__(self)
#         self.game = game
#         self.image = pg.Surface((30, 40))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         self.pos = vec(WIDTH / 2, HEIGHT / 2)
#         self.vel = vec(0, 0)
#         self.acc = vec(0, 0)

#     def jump(self):
#         # jump only if standing on a platform
#         self.rect.x += 1
#         hits = pg.sprite.spritecollide(self, self.game.platforms, False)
#         self.rect.x -= 1
#         if hits:
#             self.vel.y = -PLAYER_JUMP

#     def update(self):
#         self.acc = vec(0, PLAYER_GRAV)
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT]:
#             self.acc.x = -PLAYER_ACC
#         if keys[pg.K_RIGHT]:
#             self.acc.x = PLAYER_ACC

#         # apply friction
#         self.acc.x += self.vel.x * PLAYER_FRICTION
#         # equations of motion
#         self.vel += self.acc
#         self.pos += self.vel + 0.5 * self.acc
#         # wrap around the sides of the screen
#         if self.pos.x > WIDTH:
#             self.pos.x = 0
#         if self.pos.x < 0:
#             self.pos.x = WIDTH

#         self.rect.midbottom = self.pos

# class Platform(pg.sprite.Sprite):
#     def __init__(self, x, y, w, h):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((w, h))
#         self.image.fill(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y