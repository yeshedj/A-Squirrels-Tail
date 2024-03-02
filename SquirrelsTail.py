import pygame, sys
import random
import os
from SquirrelsButtons import Button
from spritesheet import SpriteSheet
from enemy import Enemy

pygame.init()

click = pygame.mixer.Sound("assets/wink.mp3")
# typing = pygame.mixer.Sound("typing.mp3")

pygame.mixer.init()
pygame.mixer.music.load("assets/fun.mp3")
pygame.mixer.music.play(-1)

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Squirrel's Tail")


cursor_image = pygame.image.load("assets/cursor.png")
CS_IMG = pygame.transform.scale(cursor_image, (90, 70))

pygame.mouse.set_visible(False)


def get_font(size):
    return pygame.font.SysFont("papyrus", size)


def main_menu():
    # pygame.mixer.music.play(-1)
    original_bg = pygame.image.load("assets/love is in the air.png")
    bg = pygame.transform.scale(original_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    menu_text = get_font(80).render("A SQUIRREL'S TAIL", True, "#b68f40")
    menu_rect = menu_text.get_rect(center=(700, 180))

    play_button = Button(image=pygame.image.load("assets/PlayGameButton.png"), pos=(200, 400), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    # quit_button = Button(image=pygame.image.load("QuitGameButton.png"), pos=(1200, 400), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    option_button = Button(image=pygame.image.load("assets/option.png"), pos=(1200, 400), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                if play_button.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    play()
                elif option_button.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    option()

            SCREEN.blit(bg, (0, 0))

            play_button.update(SCREEN)
            option_button.update(SCREEN)

            SCREEN.blit(menu_text, menu_rect)

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.blit(CS_IMG, MENU_MOUSE_POS)

            pygame.display.update()


def option():
    option_back = Button(image=None, pos=(170, 510), text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    option_bg = pygame.image.load("assets/optionBG.png")
    op_bg = pygame.transform.scale(option_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message = ["P.S. Happy Valentine's Day you cutie!"]
    font = get_font(35)

    text_width, text_height = font.size(message[0])
    text_x = (SCREEN_WIDTH - text_width) // 2
    text_y = (SCREEN_HEIGHT - text_height) // 2

    speed = 2
    counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_back.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    main_menu()
                elif not any(button.checkForInput(pygame.mouse.get_pos()) for button in [option_back]):
                    main_menu()

        SCREEN.blit(op_bg, (0, 0))

        if counter < speed * len(message[-1]):
            counter += 1

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")

        if text_surface.get_width() > SCREEN_WIDTH - 20:  # 20 pixels padding
            text_y += font.get_linesize()

        SCREEN.blit(text_surface, (text_x, text_y))

        option_back.changeColor(pygame.mouse.get_pos())
        option_back.update(SCREEN)

        SCREEN.blit(CS_IMG, pygame.mouse.get_pos())

        pygame.display.flip()

        pygame.time.Clock().tick(60)


def play():
    play_back = Button(image=None, pos=(170, 510),
                       text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    play_next = Button(image=None, pos=(1190, 510),
                       text_input="NEXT", font=get_font(60), base_color="White", hovering_color="Pink")

    script_bg = pygame.image.load("assets/newScriptBG.png")
    bg2 = pygame.transform.scale(script_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message = ["Your squirrel beloved is at the top! Climb as high as you can to try & reunite!"]

    font = get_font(35)

    text_width, text_height = font.size(message[0])
    text_x = (SCREEN_WIDTH - text_width) // 2
    text_y = (SCREEN_HEIGHT - text_height) // 2

    speed = 2
    counter = 0
    # done = False

    # typing.play()


    # while not done:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    main_menu()
                    # typing.stop()
                elif play_next.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    next()
                    # typing.stop()

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
    play_next2 = Button(image=None, pos=(1190, 510),
                        text_input="START", font=get_font(60), base_color="White", hovering_color="Pink")

    script_bg = pygame.image.load("assets/newScriptBG.png")
    bg2 = pygame.transform.scale(script_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    message = ["Use the left & right arrows to navigate & be careful not to fall!"]

    font = get_font(35)

    text_width, text_height = font.size(message[0])
    text_x = (SCREEN_WIDTH - text_width) // 2
    text_y = (SCREEN_HEIGHT - text_height) // 2

    speed = 2
    counter = 0
    # done = False

    # typing.play()

    # while not done:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back2.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    play()
                    # typing.stop()
                elif play_next2.checkForInput(pygame.mouse.get_pos()):
                    click.play()
                    gameplay(SCREEN)
                    # typing.stop()

        SCREEN.blit(bg2, (0, 0))

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
    #     if counter >= speed * len(message[-1]):
    #         break
    #
    # typing.stop()

def gameplay(SCREEN):
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600

    # create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A Squirrel's Tail")

    # set frame rate
    clock = pygame.time.Clock()
    FPS = 60

    # game variables
    SCROLL_THRESH = 200
    GRAVITY = 1
    MAX_PLATFORMS = 10
    scroll = 0
    bg_scroll = 0
    game_over = False
    score = 0
    fade_counter = 0

    if os.path.exists('score.txt'):
        with open('score.txt', 'r') as file:
            high_score = int(file.read())
    else:
        high_score = 0

    # define colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PANEL = (153, 217, 234)

    # define font
    font_small = pygame.font.SysFont('Lucida Sans', 20)
    font_big = pygame.font.SysFont('Lucida Sans', 24)

    # load images
    squirrel_img = pygame.image.load("assets/LoverBoy.png").convert_alpha()
    image = pygame.image.load("assets/rolling bg.png").convert_alpha()
    bg_image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    platform_img = pygame.image.load("assets/wood.png").convert_alpha()
    bird_sheet_img = pygame.image.load("assets/bird.png").convert_alpha()
    bird_sheet = SpriteSheet(bird_sheet_img)

    # function for outputting text onto the screen
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # function for drawing info panel
    def draw_panel():
        pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
        pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
        draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

    # function for drawing the background
    def draw_bg(bg_scroll):
        screen.blit(bg_image, (0, 0 + bg_scroll))
        screen.blit(bg_image, (0, -600 + bg_scroll))

    # player class
    class Player():
        def __init__(self, x, y):
            self.image = pygame.transform.scale(squirrel_img, (75, 75))
            self.width = 40
            self.height = 70
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = (x, y)
            self.vel_y = 0
            self.flip = False

        def move(self):
            # reset variables
            scroll = 0
            dx = 0
            dy = 0

            # process keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                dx = -10
                self.flip = True
            if key[pygame.K_RIGHT]:
                dx = 10
                self.flip = False

            # gravity
            self.vel_y += GRAVITY
            dy += self.vel_y

            # ensure player doesn't go off the edge of the screen
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > SCREEN_WIDTH:
                dx = SCREEN_WIDTH - self.rect.right

            # check collision with platforms
            for platform in platform_group:
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if above the platform
                    if self.rect.bottom < platform.rect.centery:
                        if self.vel_y > 0:
                            self.rect.bottom = platform.rect.top
                            dy = 0
                            self.vel_y = -20

            # check if the player has bounced to the top of the screen
            if self.rect.top <= SCROLL_THRESH:
                # if player is jumping
                if self.vel_y < 0:
                    scroll = -dy

            # update rectangle position
            self.rect.x += dx
            self.rect.y += dy + scroll

            # update mask
            self.mask = pygame.mask.from_surface(self.image)

            return scroll

        def draw(self):
            screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))

    # platform class
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, moving):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(platform_img, (width, 10))
            self.moving = moving
            self.move_counter = random.randint(0, 50)
            self.direction = random.choice([-1, 1])
            self.speed = random.randint(1, 2)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self, scroll):
            # moving platform side to side if it is a moving platform
            if self.moving == True:
                self.move_counter += 1
                self.rect.x += self.direction * self.speed

            # change platform direction if it has moved fully or hit a wall
            if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.direction *= -1
                self.move_counter = 0

            # update platform's vertical position
            self.rect.y += scroll

            # check if platform has gone off the screen
            if self.rect.top > SCREEN_HEIGHT:
                self.kill()

    # player instance
    squirrel = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

    # create sprite groups
    platform_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    # create starting platform
    platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
    platform_group.add(platform)

    # game loop
    run = True
    while run:

        clock.tick(FPS)

        if game_over == False:
            scroll = squirrel.move()

            # draw background
            bg_scroll += scroll
            if bg_scroll >= 600:
                bg_scroll = 0
            draw_bg(bg_scroll)

            # generate platforms
            if len(platform_group) < MAX_PLATFORMS:
                p_w = random.randint(40, 60)
                p_x = random.randint(0, SCREEN_WIDTH - p_w)
                p_y = platform.rect.y - random.randint(80, 120)
                p_type = random.randint(1, 2)
                if p_type == 1 and score > 500:
                    p_moving = True
                else:
                    p_moving = False
                platform = Platform(p_x, p_y, p_w, p_moving)
                platform_group.add(platform)

            # update platforms
            platform_group.update(scroll)

            # generate enemies
            if len(enemy_group) == 0 and score > 1500:
                enemy = Enemy(SCREEN_WIDTH, 100, bird_sheet, 1.5)
                enemy_group.add(enemy)

            # update enemies
            enemy_group.update(scroll, SCREEN_WIDTH)

            # update score
            if scroll > 0:
                score += scroll

            # draw line at previous high score
            pygame.draw.line(screen, WHITE, (0, score - high_score + SCROLL_THRESH),
                             (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
            draw_text('HIGH SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

            # draw sprites
            platform_group.draw(screen)
            enemy_group.draw(screen)
            squirrel.draw()

            # draw panel
            draw_panel()

            # check game over
            if squirrel.rect.top > SCREEN_HEIGHT:
                game_over = True
            # check for collision with enemies
            if pygame.sprite.spritecollide(squirrel, enemy_group, False):
                if pygame.sprite.spritecollide(squirrel, enemy_group, False, pygame.sprite.collide_mask):
                    game_over = True
        else:
            if fade_counter < SCREEN_WIDTH:
                fade_counter += 5
                for y in range(0, 6, 2):
                    pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
            else:
                draw_text('GAME OVER!', font_big, WHITE, 130, 200)
                draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
                draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 40, 300)
                # update high score
                if score > high_score:
                    high_score = score
                    with open('score.txt', 'w') as file:
                        file.write(str(high_score))
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    # reset variables
                    game_over = False
                    score = 0
                    scroll = 0
                    fade_counter = 0
                    # reposition jumpy
                    squirrel.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                    # reset enemies
                    enemy_group.empty()
                    # reset platforms
                    platform_group.empty()
                    # create starting platform
                    platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
                    platform_group.add(platform)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # update high score
                if score > high_score:
                    high_score = score
                    with open('score.txt', 'w') as file:
                        file.write(str(high_score))
                run = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

main_menu()
