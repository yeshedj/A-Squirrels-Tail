import pygame, sys
from SquirrelsButtons import Button
# import ptext



pygame.init()


SCREEN = pygame.display.set_mode((1400, 750))

pygame.display.set_caption("Squirrel's Tail")

original_BG = pygame.image.load("love is in the air.png")
BG = pygame.transform.scale(original_BG, (1400, 750))



# cursor_image = pygame.image.load("cursor.png")
# pygame.mouse.set_visible(False)






def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("papyrus", size)

def play():
    PLAY_BACK = Button(image=None, pos=(50, 50),
                       text_input="BACK", font=get_font(36), base_color="White", hovering_color="Green")

    SCREEN.fill("black")
    message = [
        "The love of your squirrel life is at the top! Climb up & collect hearts on the way to deliver to your beloved! Have fun!"]
    font = get_font(36)
    text_y = 300
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
                    return

        SCREEN.fill("black")
        pygame.draw.rect(SCREEN, "black", [0, 300, 800, 200])

        if counter < speed * len(message[-1]):
            counter += 1
        else:
            done = True

        text_to_render = "".join([line[:counter // speed] for line in message])
        text_surface = font.render(text_to_render, True, "white")
        SCREEN.blit(text_surface, (10, text_y))

        PLAY_BACK.changeColor(pygame.mouse.get_pos())
        PLAY_BACK.update(SCREEN)

        pygame.display.flip()

        pygame.time.Clock().tick(60)

    main_menu()




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

main_menu()






