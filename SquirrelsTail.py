import pygame, sys
from SquirrelsButtons import Button

# class Squirrel(pygame.sprite.Sprite):
#     def __init__(self, picture_path):
#         super().__init__()
#         self.image = pygame.image.load(picture_path)
#         self.rect = self.image.get_rect()
#     def update(self):
#         self.rect.center = pygame.mouse.get_pos()




pygame.init()


SCREEN = pygame.display.set_mode((1400, 750))

pygame.display.set_caption("Menu")

original_BG = pygame.image.load("love is in the air.png")
BG = pygame.transform.scale(original_BG, (1400, 750))



# cursor_image = pygame.image.load("cursor.png")
# pygame.mouse.set_visible(False)






def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("papyrus", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(700, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(700, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        # SCREEN.blit(cursor_image,PLAY_MOUSE_POS)
        pygame.display.update()

    
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("A SQUIRREL'S TAIL", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("PlayGameButton.JPG"), pos=(200, 400),
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("QuitGameButton.JPG"), pos=(1200, 400),
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

