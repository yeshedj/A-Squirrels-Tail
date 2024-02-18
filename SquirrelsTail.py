import pygame, sys
from SquirrelsButtons import Button
import random


pygame.init()


pygame.mixer.init()
# pygame.mixer.music.load("/Users/yeshej/Documents/CupidJam/Untitled/fun.mp3")
# pygame.mixer.music.load("/Users/yeshej/Documents/CupidJam/Untitled/cottage.mp3")
# pygame.mixer.music.play(-1)

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Squirrel's Tail")



cursor_image = pygame.image.load("cursor.png")
CS_IMG = pygame.transform.scale(cursor_image, (90, 70))
pygame.mouse.set_visible(False)


def get_font(size):
    return pygame.font.SysFont("papyrus", size)


def main_menu():
    # pygame.mixer.music.play(-1)
    original_bg = pygame.image.load("love is in the air.png")
    bg = pygame.transform.scale(original_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    menu_text = get_font(80).render("A SQUIRREL'S TAIL", True, "#b68f40")
    menu_rect = menu_text.get_rect(center=(700, 180))

    play_button = Button(image=pygame.image.load("PlayGameButton.png"), pos=(200, 400),
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    quit_button = Button(image=pygame.image.load("QuitGameButton.png"), pos=(1200, 400),
                         text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pygame.mouse.get_pos()):
                    play()
                elif quit_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            SCREEN.blit(bg, (0, 0))

            play_button.update(SCREEN)
            quit_button.update(SCREEN)

            SCREEN.blit(menu_text, menu_rect)

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.blit(CS_IMG, MENU_MOUSE_POS)
            pygame.display.update()


def play():
    play_back = Button(image=None, pos=(170, 510),
                       text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    play_next = Button(image=None, pos=(1200, 510),
                       text_input="NEXT", font=get_font(60), base_color="White", hovering_color="Pink")

    script_bg = pygame.image.load("newScriptBG.png")
    bg2 = pygame.transform.scale(script_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message = ["The love of your squirrel life is at the top! Climb up & reunite with your beloved!"]
    font = get_font(35)

    text_width, text_height = font.size(message[0])
    text_x = (SCREEN_WIDTH - text_width) // 2
    text_y = (SCREEN_HEIGHT - text_height) // 2

    speed = 2
    counter = 0
    done = False


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                elif play_next.checkForInput(pygame.mouse.get_pos()):
                    next()

        SCREEN.blit(bg2, (0, 0))

        if counter < speed * len(message[-1]):
            counter += 1

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")

        if text_surface.get_width() > SCREEN_WIDTH - 20:  # 20 pixels padding
            text_y += font.get_linesize()

        SCREEN.blit(text_surface, (text_x, text_y))

        play_back.changeColor(pygame.mouse.get_pos())
        play_back.update(SCREEN)
        play_next.changeColor(pygame.mouse.get_pos())
        play_next.update(SCREEN)

        SCREEN.blit(CS_IMG, pygame.mouse.get_pos())


        pygame.display.flip()

        pygame.time.Clock().tick(60)








def next():

    play_back2 = Button(image=None, pos=(170, 510),
                        text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    play_next2 = Button(image=None, pos=(1200, 510),
                        text_input="NEXT", font=get_font(60), base_color="White", hovering_color="Pink")

    script_bg = pygame.image.load("newScriptBG.png")
    bg2 = pygame.transform.scale(script_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message = ["Use the left & right arrows to navigate, spacebar/up arrow to jump, & don't fall!"]

    font = get_font(35)

    text_width, text_height = font.size(message[0])
    text_x = (SCREEN_WIDTH - text_width) // 2
    text_y = (SCREEN_HEIGHT - text_height) // 2

    speed = 2
    counter = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back2.checkForInput(pygame.mouse.get_pos()):
                    play()
                elif play_next2.checkForInput(pygame.mouse.get_pos()):
                    # script_BG = pygame.image.load("treeTrunk.png")
                    # BG2 = pygame.transform.scale(script_BG,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    gameplay(SCREEN)

        # SCREEN.fill("black")
        SCREEN.blit(bg2, (0, 0))
        # SCREEN.blit(CS_IMG, pygame.mouse.get_pos())

        if counter < speed * len(message[-1]):
            counter += 1

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")

        if text_surface.get_width() > SCREEN_WIDTH - 20:  # 20 pixels padding
            text_y += font.get_linesize()

        SCREEN.blit(text_surface, (text_x, text_y))

        play_back2.changeColor(pygame.mouse.get_pos())
        play_back2.update(SCREEN)
        play_next2.changeColor(pygame.mouse.get_pos())
        play_next2.update(SCREEN)

        SCREEN.blit(CS_IMG, pygame.mouse.get_pos())

        pygame.display.flip()

        pygame.time.Clock().tick(60)


def gameplay(SCREEN):


    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 750

    # Create game window
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_caption("A Squirrel's Tail")

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
    # squirrel_img = pygame.image.load("LoverBoy.png").convert_alpha()
    # image = pygame.image.load("Bg Squirrel.png").convert_alpha()
    # bg_image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # cloud_img = pygame.image.load("Cloud.png").convert_alpha()
    # image2 = pygame.image.load("rolling bg.png").convert_alpha()
    # roll_bg = pygame.transform.scale(image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

    squirrel_img = pygame.image.load("LoverBoy.png").convert_alpha()
    image = pygame.image.load("Bg Squirrel.png").convert_alpha()
    bg_image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # cloud_img = pygame.image.load("Cloud.png").convert_alpha()
    image2 = pygame.image.load("rolling bg.png").convert_alpha()
    roll_bg = pygame.transform.scale(image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Function to draw background
    def draw_bg(bg_scroll):
        SCREEN.blit(bg_image, (0, 0 + bg_scroll))
        SCREEN.blit(roll_bg, (0, -650 + bg_scroll))

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
            # for platform in platform_group:
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
                        self.vel_y = -20


            # # Check collision with ground
            # if self.rect.bottom + dy > SCREEN_HEIGHT + 20:
            #     dy = 0
            #     self.vel_y = -20
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
            SCREEN.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 215, self.rect.y - 150))
            pygame.draw.rect(SCREEN, WHITE, self.rect, 2)

    # Platform class
    # class Platform(pygame.sprite.Sprite):
    #     def __init__(self, x, y, width):
    #         pygame.sprite.Sprite.__init__(self)
    #         self.image = pygame.transform.scale(cloud_img, (width, 500))
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (x, y)
    #         self.rect.x = x
    #         self.rect.y = y
    #
    #     def update(self, scroll):
    #         # Update platform's vertical position
    #         self.rect.y += scroll
    #
    #         # Check if platform has gone off the screen
    #         if self.rect.top > SCREEN_HEIGHT:
    #             self.kill()
    #
    #     def draw(self):
    #         SCREEN.blit(self.image, self.rect)
    #         pygame.draw.rect(SCREEN, RED, self.rect)

    # Squirrel instance
    LoverBoy = Squirrel(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

    # Create sprite groups
    # platform_group = pygame.sprite.Group()
    # platform = None

    #
    # # Create temporary clouds
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

        # Draw background
        bg_scroll += scroll
        if bg_scroll >= 650:
            bg_scroll = 25
        draw_bg(bg_scroll)

        cloud_platforms = draw_clouds(clouds, cloud_images)

        # # Generate platforms
        # if len(platform_group) < MAX_PLATFORMS:
        #     p_w = random.randint(350, 700)
        #     p_x = random.randint(0, SCREEN_WIDTH - p_w)
        #     p_y = platform.rect.y - random.randint(80, 120)
        #     platform = Platform(p_x, p_y, p_w)
        #     platform_group.add(platform)

        # Update platforms
        # platform_group.update(scroll)

        # Draw sprites
        # platform_group.draw(SCREEN)
        LoverBoy.draw()

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update display window
        pygame.display.update()

    pygame.quit()


# Call the main menu function to start the game


        # gameplay_bg = pygame.image.load("Bg Squirrel.png")
        # gp_bg = pygame.transform.scale(gameplay_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        #
        # SCREEN.blit(gp_bg, (0, 0))
        # SCREEN.blit(CS_IMG, pygame.mouse.get_pos())
        #
        # pygame.display.flip()
        #
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
        #         elif event.type == pygame.MOUSEBUTTONDOWN:
        #             break
        #
        #     pygame.time.Clock().tick(60)


main_menu()


