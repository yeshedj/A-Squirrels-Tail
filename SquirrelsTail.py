import pygame, sys
from SquirrelsButtons import Button

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Squirrel's Tail")

original_BG = pygame.image.load("love is in the air.png")
BG = pygame.transform.scale(original_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))


# cursor_image = pygame.image.load("cursor.png")
# pygame.mouse.set_visible(False)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("papyrus", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("A SQUIRREL'S TAIL", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 180))

        PLAY_BUTTON = Button(image=pygame.image.load("PlayGameButton.png"), pos=(200, 400),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("QuitGameButton.png"), pos=(1200, 400),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play():
    # current_page = 0
    PLAY_BACK = Button(image=None, pos=(170, 510),
                       text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    PLAY_NEXT = Button(image=None, pos=(1200, 510),
                       text_input="NEXT", font=get_font(60), base_color="White", hovering_color="Pink")

    script_BG = pygame.image.load("newScriptBG.png")
    BG2 = pygame.transform.scale(script_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

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
                if PLAY_BACK.checkForInput(pygame.mouse.get_pos()):
                    main_menu()
                elif PLAY_NEXT.checkForInput(pygame.mouse.get_pos()):
                    next()

        # SCREEN.fill("black")
        SCREEN.blit(BG2, (0, 0))

        if counter < speed * len(message[-1]):
            counter += 1

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")

        if text_surface.get_width() > SCREEN_WIDTH - 20:  # 20 pixels padding
            text_y += font.get_linesize()

        SCREEN.blit(text_surface, (text_x, text_y))

        PLAY_BACK.changeColor(pygame.mouse.get_pos())
        PLAY_BACK.update(SCREEN)
        PLAY_NEXT.changeColor(pygame.mouse.get_pos())
        PLAY_NEXT.update(SCREEN)

        pygame.display.flip()

        pygame.time.Clock().tick(60)


def next():

    PLAY_BACK2 = Button(image=None, pos=(170, 510),
                        text_input="BACK", font=get_font(60), base_color="White", hovering_color="Yellow")
    PLAY_NEXT2 = Button(image=None, pos=(1200, 510),
                        text_input="NEXT", font=get_font(60), base_color="White", hovering_color="Pink")

    script_BG = pygame.image.load("newScriptBG.png")
    BG2 = pygame.transform.scale(script_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

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
                if PLAY_BACK2.checkForInput(pygame.mouse.get_pos()):
                    play()
                elif PLAY_NEXT2.checkForInput(pygame.mouse.get_pos()):
                    # script_BG = pygame.image.load("treeTrunk.png")
                    # BG2 = pygame.transform.scale(script_BG,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    gameplay()

        # SCREEN.fill("black")
        SCREEN.blit(BG2, (0, 0))

        if counter < speed * len(message[-1]):
            counter += 1

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")

        if text_surface.get_width() > SCREEN_WIDTH - 20:  # 20 pixels padding
            text_y += font.get_linesize()

        SCREEN.blit(text_surface, (text_x, text_y))

        PLAY_BACK2.changeColor(pygame.mouse.get_pos())
        PLAY_BACK2.update(SCREEN)
        PLAY_NEXT2.changeColor(pygame.mouse.get_pos())
        PLAY_NEXT2.update(SCREEN)

        pygame.display.flip()

        pygame.time.Clock().tick(60)


def gameplay():
        gameplay_BG = pygame.image.load("treeTrunk.png")
        GPBG = pygame.transform.scale(gameplay_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        SCREEN.blit(GPBG, (0, 0))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    break

            pygame.time.Clock().tick(60)


main_menu()


